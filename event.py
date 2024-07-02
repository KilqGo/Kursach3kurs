from tkinter import *
from saves import fsmod
import tkinter as tk
from basewindow import BaseWindow

class Event(BaseWindow):
    def __init__(self):
        super().__init__()

        if fsmod() == True:
            self.ebutton = tk.Button(self, text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",
                                     activeforeground="Black")
            self.ebutton["command"] = self.button_clicked
            self.ebutton.pack(anchor="ne", expand=1)
        else:
            None

    def button_clicked(self):
        self.destroy()