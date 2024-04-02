from tkinter import *
from tkinter import ttk
import tkinter as tk

class Main_menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1280x720+325+130")
        self.root.title("Lcorp Echoes")
        self.root.iconbitmap(default="LEchoes.ico")
        self.root.configure(bg='black')  #FF4500
        self.root.resizable(False, False)

        self.MenuLogo = PhotoImage(file="./resourses/LogoMenu.png")
        self.label = tk.Label(image=self.MenuLogo, background='black')
        self.label.pack()

        self.FsMode=False
        def Fullscreen():
            if(self.FsMode==False):
                self.FsMode=True
                self.root.attributes('-fullscreen', self.FsMode)
            else:
                self.FsMode=False
                self.root.attributes('-fullscreen', self.FsMode)

        self.Btnframe = tk.Frame(borderwidth=1, bg="#FF4500")
        self.Btnframe.pack(anchor='center', padx=5, pady=5)

        self.Play = tk.Button(self.Btnframe, text="Play", bg="Black", fg="#FF4500")
        self.Play.pack(ipadx=39, ipady=1)

        self.Fullscren = tk.Button(self.Btnframe, command=Fullscreen, text="Fulscreen", bg="Black", fg="#FF4500")
        self.Fullscren.pack(ipadx=25, ipady=1)

        self.Exit = tk.Button(self.Btnframe, command=lambda: self.root.destroy(), text="Exit", bg="Black", fg="#FF4500")
        self.Exit.pack(ipadx=41, ipady=1)

        self.root.mainloop()

app = Main_menu()