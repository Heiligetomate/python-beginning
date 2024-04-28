# battle game
from war_game_character import *
import os
import termcolor as tc
import random as r
import sys

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


def upgrade_menu(player):
    upgrade_choice = input("[1]: upgrade health\n[2]: upgrade power ")
    if upgrade_choice == "1":
        player.upgrade_health(3, 50)
    elif upgrade_choice == "2":
        player.upgrade_damage(2, 50)


def one_full_round():
    while True:
        reward = 45
        main_game(player_one, player_two, player_one_health + juri.extra_health)
        if player_two.health <= 0:
            print(f"{matti.name} is dead now")
            print(f"{juri.name} win's")
            juri.money += reward
            print(f"{juri.name} gets {reward} gold.")
            break
        main_game(player_two, player_one, player_two_health + juri.extra_health)
        if player_one.health <= 0:
            print(f"{juri.name} is dead now")
            print(f"{matti.name} win's")
            print(f"{matti.name} gets {reward} gold.")
            matti.money += reward
            break


# create instances

juri = Player("Juri", 0)
matti = Player("Matti", 0)
# put all instances in a list


while True:
    zwerg = Character("Zwerg", 20, 3, 70, False, "axe")
    archer = Character("Archer", 15, 4, 75, True, "bow and arrow")
    sword_man = Character("Sword man", 10, 6, 40, False, "sword")
    crossbow = Character("Crossbow", 25, 3, 50, True, "crossbow and arrow")
    oger = Character("Oger", 40, 10, 15, False, "club")
    character_list = [zwerg, archer, sword_man, crossbow, oger]

    while True:
        play_question = input("Play?\n[1]: leave\n[2]: upgrade\nzum spielen einen anderen Button drücken ")
        if play_question == "2":
            who_wants_to_upgrade = input(f"Who wants to upgrade?\n[1]: {juri.name}\n[2]: {matti.name}\n[3]: go back\n")
            if who_wants_to_upgrade == "1":
                upgrade_menu(juri)
            elif who_wants_to_upgrade == "2":
                upgrade_menu(matti)
            else:
                print("Invalid input! ")
        elif play_question == "1":
            print(f"{juri.name}: {juri.money}$\n{matti.name}: {matti.money}$")
            sys.exit()
        else:
            break
    # let player make choice
    for i in character_list:
        print(f"[{character_list.index(i) + 1}]: {i.name}: (health: {i.health}, power: {i.power})")
    player_one_index_choice = let_player_make_choice("one") - 1
    player_one = character_list[player_one_index_choice]
    player_one.extra_strength = juri.extra_strength
    player_one.extra_health = juri.extra_health
    while True:

        player_two_index_choice = let_player_make_choice("two") - 1
        if player_two_index_choice == player_one_index_choice:
            print("Dieser Character ist schon vergeben. ")
            continue
        break
    player_two = character_list[player_two_index_choice]
    player_two.extra_strength = matti.extra_strength
    player_two.extra_health = matti.extra_health
    player_one_health = player_one.health
    player_two_health = player_two.health

    # game loop
    one_full_round()
