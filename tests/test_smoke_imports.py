# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Release smoke test: every module under ``app/`` must import cleanly.

This is the cheapest guard against the class of breakage (a typo, a bad import,
a Qt-at-import-time mistake) that otherwise only surfaces at runtime in a frozen
PyInstaller build. Qt runs headless via the offscreen platform plugin, and the
UI language is initialised first because several UI modules build ``tr()``
constants at import time.

Run:  QT_QPA_PLATFORM=offscreen python -m unittest tests.test_smoke_imports
"""

import importlib
import os
import pkgutil
import sys
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _ROOT)


def _iter_app_modules():
    """Yield the dotted name of every module in the ``app`` package."""
    import app

    for info in pkgutil.walk_packages(app.__path__, prefix="app."):
        yield info.name


class SmokeImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # A QApplication must exist before importing widgets that build objects
        # needing one; offscreen keeps it headless.
        try:
            from PySide6.QtWidgets import QApplication

            cls._qapp = QApplication.instance() or QApplication(sys.argv[:1])
        except Exception as exc:  # pragma: no cover - PySide6 should be installed
            raise unittest.SkipTest(f"PySide6 unavailable: {exc}")
        # UI modules read the active language at import time.
        from app.i18n import set_language

        set_language("en")

    def test_all_app_modules_import(self):
        failures = []
        for name in _iter_app_modules():
            try:
                importlib.import_module(name)
            except Exception as exc:  # noqa: BLE001 - we want every failure reported
                failures.append(f"{name}: {type(exc).__name__}: {exc}")
        self.assertEqual(failures, [], "module import failures:\n" + "\n".join(failures))

    def test_locales_import(self):
        import locales

        failures = []
        for info in pkgutil.iter_modules(locales.__path__, prefix="locales."):
            try:
                importlib.import_module(info.name)
            except Exception as exc:  # noqa: BLE001
                failures.append(f"{info.name}: {type(exc).__name__}: {exc}")
        self.assertEqual(failures, [], "locale import failures:\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
