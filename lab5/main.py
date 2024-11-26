from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import sys
from main_windows_ui import Ui_MainWindow
from iterator import ImgIterator


class Imagewindow(QtWidgets.QMainWindow):
    def __init__(self, csv_file):
        super(Imagewindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.show_next_image)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10, 10, 780, 500)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)

        # Итератор для работы с CSV
        self.image_iterator = iter(ImgIterator(csv_file))
        self.current_image = None

        self.history = []
        self.show_next_image()

    def show_next_image(self):
        """
        Отображает следующую фотографию из CSV.
        """
        try:
            # Получаем следующий путь к изображению
            image_path = next(self.image_iterator)[1]
            self.history.append(image_path)
            self.display_image(image_path)
        except StopIteration:
            self.label.setText("No more images.")

    def display_image(self, image_path):
        """
        Загружает и отображает изображение по указанному пути.
        """
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.label.setPixmap(pixmap)
        else:
            self.label.setText("Image not found.")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())
