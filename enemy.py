import random

class BehaviorPattern:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def execute(self):
        return self.action()

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