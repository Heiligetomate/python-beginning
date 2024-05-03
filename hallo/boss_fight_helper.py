import termcolor as tc
import os

os.system("color")


class Boss:
    def __init__(self, life, strength):
        self.permanent_life = life

        self.life = life
        self.strength = strength
        if self.strength > 80:
            self.strength = 80

    def boss_gets_damaged(self, damage):
        self.life -= damage
        return damage


class Player:
    def __init__(self, life, strength, ranged_damage, mana_damage):
        self.life = life
        self.mana_damage = mana_damage
        self.strength = strength
        self.ranged_damage = ranged_damage

    def player_deals_damage(self, enemy):
        enemy.life -= self.strength

    def bow_shot_damage(self, enemy):
        enemy.life -= self.ranged_damage

    def mana_shot_damage(self, enemy):
        enemy.life -= self.mana_damage


def draw_health_bar(player_health, take_damage):
    dead_health_bar_piece = ""
    health_bar_piece = ""
    for i in range(player_health):
        health_bar_piece += "■"
    for i in range(take_damage):
        dead_health_bar_piece += "■"
        health_bar_piece = health_bar_piece[:-1]
    print(f"{tc.colored(health_bar_piece, "green")}{tc.colored(dead_health_bar_piece, "red")}")


def convert_input_to_int(input_text):
    while True:
        user_input = input(input_text)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Du hast keine Zahl eingeben.")