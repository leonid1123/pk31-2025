import pymysql
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QListWidget, QLineEdit, QPushButton
from PyQt6.QtCore import QTimer


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_connect()
        self.setWindowTitle('Болталка')
        layout = QGridLayout()
        self.setLayout(layout)
        self.msg_view = QListWidget()
        self.msg_entry = QLineEdit()
        send_msg_btn = QPushButton("Отправить")
        send_msg_btn.clicked.connect(self.send_message)

        layout.addWidget(self.msg_view, 0, 0, 1, 2)
        layout.addWidget(self.msg_entry, 1, 0)
        layout.addWidget(send_msg_btn, 1, 1)

        self.get_all_msg()
        self.show()

    def send_message(self):
        self.cursor = self.cnx.cursor()
        with self.cursor:
            sql = """INSERT INTO messages(text) VALUES (%s)"""
            params = (self.msg_entry.text(),)
            self.cursor.execute(sql, params)
            self.cnx.commit()
        self.msg_entry.clear()

    def get_all_msg(self):
        sql = """SELECT * FROM messages"""
        self.cursor = self.cnx.cursor()
        with self.cursor:
            self.cursor.execute(sql)
            self.cnx.commit()
            ans = self.cursor.fetchall()
        self.msg_view.clear()
        for item in ans:
            self.msg_view.addItem(item['text'])
        self.msg_view.scrollToBottom()
        QTimer.singleShot(2000, self.get_all_msg)

    def db_connect(self):
        # Connect to the database
        self.cnx = pymysql.connect(host='192.168.1.61',
                                   user='messenger',
                                   password='1234',
                                   database='pk31_msg',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.cnx.cursor()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
