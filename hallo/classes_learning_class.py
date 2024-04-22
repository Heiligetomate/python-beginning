class Phones:

    def __init__(self, name, price, quantity, broken_phones=0, discount=1):
        assert price >= 0, "Price cannot be negative"
        assert quantity >= 0, "quantity cannot be negative"
        assert broken_phones >= 0, "broken phones cannot be negative"

        self.name = name
        self.quantity = quantity
        self.broken_phones = broken_phones
        self.price = price
        self.discount = discount
        def broken_calculation(self, quantity, broken_phones):
            working_phones = quantity - broken_phones
            if working_phones < 0:
                raise ValueError(f"Ammount of working Phones cannot be negative, but was: {working_phones}")
            return working_phones

        def discount_calculation(self, discount_factor):
            self.price = self.price * discount_factor
            return self.price

        self.price = discount_calculation(self, self.discount)
        self.working_phones = broken_calculation(self, quantity, broken_phones)
        self.total_price = self.working_phones * self.price

    def __repr__(self):
        return (f"name : {self.name} \nprice : {self.price} \nworking phones : {self.working_phones} \nprice for all "
                f"working phones : {self.total_price}")

