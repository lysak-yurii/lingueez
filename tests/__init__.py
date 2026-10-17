# Lingueez test suite. Marks ``tests`` as a package so ``unittest discover``
# (and CI) can collect every ``test_*.py`` module.
import atexit

from PySide6 import QtCore  # noqa: F401  (imported first so the hook below runs before PySide's exit cleanup)


def _delete_leftover_widgets():
    # PySide6 6.12 frees widgets still alive at exit twice (children added via a
    # sub-layout stay Python-owned) and segfaults after an all-green run.
    from PySide6.QtWidgets import QApplication
    from shiboken6 import Shiboken

    app = QApplication.instance()
    if isinstance(app, QApplication):
        for widget in app.topLevelWidgets():
            if Shiboken.isValid(widget):
                Shiboken.delete(widget)


atexit.register(_delete_leftover_widgets)
