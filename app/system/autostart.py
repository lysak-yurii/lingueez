"""OS autostart entry management (Linux .desktop / Windows registry).

Uses its own app name so it never clashes with the original app's entry.
"""
import logging
import os
import sys

_APP_NAME = "Dictionary"
_DISPLAY_NAME = "Dictionary"


def _get_app_command_and_workdir():
    if getattr(sys, 'frozen', False):
        exe = os.path.abspath(sys.executable)
        return exe, os.path.dirname(exe)
    app_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
    run_sh = os.path.join(app_dir, 'run.sh')
    if sys.platform != 'win32' and os.path.isfile(run_sh):
        return run_sh, app_dir
    return f"{sys.executable} {os.path.join(app_dir, 'main.py')}", app_dir


def set_autostart(enabled: bool):
    if sys.platform == 'win32':
        _set_autostart_windows(enabled)
    else:
        _set_autostart_linux(enabled)


def get_autostart_enabled() -> bool:
    if sys.platform == 'win32':
        return _get_autostart_windows()
    return _get_autostart_linux()


def _set_autostart_linux(enabled: bool):
    autostart_dir = os.path.expanduser("~/.config/autostart")
    desktop_file = os.path.join(autostart_dir, f"{_APP_NAME}.desktop")
    if enabled:
        os.makedirs(autostart_dir, exist_ok=True)
        exec_cmd, workdir = _get_app_command_and_workdir()
        content = (
            "[Desktop Entry]\n"
            "Type=Application\n"
            f"Name={_DISPLAY_NAME}\n"
            f"Exec={exec_cmd} --minimized\n"
            f"Path={workdir}\n"
            "Hidden=false\n"
            "NoDisplay=false\n"
            "X-GNOME-Autostart-enabled=true\n"
        )
        with open(desktop_file, "w") as fh:
            fh.write(content)
    elif os.path.exists(desktop_file):
        os.remove(desktop_file)


def _get_autostart_linux() -> bool:
    return os.path.exists(os.path.expanduser(f"~/.config/autostart/{_APP_NAME}.desktop"))


def _set_autostart_windows(enabled: bool):
    try:
        import winreg
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        if enabled:
            exec_cmd, _ = _get_app_command_and_workdir()
            winreg.SetValueEx(key, _APP_NAME, 0, winreg.REG_SZ, f"{exec_cmd} --minimized")
        else:
            try:
                winreg.DeleteValue(key, _APP_NAME)
            except FileNotFoundError:
                pass
        winreg.CloseKey(key)
    except Exception as exc:
        logging.error(f"Failed to set autostart registry key: {exc}")


def _get_autostart_windows() -> bool:
    try:
        import winreg
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        try:
            winreg.QueryValueEx(key, _APP_NAME)
            return True
        except FileNotFoundError:
            return False
        finally:
            winreg.CloseKey(key)
    except Exception:
        return False
