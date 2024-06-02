import random as r
import os
from maumau_player_class import Player


def give_player_cards(number_cards, list_cards):
    cards_get = r.sample(list_cards, k=number_cards)
    for i in cards_get:
        list_cards.remove(i)
    return cards_get


def play_card(hand_cards, stack_card, cards):
    while True:
        while True:
            chosen_card = input("What card would you like to play? ")
            if chosen_card.lower() == "z":
                player_cards = give_player_cards(1, cards)
                hand_cards.append(player_cards[0])
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


def make_move(player, start_card, cards):
    print(f"stack: {start_card}")
    print(f"your cards {player.name}: {player.cards} (z for new card)")
    player_one, start_card = play_card(player.cards, start_card, cards)
    os.system("cls")
    return start_card


def run():
    cards = ['7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦',
             '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣']
    card_deck = list(cards)

    start_card = give_player_cards(1, card_deck)[0]
    player_one = Player(give_player_cards(5, card_deck), input("Wie heißt du? "))
    player_two = Player(give_player_cards(5, card_deck), input("Wie heißt du? "))

    while True:
        if len(card_deck) < 2:
            print("card refill!")
            card_deck = list(cards)
        start_card = make_move(player_one, start_card, card_deck)
        if player_one.check_for_win(): break
        start_card = make_move(player_two, start_card, card_deck)
        if player_two.check_for_win(): break
