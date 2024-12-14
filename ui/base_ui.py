from PyQt6 import QtWidgets, QtGui
from resources.css import base_css


class BaseUI:
    def __init__(self):
        self.main_widget = None

    def setup_ui(self, main_window, main_icon):
        main_window.setObjectName('main_window')
        main_window.setWindowTitle('FindFriend')
        main_window.setWindowIcon(QtGui.QIcon(main_icon))
        main_window.resize(300, 300)
        main_window.setStyleSheet(base_css)

        self.main_widget = QtWidgets.QWidget(main_window)
        self.main_widget.setObjectName('main_widget')
        self.main_widget.resize(300, 300)
