"""
System control tool — open applications, control mouse/keyboard.

Stub. Suggested implementations:
    - Open apps: `subprocess` + platform-specific command (e.g. `open -a` on
      macOS, `start` on Windows, `xdg-open` on Linux)
    - Mouse/keyboard: `pyautogui`
"""

import platform
import subprocess


def open_application(app_name: str) -> str:
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(["open", "-a", app_name], check=True)
        elif system == "Windows":
            subprocess.run(["start", app_name], shell=True, check=True)
        else:  # Linux
            subprocess.run(["xdg-open", app_name], check=True)
        return f"Opened {app_name}"
    except Exception as e:
        return f"Could not open {app_name}: {e}"
