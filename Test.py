import tkinter as tk
from tkinter import ttk
import random

class Enemy:
    def __init__(self, name, base_health, attack, defense, behavior_patterns):
        self.name = name
        self.base_health = base_health  # Базовое здоровье
        self.health = base_health  # Текущее здоровье
        self.attack = attack
        self.defense = defense
        self.behavior_patterns = behavior_patterns

    def take_damage(self, damage):
        effective_damage = max(0, damage - self.defense)
        self.health -= effective_damage
        return effective_damage

    def is_alive(self):
        return self.health > 0

    def perform_behavior(self):
        pattern = random.choice(self.behavior_patterns)
        return pattern.execute()

    def reset_health(self):
        """Сбросить текущее здоровье до базового значения."""
        self.health = self.base_health

class BehaviorPattern:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def execute(self):
        return self.action()

class Player:
    def __init__(self, name, base_health, attack, defense, experience):
        self.name = name
        self.base_health = base_health  # Базовое здоровье
        self.health = base_health  # Текущее здоровье
        self.attack = attack
        self.defense = defense
        self.turn_counter = 0  # Счетчик ходов для усиленной атаки
        self.experience = experience  # Счетчик опыта

    def take_damage(self, damage):
        effective_damage = max(0, damage - self.defense)
        self.health -= effective_damage
        return effective_damage

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        if self.health + amount > self.base_health:
            self.health = self.base_health  # Восстанавливаем до максимального здоровья
        else:
            self.health += amount

    def use_power_attack(self):
        if self.turn_counter >= 3:
            self.turn_counter = 0
            return self.attack * 2  # Увеличенный урон
        else:
            return self.attack  # Обычный урон

class BattleWindow(tk.Toplevel):
    def __init__(self, master, player, enemy):
        super().__init__(master)
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
        self.power_attack_counter_label = ttk.Label(self, text=f"Ходов до усиленной атаки: {3 - self.player.turn_counter}")
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

        self.power_attack_button = ttk.Button(button_frame, text="Усиленная атака", command=self.player_power_attack, state="disabled")
        self.power_attack_button.pack(side=tk.LEFT, padx=5)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

    def player_attack(self):
        self.player.turn_counter += 1  # Увеличиваем счетчик ходов
        damage = self.player.attack
        damage_taken = self.enemy.take_damage(damage)
        self.update_health_labels()

        if self.enemy.is_alive():
            enemy_action = self.enemy.perform_behavior()
            enemy_damage = self.enemy.attack
            damage_taken_by_player = self.player.take_damage(enemy_damage)
            self.update_health_labels()
            self.result_label.config(text=f"Вы нанесли {damage_taken} урона. {enemy_action} Враг нанес {damage_taken_by_player} урона.")
        else:
            self.player.experience += 1  # Увеличиваем опыт игрока
            self.result_label.config(text=f"Вы победили {self.enemy.name}! Опыт увеличен на 1.")
            self.disable_buttons()
            self.master.show_start_button()  # Показать кнопку для начала новой игры
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
            self.result_label.config(text=f"Вы использовали усиленную атаку и нанесли {damage_taken} урона. {enemy_action} Враг нанес {damage_taken_by_player} урона.")
        else:
            self.player.experience += 1  # Увеличиваем опыт игрока
            self.result_label.config(text=f"Вы победили {self.enemy.name}! Опыт увеличен на 1.")
            self.disable_buttons()
            self.master.show_start_button()  # Показать кнопку для начала новой игры
            self.destroy()  # Закрыть окно сражения

        self.check_power_attack_ready()
        self.check_player_alive()

    def player_defend(self):
        self.player.turn_counter += 1  # Увеличиваем счетчик ходов
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
        self.player.turn_counter += 1  # Увеличиваем счетчик ходов
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
        if self.player.turn_counter >= 3:
            self.power_attack_ready_label.config(text="Заряженная атака готова!")
            self.power_attack_button.config(state="normal")  # Разблокировать кнопку усиленной атаки
        else:
            self.power_attack_ready_label.config(text="")

    def check_power_attack_ready(self):
        if self.player.turn_counter >= 3:
            self.power_attack_button.config(state="normal")  # Разблокировать кнопку усиленной атаки
        else:
            self.power_attack_button.config(state="disabled")  # Заблокировать кнопку

    def check_player_alive(self):
        if not self.player.is_alive():
            self.result_label.config(text=f"{self.player.name} проиграл!")
            self.player.experience = 0  # Обнуляем опыт
            self.player.health = self.player.base_health  # Восстанавливаем здоровье до базового
            self.disable_buttons()
            self.master.show_start_button()  # Показать кнопку для начала новой игры
            self.destroy()  # Закрыть окно сражения

    def disable_buttons(self):
        self.action_button.config(state="disabled")
        self.defend_button.config(state="disabled")
        self.heal_button.config(state="disabled")
        self.power_attack_button.config(state="disabled")

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Игра")

        # Создание первого врага
        aggressive_pattern = BehaviorPattern("Агрессивный", lambda: "Враг атакует!")
        defensive_pattern = BehaviorPattern("Защитный", lambda: "Враг защищается!")
        self.enemy1 = Enemy(
            name="Враг1",
            base_health=100,
            attack=15,
            defense=5,
            behavior_patterns=[aggressive_pattern,aggressive_pattern, defensive_pattern]
        )

        # Создание второго врага
        self.enemy2 = Enemy(
            name="Враг2",
            base_health=80,
            attack=12,
            defense=3,
            behavior_patterns=[aggressive_pattern, defensive_pattern, defensive_pattern]
        )

        # Создание игрока
        self.player = Player(
            name="Мйю",
            base_health=100,  # Базовое здоровье
            attack=10,
            defense=5,
            experience=0  # Начальное значение опыта
        )

        # Кнопки для начала сражения
        self.battle_button1 = ttk.Button(self, text="Сразиться с 1", command=lambda: self.start_battle(self.enemy1))
        self.battle_button1.pack(pady=10)

        self.battle_button2 = ttk.Button(self, text="Сразиться с 2", command=lambda: self.start_battle(self.enemy2))
        self.battle_button2.pack(pady=10)

        # Метка для отображения опыта игрока
        self.experience_label = ttk.Label(self, text=f"Опыт {self.player.name}: {self.player.experience}")
        self.experience_label.pack(pady=10)

    def start_battle(self, enemy):
        enemy.reset_health()  # Восстановить здоровье врага перед началом боя
        self.battle_window = BattleWindow(self, self.player, enemy)
        self.battle_window.grab_set()

    def show_start_button(self):
        self.battle_button1.config(state="normal")  # Включить кнопку "Сразиться с 1"
        self.battle_button2.config(state="normal")  # Включить кнопку "Сразиться с 2"
        self.experience_label.config(text=f"Опыт {self.player.name}: {self.player.experience}")  # Обновить метку опыта

if __name__ == "__main__":
    game_window = GameWindow()
    game_window.mainloop()
