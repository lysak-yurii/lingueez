# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for the Android cross-sell gate and its Play attribution URL.

The gate decides who ever sees the one-time banner, so its failure modes are the
ones that matter: nagging someone twice, interrupting someone who has barely
started a library, or telling a user their words are already on a phone when
they are not.

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


class ShouldShowPromoTests(unittest.TestCase):
    """The gate is now about the library, not the account."""

    def test_a_library_worth_carrying_qualifies(self):
        self.assertTrue(promo.should_show_promo({}, promo.MIN_WORDS + 1))

    def test_a_handful_of_words_does_not(self):
        # Someone still trying the app out should not be pitched a second client.
        for count in (0, 1, promo.MIN_WORDS):
            with self.subTest(words=count):
                self.assertFalse(promo.should_show_promo({}, count))

    def test_the_account_kind_no_longer_decides(self):
        # Offline profiles and own-server users study the same vocabulary, so they
        # get the same invitation — what changes for them is the wording.
        for auth in (FakeAuth(), FakeAuth(logged_in=True),
                     FakeAuth(logged_in=True, local=True)):
            with self.subTest(auth=vars(auth)):
                self.assertTrue(promo.should_show_promo({}, 12))

    def test_a_missing_count_is_tolerated(self):
        self.assertFalse(promo.should_show_promo({}, None))

    def test_dismissing_retires_it(self):
        self.assertFalse(promo.should_show_promo({promo.DISMISSED_KEY: "True"}, 500))

    def test_flag_is_parsed_from_text(self):
        # settings.cfg stores everything as text; "False" must not read as truthy.
        self.assertTrue(promo.should_show_promo({promo.DISMISSED_KEY: "False"}, 12))


class ContinuityLineTests(unittest.TestCase):
    """The claim has to match the user. Only a cloud account already has its words
    on the server the phone reads; the phone app has no offline mode, so everyone
    else must be told it takes an account rather than that they are already set."""

    def _line(self, auth, long_form=False):
        # Resolve against the real predicate first, then stand in for it — the
        # line picks its claim from the no-argument call inside _continuity_line.
        answer = promo.has_cloud_library(auth)
        with mock.patch.object(promo, "has_cloud_library", return_value=answer):
            return promo._continuity_line(long_form=long_form)

    def test_a_cloud_account_is_told_its_words_are_already_there(self):
        for long_form in (False, True):
            line = self._line(FakeAuth(logged_in=True), long_form)
            self.assertIn("already there", line)

    def test_everyone_else_is_told_what_it_takes(self):
        for auth in (FakeAuth(), FakeAuth(logged_in=True, local=True)):
            for long_form in (False, True):
                with self.subTest(auth=vars(auth), long_form=long_form):
                    line = self._line(auth, long_form)
                    self.assertNotIn("already there", line)
                    self.assertIn("account", line)

    def test_offline_profiles_have_no_cloud_library(self):
        self.assertFalse(promo.has_cloud_library(FakeAuth(logged_in=True, local=True)))
        self.assertFalse(promo.has_cloud_library(FakeAuth()))
        self.assertTrue(promo.has_cloud_library(FakeAuth(logged_in=True)))

    def test_an_unusable_auth_manager_does_not_break_the_strip(self):
        class Exploding:
            def is_logged_in(self):
                raise RuntimeError("keyring is on fire")

        self.assertFalse(promo.has_cloud_library(Exploding()))


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
        self.assertTrue(promo.should_show_promo(settings, 12))

    def test_dismissing_the_banner_retires_it(self):
        host, layout, colors = self._host()
        settings = {}
        with mock.patch.object(promo, "save_settings"):
            banner = promo.show_promo_banner(host, layout, 0, settings, colors)
            banner.dismiss()
        self.assertFalse(promo.should_show_promo(settings, 12))

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

    def test_main_window_feeds_the_gate_a_word_count(self):
        # Guards the wiring, not the widget: the gate now takes a count, so a
        # call site still passing an auth manager would silently always qualify.
        import inspect
        from app.ui.main_window import MainWindow

        source = inspect.getsource(MainWindow._maybe_show_android_promo)
        self.assertIn("word_count", source)
        self.assertIn("should_show_promo(self.settings, word_count)", source)

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


