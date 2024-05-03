from math import gcd
import os


def convert_input_to_int(input_text):
    while True:
        user_input = input(input_text)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Du hast keine Zahl eingeben.")


def plus_bruch(one, two):
    res2 = one[1] * two[1]
    res1 = one[0] * two[1] + one[1] * two[0]
    results = [res1, res2]
    results = bruch_kuerzen(results)
    return results


def minus_bruch(one, two):
    res2 = two[1] * one[1]
    res1 = two[0] * one[1] - two[1] * one[0]
    results = [res1, res2]
    results = bruch_kuerzen(results)
    return results


def multiply_bruch(one, two):
    res1 = one[1] * two[1]
    res2 = one[0] * two[0]
    one = [res2, res1]
    one = bruch_kuerzen(one)
    return one


def divide_bruch(one, two):
    res1 = one[1] * two[0]
    res2 = one[0] * two[1]
    one = [res1, res2]
    one = bruch_kuerzen(one)
    return one


def bruch_kuerzen(one):
    gcd_one = gcd(one[0], one[1])
    one[0] = int(one[0] / gcd_one)
    one[1] = int(one[1] / gcd_one)
    return one


def convert_bruch(one):
    return f"{one[0]}\n_\n{one[1]}"


def ask_for_bruch():
    one = convert_input_to_int("Bitte geben Sie eine Zahl ein: \n")
    print("_")
    two = convert_input_to_int("")
    os.system("cls")
    return one, two


operators = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
}


# Main
print("Willkommen zum Bruch-Rechner.")
while True:
    user_makes_choice = input("Welchen Operator?\n[1]: +\n[2]: -\n[3]: *\n[4]: /\n[5]: kuerzen\n[6]: exit\n")
    if user_makes_choice == "5":
        bruch_one = ask_for_bruch()
    else:
        bruch_one = ask_for_bruch()
        bruch_two = ask_for_bruch()
    if user_makes_choice == "1":
        result = plus_bruch(bruch_one, bruch_two)
    elif user_makes_choice == "2":
        result = minus_bruch(bruch_one, bruch_two)
    elif user_makes_choice == "3":
        result = multiply_bruch(bruch_one, bruch_two)
    elif user_makes_choice == "4":
        result = divide_bruch(bruch_one, bruch_two)
    elif user_makes_choice == "5":
        result = bruch_kuerzen(bruch_one)
    elif user_makes_choice == "6":
        break
    else:
        print("Du hast was falsches eingegeben! ")
    print(f"Das Ergebnis lautet: \n{convert_bruch(result)}")