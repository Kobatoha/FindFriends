import pygetwindow as gw
import time
from pywinauto import Desktop
import pyautogui
import win32gui
import win32con
import win32api


def get_window_hwnd_by_title(title: str) -> int:
    windows = gw.getWindowsWithTitle(title)
    windows_hwnd = []
    for window in windows:
        print(f"Window Title: {window.title}, Window ID: {window._hWnd}")
        windows_hwnd.append(window._hWnd)
    return windows_hwnd[0]


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


def move_mouse(hwnd, x, y):
    rect = win32gui.GetWindowRect(hwnd)
    x0, y0 = rect[2], rect[3]

    pyautogui.moveTo(x0 - x, y0 - y, 0.25)


if __name__ == "__main__":
    title = '4game'
    hwnd = get_window_hwnd_by_title(title)
    if not check_active_window(hwnd, title):
        get_focus_window(hwnd, title)
        time.sleep(1)
    else:
        time.sleep(1)
        move_and_click_game_button(hwnd)
