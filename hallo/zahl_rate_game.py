
import random as r
def is_zahl_erraten(rate_zahl):
    rate_zahl = r.randint(1, 100)
    for i in range(7):
        user_guess = input(f"Rate meine Zahl von 1 bis 100. Du hast Versuche. ")
        if int(user_guess) == rate_zahl:
            print("Du hast die Zahl eraten !")
            return True
        elif int(user_guess) > rate_zahl:
            print("Meie Zahl ist kleiner!")
        elif int(user_guess) < rate_zahl:
            print("Meie Zahl ist größer")
        else:
            print('INVALID!')
    return False

is_zahl_erraten(1)


#erraten = is_zahl_erraten(rate_zahl)
#
#if erraten == False:
#    print("Du hast verloren!")