class PhoneMockTests(unittest.TestCase):
    """The drawn preview. It has no state, so what matters is that it paints at
    every size the dialog can give it and stays tied to the shared status ramp."""

    @classmethod
    def setUpClass(cls):
        from PySide6.QtWidgets import QApplication

        cls._qapp = QApplication.instance() or QApplication(sys.argv[:1])

    def _render(self, colors, width, height):
        from PySide6.QtGui import QPixmap
        from PySide6.QtWidgets import QWidget

        # Parented so the widget lives inside a normal widget tree, and rendered
        # into a pixmap so paintEvent actually runs offscreen.
        host = QWidget()
        mock = promo.PhoneMock(colors, host)
        mock.resize(width, height)
        pm = QPixmap(width, height)
        pm.fill()
        mock.render(pm)
        return pm

    def test_paints_at_every_size_in_both_themes(self):
        from app.ui import theme

        for colors in (theme.LIGHT, theme.DARK):
            for height in (340, 420, 520):
                with self.subTest(theme=colors["bg"], height=height):
                    pm = self._render(colors, promo._MOCK_W, height)
                    self.assertFalse(pm.isNull())

    def test_takes_its_chrome_from_the_palette_it_is_handed(self):
        from app.ui import theme

        light = self._render(theme.LIGHT, promo._MOCK_W, 420).toImage()
        dark = self._render(theme.DARK, promo._MOCK_W, 420).toImage()
        self.assertNotEqual(light, dark)
        # The phone body is the palette's surface, so a light theme must not be
        # painting a hard-coded dark chrome (or vice versa). Sampled in the blank
        # right-hand margin of the first row, clear of every glyph and hairline.
        blank = (180, 108)
        self.assertEqual(light.pixelColor(*blank).name(), theme.LIGHT["surface"])
        self.assertEqual(dark.pixelColor(*blank).name(), theme.DARK["surface"])

    def test_rows_use_the_shared_status_ramp(self):
        # The desktop and the phone show one library, so the spine colours have to
        # come from theme.status_style() rather than a copy that can drift.
        from app.ui import theme

        calls = []
        real = theme.status_style
        with mock.patch.object(theme, "status_style",
                               side_effect=lambda s: calls.append(s) or real(s)):
            self._render(theme.LIGHT, promo._MOCK_W, 420)

        self.assertTrue(calls, "the rows painted no status spine at all")
        self.assertLessEqual(set(calls), {s for s, _, _, _ in promo._MOCK_ROWS})
        # An unknown status would quietly take the grey fallback and imply no
        # progress level, which is exactly what the preview must not show.
        for status in calls:
            self.assertIsNot(real(status), theme.STATUS_FALLBACK, status)

    def test_shares_the_phone_app_s_first_five_words(self):
        # lingueez-mobile draws these same five, in this order, in its own mock of
        # the desktop. Whoever sees both previews should see one library.
        self.assertEqual(
            [(term, translation) for _, term, translation, _ in promo._MOCK_ROWS[:5]],
            [
                ("neighborhood", "el barrio"),
                ("le dépaysement", "change of scenery"),
                ("наполегливість", "perseverance"),
                ("die Umwelt", "довкілля"),
                ("breakfast", "le petit-déjeuner"),
            ],
        )


class AndroidDialogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from PySide6.QtWidgets import QApplication

        cls._qapp = QApplication.instance() or QApplication(sys.argv[:1])

    def test_builds_under_both_palettes_and_keeps_the_attributed_url(self):
        from app.ui import theme

        for palette in (theme.LIGHT, theme.DARK):
            with (self.subTest(theme=palette["bg"]),
                  mock.patch.object(theme, "current_colors", return_value=palette)):
                dialog = promo.AndroidDialog(surface="settings")
                self.addCleanup(dialog.deleteLater)
                self.assertEqual(dialog._url, version.android_url("settings"))
                self.assertIsInstance(dialog._mock, promo.PhoneMock)

    def test_copy_puts_the_attributed_url_on_the_clipboard(self):
        from PySide6.QtWidgets import QApplication

        dialog = promo.AndroidDialog(surface="about")
        self.addCleanup(dialog.deleteLater)
        dialog._copy()
        self.assertEqual(QApplication.clipboard().text(),
                         version.android_url("about"))


if __name__ == "__main__":
    unittest.main()
