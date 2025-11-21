'''
class PokerGame:
    def __init__(self):
        print("Test  5-Card Draw Poker")

    def printsomething(something):
        print(something + ' testing')
'''

import random

#cards and deck
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def value(self):
        order = "23456789TJQKA"
        return order.index(self.rank)
    
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    ranks = "23456789TJQKA"
    suits = "♠♥♦♣"

    def __init__(self):
        #build full deck 52 cards
        self.cards = []
        for r in Deck.ranks:
            for s in Deck.suits:
                self.cards.append(Card(r, s))
        random.shuffle(self.cards)

    def deal(self, n):
        dealt = []
        for _ in range(n):
            dealt.append(self.cards.pop()) #remove top card
        return dealt

#hand evaluation

def hand_rank(hand):
    #get number values
    vals = []
    for c in hand:
       vals.append(c.value())
    vals.sort(reverse = True)
    
    #get suits
    suits = []
    for c in hand:
        suits.append(c.suit)
    
    counts = {}
    for v in vals:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
        
    count_vals = []
    for key in counts:
        count_vals.append(counts[key])
    count_vals.sort(reverse = True)

    #sort unique ranks descending
    uniq_vals = []
    for key in counts:
        uniq_vals.append(key)
    uniq_vals.sort(reverse = True)

    is_flush = True
    first_suit = suits[0]
    for s in suits:
        if s != first_suit:
            is_flush = False
            break
    
    is_straight = True
    for i in range(4):
        if vals[i] - 1 != vals[i + 1]:
            is_straight = False
            break
    
    #hand rankings
    if is_straight and is_flush: 
        return (8, vals) # straight flush
    if count_vals == [4,1]:
        return (7, uniq_vals) # four of a kind
    if count_vals == [3,2]:
        return (6, uniq_vals) # full house
    if is_flush:
        return (5, vals) #flush
    if is_straight:
        return (4, vals) #staight
    if count_vals == [3,1,1]:
        return (3, uniq_vals) # three of a kind
    if count_vals == [2,2,1]:
        return (2, uniq_vals) # two pair
    if count_vals == [2,1,1,1]:
        return (1, uniq_vals) # pair
    return (0, vals) #highest card

#display hands
def show_hand(name, hand):
    print(f"{name}: ", end="")
    for c in hand:
        print(c, end=" ")
    print()

#player draws cards
def player_draw(deck, hand):
    show_hand("Your hand", hand)
    discard = input("which cards to discard (1-5, space seperated) or ENTER to keep all: ")
    if discard.strip() == "":
        return hand
    
    positions = []
    parts = discard.split()
    for p in parts:
        if p.isdigit():
            positions.append(int(p)-1) #convert to 0-based index
    for i in positions:
        hand[i] = deck.deal(1)[0] #replace discared card
    return hand

def dealer_draw(deck, hand):
    num_discards = random.randint(0,3) #discard 0-3 cards randomly
    discard_positions = []
    while len(discard_positions) < num_discards:
        pos = random.randint(0,4)
        if pos not in discard_positions:
            discard_positions.append(pos)
    for i in discard_positions:
        hand[i] = deck.deal(1)[0] #replace card
    return hand

def play_game():
    print("Welcome to 5-card Poker!\n")
    deck = Deck()
    player_hand = deck.deal(5)
    dealer_hand = deck.deal(5)

    player_hand = player_draw(deck, player_hand)
    dealer_hand = dealer_draw(deck, dealer_hand)

    print("Final Hands:")
    show_hand("You", player_hand)
    show_hand("Dealer", dealer_hand)

    p_rank = hand_rank(player_hand)
    d_rank = hand_rank(dealer_hand)

    if p_rank > d_rank:
        print ("YoU win!")
    elif d_rank > p_rank:
        print("Dealer Wins!")
    else:
        print("TIE!")

#play_game()