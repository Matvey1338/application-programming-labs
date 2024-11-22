from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


def application() -> None:
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Lab 5")
    window.setGeometry(500,500, 600, 600)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()