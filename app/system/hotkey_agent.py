"""Standalone global-hotkey listener process.

pynput's X11 record-extension thread is known to segfault occasionally;
running it in this separate process keeps the main app alive. Prints a
line to stdout whenever the hotkey fires; the app restarts the agent if
it dies.
"""
import sys


def main():
    from pynput import keyboard

    def on_hotkey():
        print("HOTKEY", flush=True)

    with keyboard.GlobalHotKeys({'<ctrl>+<shift>+v': on_hotkey}) as listener:
        listener.join()


if __name__ == "__main__":
    sys.exit(main())
