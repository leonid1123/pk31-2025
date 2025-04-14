import toga
from toga.style.pack import ROW, COLUMN, Pack


class App(toga.App):
    def startup(self) -> None:
        my_style = Pack(padding=5, flex=1, font_family='Helvetica', font_size=16)
        self.main_window = toga.MainWindow()
        main_box = toga.Box()
        main_box.style.update(direction=COLUMN)
        self.entry = toga.TextInput(style=my_style)
        self.view = toga.MultilineTextInput(style=my_style)
        self.btn = toga.Button("Добавить", on_press=self.add_text, style=my_style)
        main_box.add(self.entry)
        main_box.add(self.view)
        main_box.add(self.btn)
        self.main_window.content = main_box
        self.main_window.show()

    def add_text(self, widget):
        txt = self.entry.value
        self.view.value += (txt + "\n")
        self.entry.value = ""


app = App("Multiline", "multiline.app")
app.main_loop()