from tkinter import *
import tkinter as tk

from game import Research
from basewindow import BaseWindow
from saves import fsmodeswap


class MainMenu(BaseWindow):

    def __init__(self):
        super().__init__()

        self.menulogo = PhotoImage(file="./resourses/LogoMenu.png")
        self.label = tk.Label(image=self.menulogo, background='black')
        self.label.pack()

        def fullscreen():
            s = fsmodeswap()
            self.attributes('-fullscreen', s)


        def play():
            self.destroy()
            researchwindow = Research()


        #Кнопки
        self.btnframe = tk.Frame(borderwidth=1, bg="#FF4500")
        self.btnframe.pack(anchor='center', padx=5, pady=5)

        self.play = tk.Button(self.btnframe, command=play, text="Play", bg="Black", fg="#FF4500", activebackground="#FF4500", activeforeground="Black")
        self.play.pack(ipadx=39, ipady=1)

        self.fullscren = tk.Button(self.btnframe, command=fullscreen, text="Fulscreen", bg="Black", fg="#FF4500", activebackground="#FF4500",activeforeground="Black")
        self.fullscren.pack(ipadx=25, ipady=1)

        self.exit = tk.Button(self.btnframe, command=lambda: self.destroy(), text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",activeforeground="Black")
        self.exit.pack(ipadx=41, ipady=1)

        self.mainloop()


app = MainMenu()