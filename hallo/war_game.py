# battle game
from war_game_character import *
import os
import termcolor as tc

os.system("color")


def draw_health_bar(player_health, take_damage):
    dead_health_bar_piece = ""
    health_bar_piece = ""
    for i in range(player_health):
        health_bar_piece += "■"
    for i in range(take_damage):
        dead_health_bar_piece += "■"
        health_bar_piece = health_bar_piece[:-1]
    print(f"{tc.colored(health_bar_piece, "green")}{tc.colored(dead_health_bar_piece, "red")}")


def main_game(character1, character2, health):
    print(f"{character1.name}'s move")
    draw_health_bar(health, health - character1.health)
    print(f"{character1.health}/{health}")
    input("Attack player two? ")
    os.system("cls")
    print(f"You dealt {character1.power} damage\n")
    character1.health -= character2.power


def characters_move(character, enemy):
    character.take_damage(enemy.power)
    if not character.is_alive:
        print(f"{character.name} is dead")
        return False
    return True


def make_str_to_int_with_input(input_text):
    while True:
        a = input(input_text)
        try:
            a = int(a)
            return a
        except ValueError:
            print("Bitte eine Zahl eingeben.")


def let_player_make_choice(player_number):
    while True:
        player_one_choice = make_str_to_int_with_input(f"Welchen Characer waehlst du Player {player_number}? ")
        if player_one_choice > len(character_list):
            print("Dieser Spieler existiert nicht.")
            continue
        return player_one_choice


# create instances
zwerg = Character("Zwerg", 20, 3)
archer = Character("Archer", 15, 4)
sword_man = Character("Sword man", 10, 6)
crossbow = Character("Crossbow", 25, 3)
# put all instances in a list
character_list = [zwerg, archer, sword_man, crossbow]
# let player make choice
for i in character_list:
    print(f"[{character_list.index(i) + 1}]: {i.name}: (health: {i.health}, power: {i.power})")
player_one = character_list[let_player_make_choice("one") - 1]
player_two = character_list[let_player_make_choice("two") - 1]

player_one_health = player_one.health
player_two_health = player_two.health

# game loop
while True:
    main_game(player_one, player_two, player_one_health)
    if player_one.health <= 0:
        print(f"{player_one.name} is dead now")
        print(f"{player_two.name} win's")
        break

    main_game(player_two, player_one, player_two_health)
    if player_two.health <= 0:
        print(f"{player_two.name} is dead now")
        print(f"{player_one.name} win's")
        break
