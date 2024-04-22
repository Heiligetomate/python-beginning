money = 3

class asdsd:
    def __init__(self, a, b, money):
        self.a = a
        self.b = b
        self.money = money

    def blablabla(self, money):
        money += 11
        self.money = money

    money = blablabla(money)


d = asdsd(1, 2, money)
print(d.a)
print(d.b)
print(d.money)
print(money)

# KLAASSEN SIND DRECK