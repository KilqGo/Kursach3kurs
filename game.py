from tkinter import *
import tkinter as tk
from saves import fsmod
from basewindow import BaseWindow
from information import Information
from inventory import Inventory
from player import Player
from enemy import Enemy, BehaviorPattern
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
            # Создание врага
            aggressive_pattern = BehaviorPattern("Агрессивный", lambda: "Враг атакует!")
            defensive_pattern = BehaviorPattern("Защитный", lambda: "Враг защищается!")
            enemy = Enemy("Рой фей", 100, 15, 0, [aggressive_pattern])
            # Создание игрока
            player = Player("Мйю", 10, 1, 1, 0)
            # ТУТ ПОКАЧТО ВВОД ID ВРАГА ПОКА НЕ СДЕЛАЮ НОРМАЛЬНО КРАТУ-------------------------------------------------=
            enemy_id = 2

            if enemy_id == 1:
                enemy = Enemy("Рой фей", 100, 15, 0, [aggressive_pattern, aggressive_pattern, defensive_pattern])
            elif enemy_id == 2:
                enemy = Enemy("ЗНН", 150, 20, 0, [aggressive_pattern, defensive_pattern])
            else:
                enemy = Enemy("Ошибка", 30, 10, 0, [aggressive_pattern])
            # Запуск окна битвы

            battle_window = Battle(player, enemy)
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
