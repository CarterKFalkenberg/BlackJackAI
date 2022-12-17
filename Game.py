from Deck import Deck
from Hand import Hand
from Player import Player
from Dealer import Dealer 


# create deck
deck = Deck()

# initialize game
balance = 1000
print("Welcome to BlackJack. You are starting with " + str(balance)
    +  "coins. Good luck!")

while(balance > 10): # 10 is our default bet
    # create player
    player = Player(deck, balance)

    # create dealer
    dealer = Dealer(deck)

    # current balance
    print("Balance: " + str(balance))

    # check for dealer blackjack (insurance is not a thing in this)
    if dealer.hasBlackJack():
        if player.hands[0].hasBlackJack():
            print("Both player and dealer got blackjack! Round over!")
        else:
            print("Dealer had blackjack! You lose your bet")
            balance -= player.hands[0].bet
        continue
            
    
    print("Dealer is showing a " + str(dealer.hand.cards[0]))

    # while player has possible move, keep executing
    player.play()

    # check for 1 or more blackjacks
    for hand in player.hands:
        if hand is None:
            break 

        # blackjack pays 3:2
        if hand.hasBlackJack():
            balance += 3 * hand.bet // 2
            print("Your blackjack was a success! You earned " + str(3 * hand.bet // 2))

    # execute all dealer moves
    dealer.play()
    print("Dealer " + dealer.hand.toString())

    # analyze game
    for hand in player.hands:

        # no hand or we already dealt with the balance
        if hand is None or hand.hasBlackJack():
            break

        # bust is auto loss
        if hand.value > 21:
            balance -= hand.bet
            print("You busted, you lose the bet.")

        
        # then, dealer bust is auto win
        elif dealer.hand.value > 21:
            balance += hand.bet
            print("You win. Dealer busted")

        # otherwise, compare to dealer
        elif hand.value > dealer.hand.value:
            balance += hand.bet
            print("Nice! You gained " + str(hand.bet))
        elif hand.value < dealer.hand.value:
            balance -= hand.bet
            print("Sorry! You lost " + str(hand.bet))

        # otherwise, it is a push, and we do nothing
        else:
            print("Push! No money gained or lost")

print("You finished with balance: " + str(player.balance))
       
