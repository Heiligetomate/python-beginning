from math import gcd


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


def print_bruch(one):
    print(one[0])
    print("_")
    print(one[1])


