from tkinter import *
import tkinter as tk
from information import Information
from inventory import Inventory
from battle import Battle
from event import Event

class Research(Tk):
    def __init__(self):
        super().__init__()

        self.title("Lcorp Echoes")
        self.geometry("1920x1080")
        self.iconbitmap(default="LEchoes.ico")
        self.configure(bg='black')  # FF4500
        self.resizable(False, False)
        self.fsmode = True
        self.attributes('-fullscreen', True)
        self.ebutton = tk.Button(self, text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",activeforeground="Black")
        self.ebutton["command"] = self.button_clicked
        self.ebutton.pack(anchor="ne", expand=1)

        def inventory():
            inventorywindow = Inventory()

        def information():
            informationwindow = Information()

        def battle():
            battlewindow = Battle()

        def event():
            eventwindow = Event()

        self.play = tk.Button(command=inventory,text="Inventory",bg="Black",fg="#FF4500",activebackground="#FF4500",activeforeground="Black")
        self.play.pack(ipadx=26, ipady=10,anchor="s",side=LEFT)
        self.play = tk.Button(command=information,text="Information",bg="Black",fg="#FF4500",activebackground="#FF4500",activeforeground="Black")
        self.play.pack(ipadx=20, ipady=10,anchor="s",side=LEFT)
        self.play = tk.Button(command=battle,text="Battle",bg="Black",fg="#FF4500",activebackground="#FF4500",activeforeground="Black")
        self.play.pack(ipadx=20, ipady=10,anchor="s",side=LEFT)
        self.play = tk.Button(command=event,text="Event",bg="Black",fg="#FF4500",activebackground="#FF4500",activeforeground="Black")
        self.play.pack(ipadx=20, ipady=10,anchor="s",side=LEFT)

    def button_clicked(self):
        self.destroy()
