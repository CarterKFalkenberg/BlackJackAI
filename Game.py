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

# while player has possible move, keep executing
player.play()

# analyze game

# execute all dealer moves
# analyze game
