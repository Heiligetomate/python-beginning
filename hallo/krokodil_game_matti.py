import random as r


def print_list(list_p):
    teeth_s = ""
    for i in list_p:
        if i == "X":
            teeth_s += "? "
            continue
        teeth_s += f"{i} "
    return teeth_s


def let_him_make_choice(list_p):
    while True:
        choice = input("Welches Zähnchen? ")
        try:
            choice = int(choice)
            if choice > len(list_p) or choice <= 0:
                print("So geht das aber nicht Sportsfreund!")
                continue
            break
        except ValueError:
            print("So geht das aber nicht Sportsfreund!")
    if list_p[choice - 1] == "X":
        print("Du hast einen schönen saftigen Zahn erwischt!")
        return False
    else:
        print(f"Das war kein böser Zahn an Position {choice} !")
        list_p.pop(choice - 1)
    return list_p


evil_tooth = r.randint(0, 13)
teeth = ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]
teeth[evil_tooth] = "X"
user1 = input("Wer bist du(1)? ")
user2 = input("Wer bist du(2)? ")

for i in range(len(teeth)):
    print(print_list(teeth))
    teeth = let_him_make_choice(teeth)
    if not teeth:
        if i % 2 == 0:
            print(f"{user1} du hast verloren; {user2} du hast gewonnen.")
        else:
            print(f"{user2} du hast verloren; {user1} du hast gewonnen.")
        break

