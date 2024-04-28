import termcolor as tc
import os
from war_game_character import *


zwerg = Character("Zwerg", 20, 3)
archer = Character("Archer", 15, 4)
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
    #print(tc.colored(dead_health_bar_piece + "■", "red"))

zwerg_health = zwerg.health
for i in range(2):
    draw_health_bar(zwerg_health, zwerg_health - zwerg.health)
    zwerg.health -= archer.power


