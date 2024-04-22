#casino

import random as r
import os




digits = ["2", "3", "4", "5", "6", "7", "8", "9", "Z", "J", "Q", "K", "A"]
zeichen = ""
money = 25


def double(random_digit):
    for i in digits:
        count = random_digit.count(i)
        if count == 2:
            return 5
        elif count == 3:
            return 10

    return 0

def buchtabe():
    zeichen = r.choices(digits, k=5)
    zeichen = "".join(zeichen)
    return zeichen

while True:
    user_input = input("Willst du spielen? ")
    if user_input.lower() == "j":
        while True:
            gesetztes_geld = input("Wie viel wollen sie setzen? ")
            gesetztes_geld = int(gesetztes_geld)
            if money - gesetztes_geld <= 0:
                print("Du hast nicht so viel")
            else:
                break
        balken = buchtabe()
        print(balken)
        win_money = double(balken) * gesetztes_geld
        money = money + win_money

        print(f"Du hast {win_money}$ gewonnen.")
        print(f"Du hast {money}")
    elif user_input.lower() == "n":
        break
    else:
        print("Du hast was ungueltiges eingegeben. ")
