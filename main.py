import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QDateEdit, QPushButton, QListWidget, \
    QMessageBox
from qt_material import apply_stylesheet

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Hello World')
        layout = QGridLayout()
        name_label = QLabel("ИМЯ")
        self.name_entry = QLineEdit()
        fam_label = QLabel("ФАМИЛИЯ")
        self.fam_entry = QLineEdit()
        group_label = QLabel("ГРУППА")
        self.group_entry = QLineEdit()
        kurs_label = QLabel("КУРС")
        self.kurs_entry = QLineEdit()
        date_of_birth_label = QLabel("ДАТА РОЖДЕНИЯ")
        self.date_of_birth_entry = QDateEdit()
        phone_label = QLabel("ТЕЛЕФОН")
        self.phone_entry = QLineEdit()
        add_btn = QPushButton("ДОБАВИТЬ")
        add_btn.clicked.connect(self.get_values)
        self.student_view = QListWidget()
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(self.name_entry, 0, 1)
        layout.addWidget(fam_label, 0, 2)
        layout.addWidget(self.fam_entry, 0, 3)
        layout.addWidget(group_label, 1, 0)
        layout.addWidget(self.group_entry, 1, 1)
        layout.addWidget(kurs_label, 1, 2)
        layout.addWidget(self.kurs_entry, 1, 3)
        layout.addWidget(date_of_birth_label, 2, 0)
        layout.addWidget(self.date_of_birth_entry, 2, 1)
        layout.addWidget(phone_label, 2, 2)
        layout.addWidget(self.phone_entry, 2, 3)
        layout.addWidget(add_btn, 3, 0, 1, 4)
        layout.addWidget(self.student_view, 4, 0, 1, 4)
        self.setLayout(layout)
        apply_stylesheet(app, theme='light_red.xml')
        self.show()

    def get_values(self):
        name = self.name_entry.text()
        fam = self.fam_entry.text()
        group = self.group_entry.text()
        kurs = self.kurs_entry.text()
        dr = self.date_of_birth_entry.text()
        phone = self.phone_entry.text()
        if name and fam and group and kurs and dr and phone:
            self.student_view.addItem(f"{name},{fam},{group},{kurs},{dr},{phone}")
        else:
            QMessageBox.critical(
                self,
                'Внимание ',
                'Криворукость детектед! \nНУЖНО ВСё заполнить!!!'
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
