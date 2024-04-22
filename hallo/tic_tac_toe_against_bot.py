import random
import sys


def make_move(x_or_o, position):
    battle_field[position] = x_or_o


def print_battle_field():
    print(f"{battle_field[0:3]}\n{battle_field[3:6]}\n{battle_field[6:9]}")


def make_string_to_int(input_text, extra_condition=None, error_text=""):
    while True:
        user_input = input(input_text)
        try:
            user_input = int(user_input)
            if user_input > extra_condition + 1:
                print(error_text)
                continue
            break
        except ValueError:
            print("Please enter a number")
    return user_input


def players_move():
    while True:
        print_battle_field()
        move_pos = make_string_to_int("Where do you want to place your marker? ", 8, "Not in range")
        if battle_field[move_pos - 1] == "X" or battle_field[move_pos - 1] == "O":
            print("Already placed")
            continue
        make_move("X", move_pos - 1)
        break


def win_condition(a, b, c):
    if battle_field[a] == "X" and battle_field[b] == "X" and battle_field[c] == "X":
        print("Team X wins")
        sys.exit()
    elif battle_field[a] == "O" and battle_field[b] == "O" and battle_field[c] == "O":
        print("Team O wins")
        sys.exit()


def check_for_win():
    win_condition(0, 1, 2)
    win_condition(0, 1, 2)


def bot_move():
    while True:
        random_field = random.randint(0, 8)
        if battle_field[random_field] == "X" or battle_field[random_field] == "O":
            continue
        make_move("O", random_field)
        break


battle_field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
for i in range(9):
    players_move()
    bot_move()
