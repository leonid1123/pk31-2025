import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Hello World')
        layout = QGridLayout()
        name_label = QLabel("ИМЯ")
        name_entry = QLineEdit()
        layout.addWidget(name_label,0,0)
        layout.addWidget(name_entry,0,1)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
