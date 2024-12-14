import pygetwindow as gw
import time
from pywinauto import Desktop
import pyautogui
import win32gui
import win32con
import win32api


def left_click() -> None:
    pyautogui.leftClick()


def get_mouse_position(hwnd):
    x, y = pyautogui.position()

    rect = win32gui.GetWindowRect(hwnd)
    x0, y0, x1, y1 = rect

    x_rel = x - x0
    y_rel = y - y0

    x_rel = max(0, min(x_rel, x1 - x0))
    y_rel = max(0, min(y_rel, y1 - y0))

    return x_rel, y_rel


def get_window_hwnd_by_title(title: str) -> int:
    windows = gw.getWindowsWithTitle(title)
    windows_hwnd = []
    for window in windows:
        print(f"Window Title: {window.title}, Window ID: {window._hWnd}")
        windows_hwnd.append(window._hWnd)
    return windows_hwnd


def get_focus_window(hwnd: int, title: str) -> None:
    desktop = Desktop(backend="uia")
    window = desktop.windows(title=title, handle=hwnd)[0].set_focus()


def get_windows(title: str) -> list[gw.Win32Window]:
    windows = gw.getWindowsWithTitle(title)
    return windows


def check_active_window(hwnd: int, title: str) -> None:
    windows = get_windows(title)
    for window in windows:
        if window._hWnd == hwnd:
            active = window.isActive
            return active


def get_window_size(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    height = bottom - top
    width = right - left
    return width, height


def move_mouse(hwnd, x=0, y=0):
    rect = win32gui.GetWindowRect(hwnd)
    x0, y0 = rect[2], rect[3]

    pyautogui.moveTo(x0 - x, y0 - y, 0.25)
    print(x0 - x, y0 - y)


def move_to(hwnd, x, y):
    rect = win32gui.GetWindowRect(hwnd)
    x0, y0 = rect[0], rect[1]

    target_x = x0 + x
    target_y = y0 + y

    pyautogui.moveTo(target_x, target_y, duration=0.25)
    print(target_x, target_y)