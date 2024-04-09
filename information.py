from tkinter import *
import tkinter as tk


class Information(Tk):
    def __init__(self):
        super().__init__()

        self.title("Lcorp Echoes")
        self.geometry("1920x1080")
        self.iconbitmap(default="LEchoes.ico")
        self.configure(bg='black')  # FF4500
        self.resizable(False, False)
        self.fsmode = True
        self.attributes('-fullscreen', True)
        self.ebutton = tk.Button(self, text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",
                                 activeforeground="Black")
        self.ebutton["command"] = self.button_clicked
        self.ebutton.pack(anchor="ne", expand=1)


    def button_clicked(self):
        self.destroy()