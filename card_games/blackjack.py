
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

#deal cards

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
    else:
        print('stand')
        pass






#initialize variables
my_money = 1000
endgame = False

#start loop for whole game
while my_money >0 and endgame ==False:
    
    #initialize more variables
    pot = 0
    bet = 0
    win = False

    my_hand = []
    dealer_hand = []
    
    #ask for the first bet
    bet = input('bet:')
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
        print(f'your hand: {my_hand} value: {hand_value(my_hand)}')
        print(f'dealer hand: {dealer_hand}value: {hand_value(dealer_hand)}')


        #check for automatic blackjack win
        if hand_value(my_hand) == 21:
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
                if hand_value(my_hand) == 21:
                    my_money += (pot*2)
                    pot = 0
                    bet = 0
                    print('blackjack!')
                    print(f'my money: {my_money}.')
                    endloop=True
                
                #ask hit or stand
                player_turn(my_hand)
                
                #check for bust
                if hand_value(my_hand)>21:
        
                    pot = 0
                    bet = 0
                    print(f'your hand: {my_hand} value: {hand_value(my_hand)}')
                    print('bust')
                    print(f'my money: {my_money}.')
                    endloop=True
                
                else:    
       
                    #dealer hits on 17, unless player has more than 17
                    while hand_value(dealer_hand)<17 or hand_value(dealer_hand)<hand_value(my_hand):
                        deal_card(dealer_hand)
                        print(f'dealer hand: {dealer_hand}value: {hand_value(dealer_hand)}')
                
                    #if tied, push
                    if hand_value(dealer_hand)>16 and hand_value(dealer_hand) == hand_value(my_hand):
                        my_money += pot
                        pot = 0
                        bet = 0
                        print('push')
                        print(f'my money: {my_money}.')
                        endloop=True
                    
                    #dealer bust
                    elif hand_value(dealer_hand)>21:
                        my_money += (pot*2)
                        pot = 0
                        bet = 0
                        print('you win!')
                        print(f'my money: {my_money}.')
                        endloop=True
                    else:
                        print(f'your hand: {my_hand} value: {hand_value(my_hand)}')
                        print(f'dealer hand: {dealer_hand}value: {hand_value(dealer_hand)}')

#result of game
if my_money<1:
    print('you lost all your money!!!!')                    
else:
    print(f'you ended with ${my_money}.')
