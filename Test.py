import tkinter as tk
from tkinter import ttk
from basewindow import BaseWindow
from player import Player
from enemy import Enemy, BehaviorPattern
from saves import fsmod

class Battle(BaseWindow):

    def __init__(self, player, enemy):
        super().__init__()

        self.title(f"Сражение с {enemy.name}")
        self.player = player
        self.enemy = enemy

        # Полноэкранный режим
        if fsmod() == True:
            self.ebutton = tk.Button(self, text="Exit", bg="Black", fg="#FF4500", activebackground="#FF4500",
                                     activeforeground="Black")
            self.ebutton["command"] = self.ex_button_clicked
            self.ebutton.pack(anchor="ne", expand=1)

        # Создание виджетов
        self.health_label = ttk.Label(self, text=f"Здоровье {self.enemy.name}: {enemy.health}", background="#FF4500")
        self.health_label.pack(pady=10)

        self.player_health_label = ttk.Label(self, text=f"Здоровье {player.name}: {player.health}", background="#FF4500")
        self.player_health_label.pack(pady=10)

        self.experience_label = ttk.Label(self, text=f"Опыт {player.name}: {player.experience}", background="#FF4500")
        self.experience_label.pack(pady=10)

        # Счетчик для заряженной атаки
        self.charge_attack_counter_label = ttk.Label(self, text=f"Ходов до заряженной атаки: {3 - self.player.charge_counter}",
                                                     background="#FF4500")
        self.charge_attack_counter_label.pack(pady=10)

        # Метка готовности заряженной атаки
        self.charge_attack_ready_label = ttk.Label(self, text="", background="#FF4500")
        self.charge_attack_ready_label.pack(pady=10)

        # Панель для кнопок
        button_frame = tk.Frame(self, bg="#FF4500")
        button_frame.pack(anchor='s', padx=5, pady=5)

        self.action_button = tk.Button(button_frame, text="Атаковать", command=self.player_attack, bg="Black", fg="#FF4500",
                              activebackground="#FF4500", activeforeground="Black")
        self.action_button.pack(ipadx=16, ipady=10, anchor="s", side=tk.LEFT)

        self.defend_button = tk.Button(button_frame, text="Защититься", command=self.player_defend, bg="Black", fg="#FF4500",
                              activebackground="#FF4500", activeforeground="Black")
        self.defend_button.pack(ipadx=12, ipady=10, anchor="s", side=tk.LEFT)

        self.heal_button = tk.Button(button_frame, text="Лечиться", command=self.player_heal,  bg="Black", fg="#FF4500",
                              activebackground="#FF4500", activeforeground="Black")
        self.heal_button.pack(ipadx=26, ipady=10, anchor="s", side=tk.LEFT)

        self.charge_attack_button = tk.Button(button_frame, text="Заряженная атака", command=self.player_charge_attack, bg="Black", fg="#FF4500",
                              activebackground="#FF4500", activeforeground="Black", state="disabled")
        self.charge_attack_button.pack(ipadx=26, ipady=10, anchor="s", side=tk.LEFT)

        self.result_label = ttk.Label(self, text="", background="#FF4500")
        self.result_label.pack(pady=10)

        self.start_battle()

    def ex_button_clicked(self):
        self.destroy()

    def start_battle(self):
        self.enemy.reset_health()  # Восстановить здоровье врага перед началом боя

    def player_attack(self):
        self.player.charge_counter += 1  # Увеличиваем счетчик ходов
        damage = self.player.attack
        damage_taken = self.enemy.take_damage(damage)
        self.update_health_labels()

        if self.enemy.is_alive():
            enemy_action = self.enemy.perform_behavior()
            enemy_damage = self.enemy.attack
            damage_taken_by_player = self.player.take_damage(enemy_damage)
            self.update_health_labels()
            self.result_label.config(
                text=f"Вы нанесли {damage_taken} урона. {enemy_action} {self.enemy.name} нанес {damage_taken_by_player} урона.")
        else:
            self.player.experience += 1  # Увеличиваем опыт игрока
            self.result_label.config(text=f"Вы победили {self.enemy.name}! Опыт увеличен на 1.")
            self.disable_buttons()
            self.destroy()  # Закрыть окно сражения

        self.check_charge_attack_ready()
        self.check_player_alive()

    def player_charge_attack(self):
        damage = self.player.use_charge_attack()
        damage_taken = self.enemy.take_damage(damage)
        self.update_health_labels()

        if self.enemy.is_alive():
            enemy_action = self.enemy.perform_behavior()
            enemy_damage = self.enemy.attack
            damage_taken_by_player = self.player.take_damage(enemy_damage)
            self.update_health_labels()
            self.result_label.config(
                text=f"Вы использовали заряженную атаку и нанесли {damage_taken} урона. {enemy_action} {self.enemy.name} нанес {damage_taken_by_player} урона.")
        else:
            self.player.experience += 1  # Увеличиваем опыт игрока
            self.result_label.config(text=f"Вы победили {self.enemy.name}! Опыт увеличен на 1.")
            self.disable_buttons()
            self.destroy()  # Закрыть окно сражения

        self.check_charge_attack_ready()
        self.check_player_alive()

    def player_defend(self):
        self.player.charge_counter += 1  # Увеличиваем счетчик ходов
        self.player.defense += 5  # Увеличение защиты
        self.result_label.config(text=f"{self.player.name} защищается! Защита увеличена.")

        if self.enemy.is_alive():
            enemy_action = self.enemy.perform_behavior()
            enemy_damage = self.enemy.attack // 2  # Уменьшенный урон при защите
            damage_taken_by_player = self.player.take_damage(enemy_damage)
            self.update_health_labels()
            self.result_label.config(text=f"{enemy_action} {self.enemy.name} нанес {damage_taken_by_player} урона.")

        self.player.defense -= 5  # Возврат защиты к обычному значению
        self.check_charge_attack_ready()
        self.check_player_alive()

    def player_heal(self):
        self.player.charge_counter += 1  # Увеличиваем счетчик ходов
        heal_amount = 15  # Количество здоровья, восстанавливаемое при лечении
        self.player.heal(heal_amount)
        self.update_health_labels()
        self.result_label.config(text=f"{self.player.name} лечится на {heal_amount} здоровья.")

        if self.enemy.is_alive():
            enemy_action = self.enemy.perform_behavior()
            enemy_damage = self.enemy.attack
            damage_taken_by_player = self.player.take_damage(enemy_damage)
            self.update_health_labels()
            self.result_label.config(text=f"{enemy_action} {self.enemy.name} нанес {damage_taken_by_player} урона.")

        self.check_charge_attack_ready()
        self.check_player_alive()

    def update_health_labels(self):
        self.health_label.config(text=f"Здоровье {self.enemy.name}: {self.enemy.health}")
        self.player_health_label.config(text=f"Здоровье {self.player.name}: {self.player.health}")
        self.experience_label.config(text=f"Опыт {self.player.name}: {self.player.experience}")

        # Обновление счетчика и метки готовности
        if self.player.charge_counter >= 3:
            self.charge_attack_ready_label.config(text="Заряженная атака готова!")
            self.charge_attack_button.config(state="normal")  # Разблокировать кнопку заряженной атаки
        else:
            self.charge_attack_ready_label.config(text="")

    def check_charge_attack_ready(self):
        if self.player.charge_counter >= 3:
            self.charge_attack_button.config(state="normal")  # Разблокировать кнопку заряженной атаки
        else:
            self.charge_attack_button.config(state="disabled")  # Заблокировать кнопку

    def check_player_alive(self):
        if not self.player.is_alive():
            self.result_label.config(text=f"{self.player.name} проиграл!")
            self.player.experience = 0  # Обнуляем опыт
            self.player.health = self.player.base_health  # Восстанавливаем здоровье до базового
            self.disable_buttons()
            self.destroy()  # Закрыть окно сражения

    def disable_buttons(self):
        self.action_button.config(state="disabled")
        self.defend_button.config(state="disabled")
        self.heal_button.config(state="disabled")
        self.charge_attack_button.config(state="disabled")


if __name__ == "__main__":
    # Создание врага
    aggressive_pattern = BehaviorPattern("Агрессивный", lambda: "Враг атакует!")
    defensive_pattern = BehaviorPattern("Защитный", lambda: "Враг защищается!")

    enemy = Enemy("Рой фей", 100, 15, 0, [aggressive_pattern, aggressive_pattern, defensive_pattern])

    # Создание игрока
    player = Player("Мйю", 10, 1, 1, 0)

    # Запуск окна битвы
    battle_window = Battle(player, enemy)
    battle_window.mainloop()