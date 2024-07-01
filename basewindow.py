from tkinter import *
from saves import fsmod


class BaseWindow(Tk):
    def __init__(self):

        super().__init__()
        self.init(self)

    def init(self, win):
        win.title("Lcorp Echoes")
        win.geometry("800x600")
        win.iconbitmap(default="./resourses/LEchoes.ico")
        win.configure(bg='black')  #FF4500
        win.resizable(False, False)
        win.attributes('-fullscreen', fsmod())
