class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.__is_alive = self.__check_for_alive()

    def take_damage(self, damage):
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

