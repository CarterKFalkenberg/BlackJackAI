from Deck import Deck
from Hand import Hand
class Player:
    def __init__(self, deck: Deck, balance: int):
        self.hands = [Hand(deck, canPossiblySplit = True), None, None, None]
        self.deck = deck
        self.balance = balance
    # logic here is messed up. We are able to split unlimited amount of times if the 
    #   deck is [10, 10, ....]. Should only be able to split 3 times, and only if 2 cards AND card[0] == card[1]
    #   when we split, the next available slot in self.hands should become a new hand with cards [splitCard, deck.deal]
    #   and the current hand should be equal to [splitCard, deck.dealCard]. We must make sure to re check if it is now splittable
    #       maybe keep track of total splits instead of "currentSplits?"
    def play(self):
        # keep track of splits
        numSplits = 0 # max is 3
        for i, hand in enumerate(self.hands):
            print("this is hand " + str(i+1))
            if not hand:
                break
            # if blackjack, will be dealt with in Game flow
            while(hand.value < 21): 
                move = hand.makeMove()
                if move == "stand":
                    break
                elif move == "hit":
                    hand.hit()
                elif move == "double down":
                    hand.doubleDown()
                    break
                elif move == "split":
                    # keep track of the split card and split. Adjust hand and create a new one
                    splitCard = hand.cards[0]
                    hand.split()
                    numSplits += 1

                    # new hand is in the pos of the first 'None' in self.hands, whos index is just numSplits
                    # can not throw an error as canSplit was True
                    self.hands[numSplits] = Hand(self.deck, canPossiblySplit = numSplits < 3, splitCard = splitCard)
                    
                    # no hands can split if self.hands is full
                    if numSplits >= 3:
                        for j in range(i, 4):
                            self.hands[j].canSplit = False
                            
            # deal with busting immediately 
            if hand.value > 21: 
                self.balance -= hand.bet

