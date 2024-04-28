class Weapons:
    def __init__(self, name: str, damage: int, distance: bool):
        self.name = name
        self.damage = damage
        self.distance = distance


sword = Weapons('Sword', 12, False)
bow = Weapons('Bow', 10, True)


