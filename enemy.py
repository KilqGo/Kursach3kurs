class Enemy:
    def __init__(self, name, health, attack, defense, behavior_patterns):
        self.name = name  # Имя врага
        self.health = health  # Здоровье врага
        self.attack = attack  # Атака врага
        self.defense = defense  # Защита врага
        self.behavior_patterns = behavior_patterns  # Паттерны поведения

    def take_damage(self, damage):
        """Уменьшает здоровье врага на величину урона, учитывая защиту."""
        effective_damage = max(0, damage - self.defense)
        self.health -= effective_damage
        return effective_damage

    def is_alive(self):
        """Проверяет, жив ли враг."""
        return self.health > 0

    def perform_behavior(self):
        """Выполняет поведение врага на основе его паттернов."""
        # Здесь можно реализовать логику выбора поведения
        # Например, случайный выбор паттерна из списка
        import random
        pattern = random.choice(self.behavior_patterns)
        return pattern.execute()

class BehaviorPattern:
    def __init__(self, name, action):
        self.name = name  # Название паттерна
        self.action = action  # Действие, которое выполняет паттерн

    def execute(self):
        """Выполняет действие паттерна."""
        # Здесь можно реализовать логику действия
        return self.action()