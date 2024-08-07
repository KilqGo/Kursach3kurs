from tkinter import *
import tkinter as tk
from saves import fsmod
from basewindow import BaseWindow
from information import Information
from inventory import Inventory
from battle import Battle
from event import Event


class Research(BaseWindow):
    def __init__(self):
        super().__init__()

        if fsmod() == True:
            self.ebutton = tk.Button(self, text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",
                                     activeforeground="Black")
            self.ebutton["command"] = self.button_clicked
            self.ebutton.pack(anchor="ne", expand=1)
        else:
            None


        def inventory():
            inventorywindow = Inventory()

        def information():
            informationwindow = Information()

        def battle():
            self.destroy()
            battlewindow = Battle()

        def event():
            eventwindow = Event()

        canvas = Canvas(bg="black", width=300, height=200)
        canvas.pack(anchor=CENTER, expand=1)

        self.btnframe = tk.Frame(borderwidth=1, bg="#FF4500")
        self.btnframe.pack(anchor='s', padx=5, pady=5)

        self.play = tk.Button(self.btnframe,command=inventory,text="Inventory",bg="Black",fg="#FF4500",activebackground="#FF4500",activeforeground="Black")
        self.play.pack(ipadx=16, ipady=10,anchor="s",side=LEFT)

        self.play = tk.Button(self.btnframe,command=information,text="Information",bg="Black",fg="#FF4500",activebackground="#FF4500",activeforeground="Black")
        self.play.pack(ipadx=12, ipady=10,anchor="s",side=LEFT)

        self.play = tk.Button(self.btnframe,command=battle,text="Battle",bg="Black",fg="#FF4500",activebackground="#FF4500",activeforeground="Black")
        self.play.pack(ipadx=26, ipady=10,anchor="s",side=LEFT)

        self.play = tk.Button(self.btnframe,command=event,text="Event",bg="Black",fg="#FF4500",activebackground="#FF4500",activeforeground="Black")
        self.play.pack(ipadx=26, ipady=10,anchor="s",side=LEFT)

    def button_clicked(self):
        self.destroy()
