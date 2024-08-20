from saves import fsmod
import tkinter as tk
from tkinter import ttk
from basewindow import BaseWindow

options = ["Вариант 1", "Вариант 2", "Вариант 3", "Вариант 4", "Вариант 5",
           "Вариант 6", "Вариант 7", "Вариант 8", "Вариант 9", "Вариант 10"]

info = {
    "Вариант 1": "Информация о варианте 1",
    "Вариант 2": "Информация о варианте 2",
    "Вариант 3": "Информация о варианте 3",
    "Вариант 4": "Информация о варианте 4",
    "Вариант 5": "Информация о варианте 5",
    "Вариант 6": "Информация о варианте 6",
    "Вариант 7": "Информация о варианте 7",
    "Вариант 8": "Информация о варианте 8",
    "Вариант 9": "Информация о варианте 9",
    "Вариант 10": "Информация о варианте 10"
}

class Information(BaseWindow):
    def __init__(self):
        super().__init__()

        if fsmod():
            self.ebutton = tk.Button(self, text="Exit", bg="Black", fg="#FF4500",
                                     activebackground="#FF4500", activeforeground="Black",
                                     command=self.button_clicked)
            self.ebutton.grid(row=0, column=1, padx=10, pady=10, sticky="ne")  # Кнопка справа

        self.combobox = ttk.Combobox(self, values=options, state="readonly")
        self.combobox.grid(row=0, column=0, padx=10, pady=10, sticky="nw")  # Список слева
        self.combobox.bind("<<ComboboxSelected>>", self.update_info)

        self.info_label = tk.Label(self, text="Выберите вариант из списка", wraplength=400)
        self.info_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # Метка под списком

    def update_info(self, *args):
        selected_option = self.combobox.get()
        self.info_label.config(text=info[selected_option])

    def button_clicked(self):
        self.destroy()