import tkinter as tk
from tkinter import ttk

from player import Player
from enemy import Enemy, BehaviorPattern


class BattleWindow(tk.Tk):
    def __init__(self, player, enemy):
        super().__init__()
        self.title(f"Сражение с {enemy.name}")
        self.player = player
        self.enemy = enemy

        # Устанавливаем размер окна
        self.geometry("800x600")

        # Создание виджетов
        self.health_label = ttk.Label(self, text=f"Здоровье врага: {enemy.health}")
        self.health_label.pack(pady=10)

        self.player_health_label = ttk.Label(self, text=f"Здоровье {player.name}: {player.health}")
        self.player_health_label.pack(pady=10)

        self.experience_label = ttk.Label(self, text=f"Опыт {player.name}: {player.experience}")
        self.experience_label.pack(pady=10)

        # Счетчик для усиленной атаки
        self.power_attack_counter_label = ttk.Label(self,
                                                    text=f"Ходов до усиленной атаки: {3 - self.player.charge_counter}")
        self.power_attack_counter_label.pack(pady=10)

        # Метка готовности усиленной атаки
        self.power_attack_ready_label = ttk.Label(self, text="")
        self.power_attack_ready_label.pack(pady=10)

        # Панель для кнопок
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        self.action_button = ttk.Button(button_frame, text="Атаковать", command=self.player_attack)
        self.action_button.pack(side=tk.LEFT, padx=5)

        self.defend_button = ttk.Button(button_frame, text="Защититься", command=self.player_defend)
        self.defend_button.pack(side=tk.LEFT, padx=5)

        self.heal_button = ttk.Button(button_frame, text="Лечиться", command=self.player_heal)
        self.heal_button.pack(side=tk.LEFT, padx=5)

        self.power_attack_button = ttk.Button(button_frame, text="Усиленная атака", command=self.player_power_attack,
                                              state="disabled")
        self.power_attack_button.pack(side=tk.LEFT, padx=5)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

        self.start_battle()

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
                text=f"Вы нанесли {damage_taken} урона. {enemy_action} Враг нанес {damage_taken_by_player} урона.")
        else:
            self.player.experience += 1  # Увеличиваем опыт игрока
            self.result_label.config(text=f"Вы победили {self.enemy.name}! Опыт увеличен на 1.")
            self.disable_buttons()
            self.destroy()  # Закрыть окно сражения

        self.check_power_attack_ready()
        self.check_player_alive()

    def player_power_attack(self):
        damage = self.player.use_power_attack()
        damage_taken = self.enemy.take_damage(damage)
        self.update_health_labels()

        if self.enemy.is_alive():
            enemy_action = self.enemy.perform_behavior()
            enemy_damage = self.enemy.attack
            damage_taken_by_player = self.player.take_damage(enemy_damage)
            self.update_health_labels()
            self.result_label.config(
                text=f"Вы использовали усиленную атаку и нанесли {damage_taken} урона. {enemy_action} Враг нанес {damage_taken_by_player} урона.")
        else:
            self.player.experience += 1  # Увеличиваем опыт игрока
            self.result_label.config(text=f"Вы победили {self.enemy.name}! Опыт увеличен на 1.")
            self.disable_buttons()
            self.destroy()  # Закрыть окно сражения

        self.check_power_attack_ready()
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
            self.result_label.config(text=f"{enemy_action} Враг нанес {damage_taken_by_player} урона.")

        self.player.defense -= 5  # Возврат защиты к обычному значению
        self.check_power_attack_ready()
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
            self.result_label.config(text=f"{enemy_action} Враг нанес {damage_taken_by_player} урона.")

        self.check_power_attack_ready()
        self.check_player_alive()

    def update_health_labels(self):
        self.health_label.config(text=f"Здоровье врага: {self.enemy.health}")
        self.player_health_label.config(text=f"Здоровье {self.player.name}: {self.player.health}")
        self.experience_label.config(text=f"Опыт {self.player.name}: {self.player.experience}")

        # Обновление счетчика и метки готовности
        if self.player.charge_counter >= 3:
            self.power_attack_ready_label.config(text="Заряженная атака готова!")
            self.power_attack_button.config(state="normal")  # Разблокировать кнопку усиленной атаки
        else:
            self.power_attack_ready_label.config(text="")

    def check_power_attack_ready(self):
        if self.player.charge_counter >= 3:
            self.power_attack_button.config(state="normal")  # Разблокировать кнопку усиленной атаки
        else:
            self.power_attack_button.config(state="disabled")  # Заблокировать кнопку

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
        self.power_attack_button.config(state="disabled")


if __name__ == "__main__":
    # Создание врага
    aggressive_pattern = BehaviorPattern("Агрессивный", lambda: "Враг атакует!")
    defensive_pattern = BehaviorPattern("Защитный", lambda: "Враг защищается!")

    enemy = Enemy("Враг1", 100, 15, 5, [aggressive_pattern, aggressive_pattern, defensive_pattern])

    # Создание игрока
    player = Player("Мйю", 100, 10, 5, 0)

    # Запуск окна битвы
    battle_window = BattleWindow(player, enemy)
    battle_window.mainloop()