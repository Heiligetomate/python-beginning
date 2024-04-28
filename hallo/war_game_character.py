class Character:
    def __init__(self, name: str, health: int, power: int, chance_to_hit: int, ranged: bool, weapon: str, extra_strength=0, extra_health=0):
        self.extra_health = extra_health
        self.extra_strength = extra_strength
        self.name = name
        self.health = health
        self.power = power
        self.ranged = ranged
        self.chance_to_hit = chance_to_hit
        self.__is_alive = self.__check_for_alive()

    def take_damage(self, damage):
        if not self.ranged:
            self.health -= int(damage/2.5)
        self.health -= damage
        self.__is_alive = self.__check_for_alive()
        return self.health

    def __check_for_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    @property
    def is_alive(self):
        return self.__is_alive


class Player:
    def __init__(self, name, money, extra_strength=0, extra_health=0):
        self.name = name
        self.extra_health = extra_health
        self.money = money
        self.extra_strength = extra_strength

    def upgrade_health(self, health_upgrade, price):
        self.extra_health += health_upgrade
        self.money -= price

    def upgrade_damage(self, damage_upgrade, price):
        self.extra_strength += damage_upgrade
        self.money -= price


