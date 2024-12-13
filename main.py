import sys
from PyQt6 import QtWidgets
from ui.base_ui import BaseUI


class MainApp(BaseUI):
    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()
        self.setup_ui(self.main_window, '')

    def run(self):
        self.main_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.run()
    sys.exit(app.exec())
