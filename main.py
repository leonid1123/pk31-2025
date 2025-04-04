from tkinter import *
import pymysql.cursors


class App:
    def __init__(self):
        self.win = Tk()
        self.win.title("Начинаем начинать опять")
        self.win.geometry("400x300")
        name_label = Label(text="Название")
        name_label.grid(row=0, column=0)
        Label(text="Цена").grid(row=1, column=0)
        self.name_entry = Entry()
        self.price_entry = Entry()
        self.name_entry.grid(row=0, column=1)
        self.price_entry.grid(row=1, column=1)
        self.btn = Button(text="Добавить", command=self.chpun)
        self.btn.grid(row=2, column=0, columnspan=2)

        self.keyboards = []
        self.keyboards_var = Variable(value=self.keyboards)
        self.keyboard_view = Listbox(listvariable=self.keyboards_var, width=50)
        self.keyboard_view.grid(row=0, column=2, rowspan=3)
        self.del_button = Button(text="УДОЛИ!!!!", command=self.del_keyboard)
        self.del_button.grid(row=3,column=2)
        self.cnx = pymysql.connect(host='localhost',
                                   user='pk31',
                                   password='1234',
                                   database='keyboard')
        self.select_keyboards()
        self.win.mainloop()

    def select_keyboards(self):
        cursor = self.cnx.cursor()
        sel_str = "SELECT * FROM keyboard"
        cursor.execute(sel_str)
        ans = cursor.fetchall()
        self.keyboards = []
        for item in ans:
            tmp = f"Название:{item[1]}, цена:{item[2]}"
            self.keyboards.append(tmp)
        self.keyboards_var.set(self.keyboards)

    def chpun(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        cursor = self.cnx.cursor()
        sql_str = "INSERT INTO `keyboard`(`name`, `price`) VALUES (%s,%s);"
        params = (name, price)
        cursor.execute(sql_str, params)
        self.cnx.commit()
        cursor.close()
        self.select_keyboards()

    def del_keyboard(self):
        #DELETE FROM `keyboard` WHERE `keyboard`.`id` = 6
        cursor = self.cnx.cursor()
        del_str="DELETE FROM `keyboard` WHERE `keyboard`.`id` = %s"
        print(self.keyboard_view.curselection())



app = App()

