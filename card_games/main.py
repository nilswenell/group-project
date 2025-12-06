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
    ask = input('which game? blackjack? (1), poker? (2), roulette? (3), quit? (4) \n 1, 2, 3, or 4: ')
    if ask == '1':
        blackjack.play_blackjack()
    if ask =='2':    
        poker.play_game()
    if ask == '3':
        name = input("Enter your name: ")
        balance = int(input("Enter your starting balance: "))
        player = roulette.Player(name, balance)
        roulette_game = roulette.RouletteGame(player)
        roulette_game.play_roulette()
    if ask == '4':
        print('Thanks for playing!')
        break
