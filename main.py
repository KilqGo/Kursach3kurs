from tkinter import *
import tkinter as tk
from game import Research
class Main_menu:
    def __init__(self):
        #Основные атрибуты
        self.root = tk.Tk()
        self.root.geometry("1920x1080")
        self.root.title("Lcorp Echoes")
        self.root.iconbitmap(default="LEchoes.ico")
        self.root.configure(bg='black')  #FF4500
        self.root.resizable(False, False)

        self.menulogo = PhotoImage(file="./resourses/LogoMenu.png")
        self.label = tk.Label(image=self.menulogo, background='black')
        self.label.pack()

        #Полный экран
        self.fsmode=True
        self.root.attributes('-fullscreen', self.fsmode)
        def fullscreen():
            if self.fsmode==True:
                self.fsmode=False
                self.root.attributes('-fullscreen', self.fsmode)
            else:
                self.fsmode=True
                self.root.attributes('-fullscreen', self.fsmode)

        def play():
            self.root.destroy()
            researchwindow = Research()


        #Кнопки
        self.btnframe = tk.Frame(borderwidth=1, bg="#FF4500")
        self.btnframe.pack(anchor='center', padx=5, pady=5)

        self.play = tk.Button(self.btnframe, command=play, text="Play", bg="Black", fg="#FF4500", activebackground="#FF4500", activeforeground="Black")
        self.play.pack(ipadx=39, ipady=1)

        self.fullscren = tk.Button(self.btnframe, command=fullscreen, text="Fulscreen", bg="Black", fg="#FF4500", activebackground="#FF4500",activeforeground="Black")
        self.fullscren.pack(ipadx=25, ipady=1)

        self.exit = tk.Button(self.btnframe, command=lambda: self.root.destroy(), text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",activeforeground="Black")
        self.exit.pack(ipadx=41, ipady=1)

        self.root.mainloop()

app = Main_menu()