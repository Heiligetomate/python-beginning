# battle game
from war_game_character import *
import os
import termcolor as tc
import random as r

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
    user_input = input(f"[1]: {character2.name} angreifen\n[2]: warten und dafür heilen ")
    os.system("cls")
    if user_input == "1":
        random_number = r.randint(0, 99)
        if 0 <= random_number <= character1.chance_to_hit:
            character2.take_damage(character1.power)
            print(f"You dealt {character1.power} damage to {character2.name}\n")
        else:
            print(f"That didnt work")
    elif user_input == "2":
        random_heal = r.randint(1, 5)
        character1.health += r.randint(1, 5)
        if character1.health >= health:
            print("Du bist jetzt voll geheilt.")
            character1.health = health
    else:
        print("Invalid input")

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
        player_one_choice = make_str_to_int_with_input(f"Welchen Character wählst du Player {player_number}? ")
        if player_one_choice > len(character_list):
            print("Dieser Spieler existiert nicht.")
            continue
        return player_one_choice


# create instances
zwerg = Character("Zwerg", 20, 3, 70, False, "axe")
archer = Character("Archer", 15, 4, 75, True, "bow and arrow")
sword_man = Character("Sword man", 10, 6, 40, False, "sword")
crossbow = Character("Crossbow", 25, 3, 50, True, "crossbow and arrow")
oger = Character("Oger", 40, 10, 10, False, "club")
# put all instances in a list
character_list = [zwerg, archer, sword_man, crossbow, oger]
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
