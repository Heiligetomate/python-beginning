import random
import sys


def make_move(x_or_o, position):
    battle_field[position] = x_or_o


def print_battle_field():
    print(f"{battle_field[0]} | {battle_field[1]} | {battle_field[2]}")
    print(f"{battle_field[3]} | {battle_field[4]} | {battle_field[5]}")
    print(f"{battle_field[6]} | {battle_field[7]} | {battle_field[8]}")
    #print(f"{battle_field[0:3]}\n{battle_field[3:6]}\n{battle_field[6:9]}")


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
    check_for_win()


def check_for_win():
    for i in range(len(win_sets)):
        if battle_field[win_sets[i][0]] == "X" and battle_field[win_sets[i][1]] == "X" and battle_field[
            win_sets[i][2]] == "X":
            print("Team X wins")
            print_battle_field()
            sys.exit()
        elif battle_field[win_sets[i][0]] == "O" and battle_field[win_sets[i][1]] == "O" and battle_field[
            win_sets[i][2]] == "O":
            print("Team O wins")
            print_battle_field()

            sys.exit()


def bot_move():
    while True:
        random_field = random.randint(0, 8)
        if battle_field[random_field] == "X" or battle_field[random_field] == "O":
            continue
        make_move("O", random_field)
        break
    check_for_win()


def print_win(color):
    print(f"Team {color} wins")
    print_battle_field()
    sys.exit()


def bot_make_winning_move(color):
    for i in range(len(win_sets)):
        if battle_field[win_sets[i][0]] == color and battle_field[win_sets[i][1]] == color and battle_field[
            win_sets[i][2]] == " ":
            battle_field[win_sets[i][2]] = "O"
            if color == "O":
                print_win("O")
            else:
                return True
        elif battle_field[win_sets[i][0]] == color and battle_field[win_sets[i][2]] == color and battle_field[
            win_sets[i][1]] == " ":
            battle_field[win_sets[i][1]] = "O"
            if color == "O":
                print_win("O")
            else:
                return True
        elif battle_field[win_sets[i][1]] == color and battle_field[win_sets[i][2]] == color and battle_field[
            win_sets[i][0]] == " ":
            battle_field[win_sets[i][0]] = "O"
            if color == "O":
                print_win("O")
            else:
                return True


def bot():
    bot_make_winning_move("O")
    a = bot_make_winning_move("X")
    if a == True:
        return None
    elif battle_field[4] == " ":
        battle_field[4] = "O"
    else:
        bot_move()


battle_field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win_sets = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

for i in range(9):
    players_move()
    bot()
