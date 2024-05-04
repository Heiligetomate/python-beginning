import termcolor as tc
import os
import time

os.system("color")


class Boss:
    def __init__(self, life, strength):
        self.permanent_life = life

        self.life = life
        self.strength = strength
        if self.strength > 80:
            self.strength = 80

    def boss_deals_damaged(self, player):
        player.life -= self.strength
        print(f"Boss dealt {self.strength} damage!")


class Player:
    def __init__(self, life, strength, ranged_damage, mana_damage):
        self.life = life
        self.permanent_life = life
        self.mana_damage = mana_damage
        self.strength = strength
        self.ranged_damage = ranged_damage

    def player_deals_damage(self, enemy):
        enemy.life -= self.strength

    def bow_shot_damage(self, enemy):
        enemy.life -= self.ranged_damage

    def mana_shot_damage(self, enemy):
        enemy.life -= self.mana_damage


def draw_health_bar(player_name, player_health, take_damage):
    dead_health_bar_piece = ""
    health_bar_piece = ""
    for i in range(player_health):
        health_bar_piece += "■"
    for i in range(take_damage):
        dead_health_bar_piece += "■"
        health_bar_piece = health_bar_piece[:-1]
    print(f"{player_name}'s health: ")
    print(f"{tc.colored(health_bar_piece, "green")}{tc.colored(dead_health_bar_piece, "red")}")
    print(tc.colored(f"{player_health - take_damage}/{player_health}", "green"))


def convert_input_to_int(input_text):
    while True:
        user_input = input(input_text)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Du hast keine Zahl eingeben.")


def dodge_boss(pattern: tuple, timer: int, player: Player, boss: Boss) -> bool:
    str_pattern = ""
    for i in pattern:
        str_pattern += i
    print(f"remember this: {str_pattern}")
    old_time = time.time()
    for i in pattern:
        if i == input():
            continue
        boss.boss_deals_damaged(player)
        return False
    new_time = time.time()
    if new_time - old_time > timer:
        boss.boss_deals_damaged(player)
        return False
    elif new_time - old_time < timer:
        return True


