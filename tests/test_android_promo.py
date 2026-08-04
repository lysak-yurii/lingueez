# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for the Android cross-sell gate and its Play attribution URL.

The gate decides who ever sees the one-time banner, so its failure modes are the
ones that matter: nagging someone twice, or showing a phone-app pitch to someone
whose data never leaves the machine.

Run:  QT_QPA_PLATFORM=offscreen python -m unittest tests.test_android_promo
"""

import os
import sys
import unittest
from unittest import mock
from urllib.parse import parse_qs, unquote, urlparse

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import version  # noqa: E402
from app.ui import android_promo as promo  # noqa: E402


class FakeAuth:
    def __init__(self, logged_in=False, local=False):
        self._logged_in = logged_in
        self._local = local

    def is_logged_in(self):
        return self._logged_in

    def is_local_active(self):
        return self._local


def _builtin_server():
    """Patch out the own-server check — the built-in project is the normal case."""
    return mock.patch("app.core.supabase_client.is_custom_server", return_value=False)


class ShouldShowPromoTests(unittest.TestCase):
    def test_fresh_cloud_sign_in_qualifies(self):
        with _builtin_server():
            self.assertTrue(promo.should_show_promo({}, FakeAuth(logged_in=True)))

    def test_signed_out_never_qualifies(self):
        with _builtin_server():
            self.assertFalse(promo.should_show_promo({}, FakeAuth()))

    def test_offline_profile_never_qualifies(self):
        # An offline profile has no cloud session to share with a phone.
        with _builtin_server():
            self.assertFalse(promo.should_show_promo({}, FakeAuth(logged_in=True, local=True)))

    def test_own_server_users_never_qualify(self):
        with mock.patch("app.core.supabase_client.is_custom_server", return_value=True):
            self.assertFalse(promo.should_show_promo({}, FakeAuth(logged_in=True)))

    def test_missing_auth_is_tolerated(self):
        with _builtin_server():
            self.assertFalse(promo.should_show_promo({}, None))

    def test_dismissing_retires_it(self):
        with _builtin_server():
            self.assertFalse(
                promo.should_show_promo({promo.DISMISSED_KEY: "True"}, FakeAuth(logged_in=True))
            )

    def test_flag_is_parsed_from_text(self):
        # settings.cfg stores everything as text; "False" must not read as truthy.
        with _builtin_server():
            self.assertTrue(
                promo.should_show_promo({promo.DISMISSED_KEY: "False"}, FakeAuth(logged_in=True))
            )


class RecordingTests(unittest.TestCase):
    """The writer, with save_settings stubbed out — no settings.cfg is touched."""

    def setUp(self):
        patcher = mock.patch.object(promo, "save_settings")
        self.save = patcher.start()
        self.addCleanup(patcher.stop)

    def test_dismissing_sets_and_persists_the_flag(self):
        settings = {}
        promo._record_dismissed(settings)
        self.assertTrue(promo.get_bool(settings, promo.DISMISSED_KEY, False))
        self.save.assert_called_once()


class AndroidUrlTests(unittest.TestCase):
    def test_points_at_the_published_listing(self):
        url = urlparse(version.android_url("menu"))
        self.assertEqual(url.netloc, "play.google.com")
        self.assertEqual(parse_qs(url.query)["id"], ["app.lingueez.mobile"])

    def test_referrer_is_a_url_encoded_query_string(self):
        # Play hands the decoded referrer to the install, so it has to survive one
        # round of decoding as a query string of its own.
        referrer = parse_qs(urlparse(version.android_url("nudge")).query)["referrer"][0]
        self.assertEqual(
            parse_qs(unquote(referrer)),
            {
                "utm_source": ["desktop"],
                "utm_medium": ["in-app"],
                "utm_campaign": ["nudge"],
            },
        )

    def test_each_surface_is_distinguishable(self):
        urls = {version.android_url(s) for s in ("menu", "about", "settings", "nudge")}
        self.assertEqual(len(urls), 4)


class BannerTests(unittest.TestCase):
    """The rule that motivates the whole design: display is not an answer."""

    @classmethod
    def setUpClass(cls):
        from PySide6.QtWidgets import QApplication

        cls._qapp = QApplication.instance() or QApplication(sys.argv[:1])

    def _host(self):
        from PySide6.QtWidgets import QVBoxLayout, QWidget
        from app.ui import theme

        host = QWidget()
        return host, QVBoxLayout(host), theme.current_colors()

    def test_showing_the_banner_writes_nothing(self):
        host, layout, colors = self._host()
        settings = {}
        with mock.patch.object(promo, "save_settings") as save:
            promo.show_promo_banner(host, layout, 0, settings, colors)
            save.assert_not_called()
        self.assertEqual(settings, {})
        # So a user who ignored it the first time is still eligible next launch.
        with _builtin_server():
            self.assertTrue(promo.should_show_promo(settings, FakeAuth(logged_in=True)))

    def test_dismissing_the_banner_retires_it(self):
        host, layout, colors = self._host()
        settings = {}
        with mock.patch.object(promo, "save_settings"):
            banner = promo.show_promo_banner(host, layout, 0, settings, colors)
            banner.dismiss()
        with _builtin_server():
            self.assertFalse(promo.should_show_promo(settings, FakeAuth(logged_in=True)))

    def test_refresh_theme_retints_every_styled_child(self):
        # The banner paints from inline stylesheets, so a live theme switch only
        # reaches it if MainWindow._refresh_icons calls refresh_theme.
        from app.ui import theme

        host, layout, _ = self._host()
        with mock.patch.object(promo, "save_settings"):
            banner = promo.show_promo_banner(host, layout, 0, {}, theme.LIGHT)
        light = (
            banner.styleSheet(),
            banner._head.styleSheet(),
            banner._sub.styleSheet(),
            banner._get_btn.styleSheet(),
        )
        banner.refresh_theme(theme.DARK)
        dark = (
            banner.styleSheet(),
            banner._head.styleSheet(),
            banner._sub.styleSheet(),
            banner._get_btn.styleSheet(),
        )
        for before, after in zip(light, dark, strict=True):
            self.assertNotEqual(before, after)
        self.assertIn(theme.DARK["accent_soft"], banner.styleSheet())

    def test_main_window_refreshes_the_banner_on_theme_change(self):
        # Guards the wiring, not the widget: _refresh_icons must reach the banner.
        import inspect
        from app.ui.main_window import MainWindow

        source = inspect.getsource(MainWindow._refresh_icons)
        self.assertIn("_android_banner", source)
        self.assertIn("refresh_theme", source)

    def test_opening_the_dialog_counts_as_an_answer(self):
        # "Get the app…" hands off to the QR dialog and must retire the strip too,
        # otherwise it would keep returning to someone who already installed it.
        host, layout, colors = self._host()
        settings = {}
        with (
            mock.patch.object(promo, "save_settings"),
            mock.patch.object(promo, "open_android_dialog") as open_dialog,
        ):
            banner = promo.show_promo_banner(host, layout, 0, settings, colors)
            banner._details()
            open_dialog.assert_called_once()
        self.assertTrue(promo.get_bool(settings, promo.DISMISSED_KEY, False))


class QrPixmapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from PySide6.QtWidgets import QApplication

        cls._qapp = QApplication.instance() or QApplication(sys.argv[:1])

    def test_renders_at_the_requested_logical_size(self):
        pm = promo.qr_pixmap(version.android_url("menu"), size=160, dpr=2.0)
        self.assertFalse(pm.isNull())
        # Device pixels are snapped to whole modules, so the raw size is only
        # approximately size*dpr — but the logical size must land exactly.
        self.assertAlmostEqual(pm.width() / pm.devicePixelRatio(), 160, places=6)

    def test_modules_are_whole_device_pixels(self):
        # Uneven module widths are what makes a small QR fail to scan.
        import segno

        url = version.android_url("nudge")
        modules = len(list(segno.make(url, error="m").matrix_iter(border=promo._QR_BORDER)))
        pm = promo.qr_pixmap(url, size=52, dpr=2.0)
        self.assertEqual(pm.width() % modules, 0)


if __name__ == "__main__":
    unittest.main()
