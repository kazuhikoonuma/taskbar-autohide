import io
import threading
import time
import sys
import ctypes
import ctypes.wintypes as wintypes
import cairosvg  # LGPL-3.0
from PIL import Image  # MIT-CMU
import pystray  # GPL-3.0 or LGPL-3.0
from pystray import MenuItem
from tendo.singleton import SingleInstance, SingleInstanceException  # PSF-2.0
from winotify import Notification  # MIT

ICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128">
  <rect x = "8" y="22" width="112" height="84" fill="white" rx="12" ry="12" stroke="#1e1f22" stroke-width="4"/>
  <rect x = "18" y="32" width="92" height="64" fill="#1e1f22" rx="6" ry="6"/>
  <rect x = "12" y="74" width="104" height="8" fill="white"/>
</svg>
"""

ABM_GETSTATE = 0x00000004
ABM_SETSTATE = 0x0000000A
ABS_AUTOHIDE = 0x0000001
ABS_ALWAYSONTOP = 0x0000002
PROCESS_PER_MONITOR_DPI_AWARE = 2
PROGRAM_NAME = 'Autohide'
PROGRAM_TITLE = 'Taskbar Autohide'


class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long)
    ]

class APPBARDATA(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_ulong),
        ("hWnd", wintypes.HWND),
        ("uCallbackMessage", ctypes.c_uint),
        ("uEdge", ctypes.c_uint),
        ("rc", RECT),
        ("lParam", ctypes.c_int)
    ]

def svg_to_image(svg_data: str) -> Image.Image:
    png_data = cairosvg.svg2png(bytestring=svg_data.encode('utf-8'))
    return Image.open(io.BytesIO(png_data))

def on_quit(icon, item):
    icon.stop()

def set_dpi_awareness():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

def ensure_single_instance(program_name: str) -> SingleInstance:
    try:
        instance = SingleInstance(program_name)
        return instance
    except SingleInstanceException:
        sys.exit()

def show_notification(title: str, message: str) -> int:
    toast = Notification(app_id=PROGRAM_NAME, title=title, msg=message)
    toast.show()
    return 0

def get_taskbar_state() -> int:
    abd = APPBARDATA()
    abd.cbSize = ctypes.sizeof(APPBARDATA)
    return ctypes.windll.shell32.SHAppBarMessage(ABM_GETSTATE, ctypes.byref(abd))

def get_taskbar_autohide() -> bool:
    return bool(get_taskbar_state() & ABS_AUTOHIDE)

def set_taskbar_autohide(auto_hide: bool) -> bool:
    if auto_hide:
        new_state = get_taskbar_state() | ABS_AUTOHIDE
    else:
        new_state = get_taskbar_state() & ~ABS_AUTOHIDE
    abd = APPBARDATA()
    abd.cbSize = ctypes.sizeof(APPBARDATA)
    abd.lParam = new_state
    result = ctypes.windll.shell32.SHAppBarMessage(ABM_SETSTATE, ctypes.byref(abd))
    return bool(result)

def monitor_taskbar_autohide():
    show_notification(PROGRAM_TITLE, 'Autohide monitor started.')
    while True:
        try:
            if not get_taskbar_autohide():
                set_taskbar_autohide(True)
                show_notification(PROGRAM_TITLE, 'Autohide is disabled. Re-enabling...')
        except Exception:
            pass
        time.sleep(10)

def main():
    me = ensure_single_instance(PROGRAM_NAME)
    set_dpi_awareness()

    icon = pystray.Icon(
        name=PROGRAM_NAME,
        icon=svg_to_image(ICON_SVG),
        menu=pystray.Menu(MenuItem('Quit', on_quit)),
        title=PROGRAM_TITLE,
    )

    poll_thread = threading.Thread(target=monitor_taskbar_autohide, daemon=True)
    poll_thread.start()

    icon.run()


if __name__ == "__main__":
    main()
