
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

my_hand = []
dealer_hand = []

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







my_money = 1000
pot = 0
bet = 0
win = False

bet = int(input('bet:'))
my_money -= bet
pot += bet
print(f'my money: {my_money}. pot: {pot}.')
deal_card(my_hand)
deal_card(dealer_hand)
deal_card(my_hand)
if hand_value(my_hand) == 21:
    my_money += (pot*2)
    pot = 0
    bet = 0
else:


    print(f'hand 1: {my_hand} value: {hand_value(my_hand)}')
    print(f'hand 2: {dealer_hand}value: {hand_value(dealer_hand)}')

    player_turn(my_hand)
    print(f'hand 1: {my_hand} value: {hand_value(my_hand)}')
    print(f'hand 2: {dealer_hand}value: {hand_value(dealer_hand)}')

