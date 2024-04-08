
import random as r

def is_zahl_erraten(rate_zahl):
    max_tries = 7
    for i in range(max_tries):
        user_guess = input(f"Rate meine Zahl von 1 bis 100. Du hast noch {max_tries - i} Versuche. ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Du hast was falsches eingegeben")
            continue

        if user_guess == rate_zahl:
            print("Du hast die Zahl eraten !")
            return True
        elif user_guess > rate_zahl:
            print("Meie Zahl ist kleiner!")
        else:
            print("Meie Zahl ist größer")
    return False


rate_zahl = r.randint(1, 100)

erraten = is_zahl_erraten(rate_zahl)

if erraten == False:
    print("Du hast verloren!")