class Player:

    def __init__(self, fortitude, prudence, temperance, justice, experience):
        self.name = "Мйю"
        self.base_health = fortitude*10  # Базовое здоровье
        self.health = fortitude*10  # Текущее здоровье
        self.base_health = prudence * 10  # Базовое здравомыслие
        self.health = prudence * 10  # Текущее здравомыслие
        self.defense = temperance * 5
        self.attack = justice * 5
        self.rdef = 100
        self.wdef = 100
        self.bdef = 100
        self.pdef = 100
        self.charge_counter = 0  # Счетчик ходов для усиленной атаки
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
        if self.charge_counter >= 3:
            self.charge_counter = 0
            return self.attack * 3  # Увеличенный урон
        else:
            return self.attack  # Обычный урон
