class Player:
    def __init__(self, cards, name):
        self.cards = cards
        self.name = name

    def check_for_win(self):
        if not self.cards:
            print(self.name, " won!")
            return True
        return False
