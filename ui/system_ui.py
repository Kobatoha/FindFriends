from PyQt6 import QtWidgets
from resources.css import start_button_css, stop_button_css


class SystemUI:
    def __init__(self):
        self.start_button = None

    def add_system_buttons(self, parent):
        self.start_button = QtWidgets.QPushButton(parent)
        self.start_button.setText("Start")
        self.start_button.setGeometry(10, 10, 70, 30)
        self.start_button.setStyleSheet(stop_button_css)
