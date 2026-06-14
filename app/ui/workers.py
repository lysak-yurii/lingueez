# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Additional terms under AGPL-3.0 section 7 apply to this program; see the
# NOTICE file distributed with this source for details.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Background-thread helpers for keeping the UI responsive."""
import traceback

from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot


class _WorkerReaper(QObject):
    """Holds finished-but-undelivered workers and releases them safely.

    QThreadPool's autoDelete destroys the QRunnable in the *pool* thread the
    moment run() returns — taking the Python wrapper and its WorkerSignals
    QObject with it while queued result/progress emissions may still be in
    flight to the GUI thread. Destroying a QObject from the wrong thread mid
    delivery segfaults. So workers are kept referenced here and dropped via a
    queued signal: the release runs on the GUI thread *after* every signal the
    worker posted earlier (per-thread event FIFO), making destruction safe.
    """

    _release = Signal(object)

    def __init__(self):
        super().__init__()
        self._alive = set()
        self._release.connect(self._on_release)

    def hold(self, worker):
        self._alive.add(worker)

    def release_later(self, worker):
        # safe from the pool thread: queues onto the GUI thread
        self._release.emit(worker)

    def _on_release(self, worker):
        self._alive.discard(worker)


_reaper = _WorkerReaper()


class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(str)
    result = Signal(object)
    progress = Signal(object, object)


class Worker(QRunnable):
    """Run *fn(*args, **kwargs)* on the global thread pool.

    If the callable accepts a ``progress_callback`` kwarg it receives a
    callable forwarding to the ``progress`` signal.
    """

    def __init__(self, fn, *args, wants_progress=False, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        if wants_progress:
            self.kwargs['progress_callback'] = self._emit_progress

    def _emit_progress(self, a=None, b=None):
        self.signals.progress.emit(a, b)

    @Slot()
    def run(self):
        # Emits can fail with RuntimeError when the app is shutting down and
        # the receiving QObject has already been deleted — that's harmless.
        try:
            result = self.fn(*self.args, **self.kwargs)
        except RuntimeError:
            return
        except Exception as exc:  # noqa: BLE001 - report to UI
            traceback.print_exc()
            try:
                self.signals.error.emit(str(exc))
            except RuntimeError:
                return
        else:
            try:
                self.signals.result.emit(result)
            except RuntimeError:
                return
        finally:
            try:
                self.signals.finished.emit()
            except RuntimeError:
                pass


def run_in_thread(fn, *args, on_result=None, on_error=None, on_finished=None,
                  on_progress=None, wants_progress=False, **kwargs):
    """Convenience wrapper; returns the Worker (keep a reference if needed)."""
    worker = Worker(fn, *args, wants_progress=wants_progress, **kwargs)
    if on_result:
        worker.signals.result.connect(on_result)
    if on_error:
        worker.signals.error.connect(on_error)
    if on_finished:
        worker.signals.finished.connect(on_finished)
    if on_progress:
        worker.signals.progress.connect(on_progress)
    # lifetime is managed by the reaper, not the pool — see _WorkerReaper
    worker.setAutoDelete(False)
    _reaper.hold(worker)
    worker.signals.finished.connect(lambda: _reaper.release_later(worker))
    QThreadPool.globalInstance().start(worker)
    return worker
