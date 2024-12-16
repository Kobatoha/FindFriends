import time
from logic import utils


title = '4game'
launcher_hwnd = utils.get_window_hwnd_by_title(title)[0]


def click_game_button(launcher_hwnd):
    x = 140
    y = 840
    utils.move_mouse(launcher_hwnd, x, y)
    utils.left_click()


def focus_launcher(launcher_hwnd, title):
    if not utils.check_active_window(launcher_hwnd, title):
        utils.get_focus_window(launcher_hwnd, title)
        time.sleep(1)


def click_profile(launcher_hwnd):
    x, y = 1079, 46
    utils.move_to(launcher_hwnd, x, y)
    time.sleep(1)
    utils.left_click()


def logout(launcher_hwnd):
    x, y = 174, 755
    utils.move_to(launcher_hwnd, x, y)
    time.sleep(1)
    utils.left_click()


def click_short_login_text_edit(launcher_hwnd):
    x, y = 449, 128
    utils.move_to(launcher_hwnd, x, y)
    time.sleep(1)
    utils.left_click()


def click_long_login_text_edit(launcher_hwnd):
    x, y = 750, 128
    utils.move_to(launcher_hwnd, x, y)
    time.sleep(1)
    utils.left_click()


def choice_short_account(launcher_hwnd, num=1):
    accounts = {
        1: {'x': 470, 'y': 185},
        2: {'x': 445, 'y': 242},
        3: {'x': 434, 'y': 296},
        4: {'x': 431, 'y': 343},
    }
    utils.move_to(launcher_hwnd, accounts[num]['x'], accounts[num]['y'])
    time.sleep(1)
    utils.left_click()


def choice_long_account(launcher_hwnd, num=1):
    accounts = {
        1: {'x': 750, 'y': 179},
        2: {'x': 750, 'y': 243},
        3: {'x': 750, 'y': 287},
        4: {'x': 750, 'y': 345},
    }
    utils.move_to(launcher_hwnd, accounts[num]['x'], accounts[num]['y'])
    time.sleep(1)
    utils.left_click()


if __name__ == '__main__':
    title = '4game'
    launcher_hwnd = utils.get_window_hwnd_by_title(title)[0]
    focus_launcher(launcher_hwnd, title)
    click_long_login_text_edit(launcher_hwnd)
    choice_long_account(launcher_hwnd, num=4)
    click_game_button(launcher_hwnd)
    click_profile(launcher_hwnd)
    logout(launcher_hwnd)
    # click_game_button(launcher_hwnd)
    # utils.get_mouse_position(launcher_hwnd)