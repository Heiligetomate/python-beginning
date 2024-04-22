import random

battle_field = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def make_move(x_or_o, position):
    battle_field[position] = x_or_o


def print_battle_field():
    print(f"{battle_field[0:3]}\n{battle_field[3:6]}\n{battle_field[6:9]}")


def make_string_to_int(input_text, extra_condition=None):
    while True:
        user_input = input(input_text)
        try:
            user_input = int(user_input)
            if user_input > extra_condition:
                continue
            break
        except ValueError:
            print("Please enter a number")
    return user_input



# make_move("X", 4)
# print_battle_field()
while True:
    print_battle_field()
    move_pos = make_string_to_int("Where do you want to place your marker? ", 8)
    make_move("X", move_pos)