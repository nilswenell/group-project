
class BlackJackGame:
    def __init__(self):
        print("Test Blackjack")

    def printsomething(something):
        print(something + ' testing')

import random

suits = ['Hearts','Diamonds','Clubs','Spades']
cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
deck = [(card,suit) for suit in suits for card in cards]
print(deck)