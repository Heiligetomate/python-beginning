import random as r
import os


def give_player_cards(number_cards, list_cards):
    cards_get = r.choices(list_cards, k=number_cards)
    for i in cards_get:
        list_cards.remove(i)
    return cards_get


def play_card(hand_cards, stack_card, cards):
    while True:
        while True:
            chosen_card = input("What card would you like to play? ")
            if chosen_card.lower() == "z":
                hand_cards.append(give_player_cards(1, cards)[0])
                return hand_cards, stack_card
            try:
                chosen_card = int(chosen_card)
                if chosen_card > len(hand_cards):
                    print("Sorry, but no")
                    continue
                break
            except ValueError:
                print("Sorry, but no")

        if hand_cards[chosen_card - 1][0] == stack_card[0] or hand_cards[chosen_card - 1][1] == stack_card[1]:
            break
        else:
            print("Sorry that's not possible. Try again.")
    stack_card = hand_cards[chosen_card - 1]
    hand_cards.remove(hand_cards[chosen_card - 1])
    return hand_cards, stack_card


def run():
    cards = ['7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦',
             '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣']

    start_card = r.choice(cards)
    cards.remove(start_card)
    player_one = give_player_cards(5, cards)
    player_two = give_player_cards(5, cards)

    while True:
        # one
        print(f"stack: {start_card}")
        print(f"your cards player one: {player_one} (Z for new card)")
        player_one, start_card = play_card(player_one, start_card, cards)
        os.system("cls")
        # two
        print(f"stack: {start_card}")
        print(f"your cards player two: {player_two} (Z for new card)")
        player_two, start_card = play_card(player_two, start_card, cards)
        os.system("cls")


