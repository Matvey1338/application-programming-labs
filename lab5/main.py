from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import os
import sys
from main_windows_ui import Ui_MainWindow
from iterator import ImgIterator


class Imagewindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Imagewindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_csv.clicked.connect(self.choose_csv)
        self.ui.btn_csv_2.clicked.connect(self.choose_csv)
        self.ui.btn_right.clicked.connect(self.show_next_image)
        self.ui.btn_left.clicked.connect(self.show_previous_image)
        
        # Переменные для итерации
        self.image_iterator = None
        self.history = []

    def choose_csv(self) -> None:
        """
        Opens a file dialog to choose a CSV file, initializes the image iterator,
        switches to the display widget, and skips the first row of the CSV file.
        """
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Annotation File", "", "CSV Files (*.csv)")
        if file_path:
            self.image_iterator = iter(ImgIterator(file_path))
            self.ui.stackedWidget.setCurrentIndex(1)
            self.history = []  # Очистить историю
            self.skip_csv_intro()

    def skip_csv_intro(self) -> None:
        """
        Skips the first row of the CSV file and displays the first image.
        """
        next(self.image_iterator, None)
        self.show_next_image()

    def show_next_image(self) -> None:
        """
        Displays the next image from the CSV file. If no more images are available,
        displays a message in the label.
        """
        try:
            # Получаем следующий путь к изображению
            image_path = next(self.image_iterator)[1]
            self.history.append(image_path)
            self.display_image(image_path)
        except StopIteration:
            self.ui.label.setText("No more images.")
            self.history.append("decoy")
            self.ui.btn_right.setEnabled(False)

    def show_previous_image(self) -> None:
        """
        Displays the previous image if there is one in the history.
        If no previous images exist, does nothing.
        """
        if len(self.history) > 1:
            # Enable the 'Next' button if it was disabled
            self.history.pop()  # Убираем текущую
            image_path = self.history[-1]
            self.display_image(image_path)

            self.ui.btn_right.setEnabled(True)
            self.reset_iterator_to_current()
        else:
            pass

    def reset_iterator_to_current(self) -> None:
        """
        Resets the image iterator to start from the current position in the history.
        """
        if self.image_iterator:
            # Recreate the iterator and skip to the current position in history
            current_position = len(self.history)
            self.image_iterator = iter(ImgIterator(self.image_iterator.csv_file))
            for _ in range(current_position + 1):
                next(self.image_iterator)

    def display_image(self, image_path: str) -> None:
        """
        Loads and displays an image in the QLabel.

        Args:
            image_path (str): The absolute path to the image file.
        """
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.ui.label.setPixmap(pixmap)
        else:
            self.ui.label.setText("Image not found.")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    image = Imagewindow()
    image.show()
    sys.exit(app.exec_())
