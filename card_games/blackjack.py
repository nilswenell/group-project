
class BlackJackGame:
    def __init__(self):
        print("Test Blackjack")

    def printsomething(something):
        print(something + ' testing')

import random

#making a deck
suits = ['Hearts','Diamonds','Clubs','Spades']
cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
deck = [(card,suit) for suit in suits for card in cards]
#print(deck)

#return card value
def get_card_value(card):
    if card[0] in ['Jack','Queen','King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

random.shuffle(deck)

#deal cards

hand_1 = []
hand_2 = []

def deal_card(hand):
    random_card = random.choice(deck)
    hand.append(random_card)
    deck.remove(random_card)

#hand value
def hand_value(hand):
    value = 0
    for card in hand:
        value += get_card_value(card)
    if 'Ace' in hand:
        if value >21:
            value -=10
    return value

#player turn
def player_turn(player):
    hit_or_stand = input('hit or stand?')
    if hit_or_stand == 'hit':
        deal_card(player)
        if hand_value(player)>21:
            print('bust')
    else:
        print('stand')
        pass

deal_card(hand_1)
deal_card(hand_2)
deal_card(hand_1)
deal_card(hand_2)

print(f'hand 1: {hand_1} value: {hand_value(hand_1)}')
print(f'hand 2: {hand_2}value: {hand_value(hand_2)}')

player_turn(hand_1)
player_turn(hand_2)
