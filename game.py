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
from rooms import Room

class Research(BaseWindow):
    def __init__(self):
        super().__init__()

        if fsmod() == True:
            self.ebutton = tk.Button(self, text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",
                                     activeforeground="Black")
            self.ebutton["command"] = self.button_clicked
            self.ebutton.pack(anchor="ne", expand=1)

        self.rooms = [
            Room("Начало", ["Верх 1", "Низ 1"]),
            Room("Верх 1", ["Верх 2"]),
            Room("Верх 2", ["Конец"]),
            Room("Низ 1", ["Низ 2"]),
            Room("Низ 2", ["Конец"]),
            Room("Конец")
        ]

        self.current_room = self.rooms[0]  # начало

        self.text_box = tk.Text(self, height=15, width=50, bg="#FF4500", fg="black", insertbackground='black', bd=2,
                                relief="solid")
        self.text_box.pack(pady=10)

        self.buttons_frame = tk.Frame(self, bg="black")
        self.buttons_frame.pack(pady=10)



        def update_text_box():
            self.text_box.delete("1.0", tk.END)  # чистка текста
            if not self.current_room.connected_rooms:
                self.text_box.insert(tk.END, "Победа! Игра окончена.")
                return

            self.text_box.insert(tk.END, f"\nВы находитесь в: {self.current_room}\n")
            self.text_box.insert(tk.END, "Выбор комнаты:\n")

        def create_room_buttons():
            for widget in self.buttons_frame.winfo_children():
                widget.destroy()  # удаление кнопок

            for room_name in self.current_room.connected_rooms:
                button = tk.Button(self.buttons_frame, text=room_name,
                                   bg="#FF4500", fg="black",
                                   bd=2, relief="solid",
                                   command=lambda name=room_name: move_to_room(name))
                button.pack(side=tk.LEFT, padx=5)

        def move_to_room(room_name):
            selected_room = next((room for room in self.rooms if room.room_text == room_name), None)

            if selected_room:
                self.current_room = selected_room
                update_text_box()
                create_room_buttons()

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
            enemy_id = 3

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

        update_text_box()
        create_room_buttons()

    def button_clicked(self):
        self.destroy()
