from Deck import Deck
from Hand import Hand
class Player:
    def __init__(self, deck: Deck, balance: int):
        self.hands = [Hand(deck, canSplit=True), None, None, None]
        self.deck = deck
        self.balance = balance
    def play(self):
        for i, hand in enumerate(self.hands):
            if not hand:
                break
  
            # if blackjack, will be dealt with in Game flow
            while(hand.value < 21): 
                currentSplits = 0
                move = hand.makeMove()
                if move == "stand":
                    break
                elif move == "hit":
                    hand.hit()
                elif move == "double down":
                    hand.doubleDown()
                    break
                elif move == "split":
                    currentSplits += 1
                    # this only occurs when canSplit is true
                    # new hand can't split if it takes up index 3 of self.hands
                    self.hands[i + currentSplits] = Hand(self.deck, canSplit = i + currentSplits < 3)
                    # no hands can split if self.hands is full
                    if i + currentSplits >= 3:
                        for j in range(i, 4):
                            self.hands[j].canSplit = False
                            
            # deal with busting immediately 
            if hand.value > 21: 
                self.balance -= hand.bet

