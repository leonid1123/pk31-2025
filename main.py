from tkinter import *
import pymysql.cursors


class Keyboards:
    def __init__(self, _name, _price, _id):
        self.name = _name
        self.price = _price
        self.id = _id

    def __str__(self):
        return f"Название: {self.name}, цена: {self.price}"


class App:
    def __init__(self):
        self.win = Tk()
        self.win.title("Начинаем начинать опять")
        self.win.geometry("400x300")

        # Создание и размещение элементов интерфейса
        Label(text="Название").grid(row=0, column=0)
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
        self.keyboard_view.bind("<<ListboxSelect>>", self.get_object)
        self.keyboard_view.grid(row=0, column=2, rowspan=3)

        self.del_button = Button(text="Удалить", command=self.del_keyboard)
        self.del_button.grid(row=3, column=2)

        # Подключение к базе данных
        self.cnx = pymysql.connect(
            host='localhost',
            user='pk31',
            password='1234',
            database='keyboard',
            port=3306
        )

        self.select_keyboards()
        self.win.mainloop()

    def select_keyboards(self):
        """Метод для получения записей из БД и внесения их в Listbox."""
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM keyboard")
        ans = cursor.fetchall()
        self.keyboards = [Keyboards(item[1], item[2], item[0]) for item in ans]
        self.keyboards_var.set([str(kb) for kb in self.keyboards])

    def chpun(self, event=None):
        """Метод для добавления записей в БД."""
        name = self.name_entry.get()
        price = self.price_entry.get()
        cursor = self.cnx.cursor()
        cursor.execute("INSERT INTO `keyboard`(`name`, `price`) VALUES (%s, %s)", (name, price))
        self.cnx.commit()
        cursor.close()
        self.select_keyboards()

    def del_keyboard(self):
        """Метод для удаления записей из БД."""
        cursor = self.cnx.cursor()
        selected = self.keyboard_view.curselection()
        if selected:
            keyboard_id = self.keyboards[selected[0]].id
            cursor.execute("DELETE FROM keyboard WHERE keyboard.id = %s", (keyboard_id,))
            self.cnx.commit()
            self.select_keyboards()
            self.btn.config(text="Добавить", command=self.chpun)

    def get_object(self, event):
        """Метод для заполнения полей данными выбранной записи."""
        selected = self.keyboard_view.curselection()
        if selected:
            keyboard = self.keyboards[selected[0]]
            self.name_entry.delete(0, END)
            self.price_entry.delete(0, END)
            self.name_entry.insert(0, keyboard.name)
            self.price_entry.insert(0, keyboard.price)
            self.btn.config(text="Изменить", command=lambda: self.update_selection(keyboard.id))

    def update_selection(self, keyboard_id):
        """Метод для обновления записи в БД."""
        name = self.name_entry.get()
        price = self.price_entry.get()
        cursor = self.cnx.cursor()
        cursor.execute("UPDATE keyboard SET name=%s, price=%s WHERE id=%s", (name, price, keyboard_id))
        self.cnx.commit()
        self.btn.config(text="Добавить", command=self.chpun)
        self.select_keyboards()


app = App()
