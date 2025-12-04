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
import roulette

play = True
while play == True:
    ask = input('which game? blackjack? (1), poker? (2) or roulette? (3) \n 1, 2, or 3: ')
    if ask == '1':
        blackjack.play_blackjack()
    if ask =='2':    
        poker.play_game()
    if ask == '3':
        roulette.start()
        