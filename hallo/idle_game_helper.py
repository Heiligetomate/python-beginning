worker = 5
money = 0


class Achievement:
    achievements = []

    def __init__(self, requirement, number, which_achievement, dollar, price):
        self.requirement = requirement
        self.number = number
        self.which_achievement = which_achievement
        self.money = dollar
        self.price = price

    def achieve(self):
        if self.requirement == self.number and not self.which_achievement in Achievement.achievements:
            print(f"{self.which_achievement} complete")
            Achievement.achievements.append(self.which_achievement)
            print(f"Du hast {self.money + self.price}$")
            return self.price




