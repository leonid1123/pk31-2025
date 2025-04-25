import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QWidget, QVBoxLayout, QLabel


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        self.label = QLabel("Это второе окно!")
        layout.addWidget(self.label)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Открыть второе окно", self)
        self.button.setGeometry(150, 100, 150, 40)
        self.button.clicked.connect(self.open_second_window)

        self.second_window = None

    def open_second_window(self):
        if self.second_window is None:
            self.second_window = SecondWindow()
        self.second_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
