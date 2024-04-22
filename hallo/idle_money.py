import time as t
import sys


# Fehler beim Geldabbuchen oder Geldabfragen
def print_game():
    print(f"Geld.          : {money}")
    print(f"Arbeiter.      : {workers}")
    print(f"effizienz.     : {effec}")


def time():
    new_time = t.time()
    time_count = new_time - old_time
    time_count = int(time_count)
    return time_count


def achievement(requirement, number, price, achievement):
    if requirement >= number and not achievement in achievements:
        print(f"Achievement {achievement} complete")
        players_stats[3] += price
        print(f"Herzlichen Glückwunsch! Sie haben {price}$ durch Skill verdient.")
        achievements.append(achievement)
    return 0


def achievement_with_loop(condition, achievement_text):
    for i in range(20):
        count = (i + 1) * 5
        bonus = int(20 ** (0.35 * i + 1))
        achievement(condition, count, bonus, f"{achievement_text} {i + 1}")


players_stats = [1, 1, 1, 5000000]
achievements = []
worker_price = 5
effec_price = 5
multiply = 2
worker_count = 0

old_time = t.time()

while True:

    workers = players_stats[0]
    effec = players_stats[1]
    manager = players_stats[2]
    money = players_stats[3]

    user_input = input(
        "Was wollen sie tun?\n[1] : Geld abholen \n[2] : zum Upgradecenter\n[3] : Achievements\n[4] : Inventar abrufen\n[5] : Cosmetic Shop\n[6] : zum verlassen\n")

    if user_input == "1":
        money_collected = time() * workers * effec
        print(f"Sie haben {money_collected}$ verdient.")
        players_stats[3] += money_collected
        money = players_stats[3]
        print_game()
        old_time = t.time()

    elif user_input == "2":
        if not money >= worker_price and not money >= effec_price:
            print("Du bist zu arm um dir etwas zu kaufen komm spaeter wieder.")
            continue
        upgrade_choice = input(
            f"[1]: Arbeiter upgraden {worker_price}$\n[2]: Effizienz upgraden {effec_price}$\n[3]: zum verlassen\n")
        if upgrade_choice == "1" and money >= worker_price:
            players_stats[int(upgrade_choice) - 1] += 1
            players_stats[3] = money - worker_price
            worker_price = int(5 * (1.2 ** workers))

        elif upgrade_choice == "2" and money >= effec_price:
            players_stats[int(upgrade_choice) - 1] += 1
            players_stats[3] = money - effec_price
            effec_price = int(5 * (1.2 ** effec))

        else:
            print("Du hast etwas ungueltige Eingegeben")

    elif user_input == "3":
        achievement_with_loop(workers, "Worker")
        achievement_with_loop(effec, "Effizienz")
        for i in range(20):
            sparen = 10 ** (i + 1)
            sparen_gewinn = sparen / 2
            achievement(money, sparen, sparen_gewinn, f"Spaarhoernchie{i + 1}")


    elif user_input == "6":
        sys.exit()
