from boss_fight_helper import *

weapon_text = """
You have these weapons:
[1]: sword                  
[2]: bow                    
[3]: play valorant (mage)  
[4]: talk to the boss
[5]: regenerate
"""
dodge_sets = [("1", "2"),
              ("3", "5", "2", "2"),
              ("M", "i", "a", "u"),
              ("1", "L", "w", "/"),
              ("/", "o", "1", "@", "w"),
              ("@", "1", "3", "*", "²")
              ]
time_set = (4, 5, 4, 5, 4, 6)

boss = Boss(40, 2)
player = Player(4, 2, 5, 12)
round_clock, mana, arrows = 1, 10, 3

print("=============== Boss Fight ===============")
print("_______________ Rules: ___________________")
print("There are NO rules! BUT:")
print("If u dodge the boss attack you should always press a enter after\n every char, digit or special char.")
input("Press any button to continue... ")
os.system("cls")

while boss.life > 0:

    weapon_choice = convert_input_to_int(weapon_text)
    os.system("cls")
    if weapon_choice < 1 or weapon_choice > 5 or weapon_choice == 3 and mana < 10 or weapon_choice == 2 and arrows <= 0:
        if mana < 10:
            print("You're a bad wizard! You dont have any mana left.")
        if arrows < 1:
            print("No arrows left! ")
        draw_health_bar("boss", boss.permanent_life, boss.permanent_life - boss.life)
        draw_health_bar("player", player.permanent_life, player.permanent_life - player.life)
        continue
    elif weapon_choice == 1:
        player.player_deals_damage(boss)
    elif weapon_choice == 2:
        player.bow_shot_damage(boss)
        arrows -= 1
        print(arrows)
    elif weapon_choice == 3:
        player.mana_shot_damage(boss)
        mana -= 10
    elif weapon_choice == 4:
        print("I DONT LIKE YOU HEHEHEHEHE! ")
        continue
    elif weapon_choice == 5:
        print("You got two extra mana! ")
        print("You got 1 health back!")
        print("You built two arrows!")
        mana += 2
        arrows += 2
        player.life += 1

    if boss.life < 0:
        boss.life = 0
        print("Boss dead! ")
        break

    draw_health_bar("boss", boss.permanent_life, boss.permanent_life - boss.life)
    mana += 2
    if dodge_boss(dodge_sets[round_clock - 1], time_set[round_clock - 1], player, boss):
        round_clock += 1
        player_dodged = True
    else:
        player_dodged = False
    os.system("cls")
    if player_dodged:
        print("Successfully dodged! ")
    else:
        print("Nah")
    draw_health_bar("player", player.permanent_life, player.permanent_life - player.life)
    if player.life <= 0:
        player.life = 0
        print("Player Dead! You loose. ")
        break
