import pygetwindow as gw
import time
from pywinauto import Desktop
import pyautogui
import win32gui
import win32con
import win32api
from logic import utils


title = '4game'
hwnd = utils.get_window_hwnd_by_title(title)


def move_and_click_game_button(hwnd):
    x = 140
    y = 840
    utils.move_mouse(hwnd, x, y)
    pyautogui.leftClick()


def focus_launcher(hwnd, title):
    if not utils.check_active_window(hwnd, title):
        utils.get_focus_window(hwnd, title)
        time.sleep(1)


