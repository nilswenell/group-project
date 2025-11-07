
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
    if card in ['Jack','Queen','King']:
        return 10
    elif card == 'Ace':
        return 11
    else:
        return int(card)

random.shuffle(deck)

#deal cards

hand_1 = []
hand_2 = []

def deal_card(hand):
    random_card = random.choice(deck)
    hand.append(random_card)
    deck.remove(random_card)
