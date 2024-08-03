from tkinter import *
from saves import fsmod
import tkinter as tk
from basewindow import BaseWindow

class Battle(BaseWindow):
    def __init__(self):
        super().__init__()

        if fsmod() == True:
            self.ebutton = tk.Button(self, text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",
                                     activeforeground="Black")
            self.ebutton["command"] = self.button_clicked
            self.ebutton.pack(anchor="ne", expand=1)
        else:
            None

        def attack():
            None

        def charge():
            None

        def defence():
            None

        def heal():
            None

        canvas = Canvas(bg="black", width=300, height=200)
        canvas.pack(anchor=CENTER, expand=1)

        self.btnframe = tk.Frame(borderwidth=1, bg="#FF4500")
        self.btnframe.pack(anchor='s', padx=5, pady=5)

        self.play = tk.Button(self.btnframe, command=attack, text="Attack", bg="Black", fg="#FF4500",
                              activebackground="#FF4500", activeforeground="Black")
        self.play.pack(ipadx=16, ipady=10, anchor="s", side=LEFT)

        self.play = tk.Button(self.btnframe, command=charge, text="Charge attack", bg="Black", fg="#FF4500",
                              activebackground="#FF4500", activeforeground="Black")
        self.play.pack(ipadx=12, ipady=10, anchor="s", side=LEFT)

        self.play = tk.Button(self.btnframe, command=defence, text="Defence", bg="Black", fg="#FF4500",
                              activebackground="#FF4500", activeforeground="Black")
        self.play.pack(ipadx=26, ipady=10, anchor="s", side=LEFT)

        self.play = tk.Button(self.btnframe, command=heal, text="Heal", bg="Black", fg="#FF4500",
                              activebackground="#FF4500", activeforeground="Black")
        self.play.pack(ipadx=26, ipady=10, anchor="s", side=LEFT)

    def button_clicked(self):
        self.destroy()