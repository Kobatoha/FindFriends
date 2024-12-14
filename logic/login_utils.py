from logic import utils
import time


title = 'Lineage II'
clients_hwnd = utils.get_window_hwnd_by_title(title)


def focus_client(client_hwnd, title):
    if not utils.check_active_window(client_hwnd, title):
        utils.get_focus_window(client_hwnd, title)
        time.sleep(2)


def click_client_options(client_hwnd):
    x, y = 40, 70
    utils.move_mouse(client_hwnd, x, y)
    time.sleep(1)
    utils.left_click()


def client_exit(client_hwnd):
    x, y = 1659, 826
    utils.move_to(client_hwnd, x, y)
    time.sleep(1)
    utils.left_click()


def client_enter(client_hwnd):
    x, y = 819, 727
    utils.move_to(client_hwnd, x, y)
    time.sleep(1)
    utils.left_click()
    utils.left_click()


def login_server(client_hwnd):
    x, y = 804, 793
    utils.move_to(client_hwnd, x, y)
    time.sleep(1)
    utils.left_click()
    utils.left_click()


def choice_character(client_hwnd):
    x, y = 869, 961
    utils.move_to(client_hwnd, x, y)
    time.sleep(1)
    utils.left_click()
    utils.left_click()


if __name__ == '__main__':
    client_hwnd = clients_hwnd[1]
    focus_client(client_hwnd, title)
    client_enter(client_hwnd)
    time.sleep(10)
    login_server(client_hwnd)
    time.sleep(10)
    choice_character(client_hwnd)
    time.sleep(10)

    click_client_options(client_hwnd)
    client_exit(client_hwnd)

    utils.get_mouse_position(client_hwnd)

    for client_hwnd in clients_hwnd:
        focus_client(client_hwnd, title)
        time.sleep(1)
        utils.move_mouse(client_hwnd, 40, 70)
