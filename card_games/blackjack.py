
class BlackJackGame:
    def __init__(self):
        print("Test Blackjack")

    def printsomething(something):
        print(something + ' testing')

import random

#making a deck
suits = ['♠','♥','♦','♣']
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

#hand class
class Hand:
    #initiate variables
    def __init__(self,_player):
        self.player = _player
        self.cards = []
    #returns the number value of hand
    def get_value(self):
        value = 0
        for card in self.cards:
            value += get_card_value(card)
        if 'Ace' in self.cards:
            if value >21:
                value -=10
        return value
    #adds a card to the hand
    def add_card(self,card):
        self.cards.append(card)

    def __str__(self):
        return self.cards

#deal cards

def deal_card(hand : Hand):
    random_card = random.choice(deck)
    hand.add_card(random_card)
    deck.remove(random_card)

    
#player turn
def player_turn(player):
    hit_or_stand = input('hit or stand?')
    if hit_or_stand == 'hit':
        deal_card(player)
    else:
        print('stand')
        pass




def play_blackjack():
    print('Welcome to blackjack!')

#initialize variables
    my_money = 1000
    endgame = False

#start loop for whole game
    while my_money >0 and endgame ==False:
    
    #initialize more variables
        pot = 0
        bet = 0
        win = False

    #my_hand = []
    #dealer_hand = []
        my_hand = Hand('Player')
        dealer_hand = Hand('Dealer')
    
    #ask for the first bet
        bet = input('enter bet or type "quit" :')


    #always check if the player wants to quit
        if bet == 'quit':
            endgame = True
        else:
        #adjust variables for start of turn
            bet = int(bet)
            my_money -= bet
            pot += bet
        
        #show player their money, the pot
            print(f'my money: {my_money}. pot: {pot}.')
        
        #deal player 2 cards, 1 to dealer
            deal_card(my_hand)
            deal_card(dealer_hand)
            deal_card(my_hand)

        #show the hands and values
            print(f'your hand: {my_hand.cards} value: {my_hand.get_value()}')
            print(f'dealer hand: {dealer_hand.cards}value: {dealer_hand.get_value()}')


        #check for automatic blackjack win
            if my_hand.get_value() == 21:
                my_money += (pot*2)
                pot = 0
                bet = 0
                print('blackjack!')
                print(f'my money: {my_money}.')
        
            else:
            #begin loop of an individual turn
                endloop = False
                while endloop == False:
        
                #check for blackjack every time
                    if my_hand.get_value() == 21:
                        my_money += (pot*2)
                        pot = 0
                        bet = 0
                        print('blackjack!')
                        print(f'my money: {my_money}.')
                        endloop=True
                
                    if dealer_hand.get_value()==21:
                        pot = 0
                        bet = 0
                        print('dealer blackjack- you lose!')
                        print(f'my money: {my_money}.')
                        endloop = True

                #ask hit or stand
                    player_turn(my_hand)
                
                #check for bust
                    if my_hand.get_value()>21:
        
                        pot = 0
                        bet = 0
                        print(f'your hand: {my_hand.cards} value: {my_hand.get_value()}')
                        print('bust')
                        print(f'my money: {my_money}.')
                        endloop=True
                
                    else:    
       
                    #dealer hits on 17, unless player has more than 17
                        while dealer_hand.get_value()<17 or dealer_hand.get_value()<my_hand.get_value():
                            deal_card(dealer_hand)
                            print(f'dealer hand: {dealer_hand.cards}value: {dealer_hand.get_value()}')
                        
                
                    #if tied, push
                        if dealer_hand.get_value()>16 and dealer_hand.get_value() == my_hand.get_value():
                            my_money += pot
                            pot = 0
                            bet = 0
                            print('push')
                            print(f'my money: {my_money}.')
                            endloop=True
                    
                    #dealer bust
                        elif dealer_hand.get_value()>21:
                            my_money += (pot*2)
                            pot = 0
                            bet = 0
                            print('you win!')
                            print(f'my money: {my_money}.')
                            endloop=True
                        else:
                            print(f'your hand: {my_hand.cards} value: {my_hand.get_value()}')
                            print(f'dealer hand: {dealer_hand.cards}value: {dealer_hand.get_value()}')

#result of game
    if my_money<1:
        print('you lost all your money!!!!')                    
    else:
        print(f'you ended with ${my_money}.')

#play_blackjack()