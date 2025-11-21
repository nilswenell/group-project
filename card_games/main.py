'''
from blackjack import BlackJackGame
if __name__=='__main__':
    game1 = BlackJackGame()
BlackJackGame.printsomething('something')

from poker import PokerGame
if __name__=='__main__':
    game1 = PokerGame()
PokerGame.printsomething('something')
'''
import blackjack
import poker

play = True
while play == True:
    ask = input('which game? blackjack? (1) or poker? (2) \n 1 or 2: ')
    if ask == '1':
        blackjack.play_blackjack()
    if ask =='2':    
        poker.play_game()