import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QTableWidget, QMessageBox
import pymysql.cursors


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(QSize(600,400))
        self.table_fields = []
        self.setWindowTitle('Студенты')
        layout = QGridLayout()
        self.setLayout(layout)
        self.students_view = QTableWidget()
        layout.addWidget(self.students_view)
        self.students_view.setColumnCount(3)
        labels=["one","two","three"]
        self.students_view.setHorizontalHeaderLabels(labels)
        self.db_connect()
        self.get_db_info()
        self.show()

    def db_connect(self):
        """метод для подключения к БД и создания курсора"""
        try:
            self.cnx = pymysql.connect(host="localhost",
                                       user="pk31",
                                       password="1234",
                                       database="students",
                                       cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.cnx.cursor()
        except pymysql.Error as e:
            QMessageBox.critical(self,
                                 "Ошибка БД",
                                 f"Ошибка:{e}")
            self.cnx = None
            self.cur = None

    def get_db_info(self):
        """метод для получения информации о таблице студенты"""
        sql = 'SHOW COLUMNS FROM students'
        if self.cnx:
            self.cur.execute(sql)
            ans = self.cur.fetchall()
            for item in ans:
                self.table_fields.append(item['Field'])


    def setTable(self):
        """метод для настройки таблицы"""
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

