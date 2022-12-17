from Deck import Deck
from Hand import Hand
from Player import Player
from Dealer import Dealer 


# create deck
deck = Deck()

# create player
startingBalance = 1000
player = Player(deck, startingBalance)

# create dealer
dealer = Dealer(deck)

print("Welcome to BlackJack. You are starting with " + str(startingBalance)
    +  "coins. Good luck!")


# while player has possible move, keep executing
player.play()

# check for 1 or more blackjacks

# execute all dealer moves
dealer.play()

# analyze game
