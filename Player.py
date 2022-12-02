from Deck import Deck
from Hand import Hand
class Player:
    def __init__(self, deck: Deck):
        self.hands = [Hand(deck, canSplit=True), None, None, None]
    def play(self):
        for i, hand in enumerate(self.hands):
            if not hand:
                break
            if hand.value == 21: 
                # BLACKJACK
                pass
            while(hand.value < 21): 
                currentSplits = 0
                move = hand.makeMove()
                if move == "stand":
                    break
                elif move == "hit":
                    # TODO
                    pass
                elif move == "double down":
                    # TODO
                    pass
                elif move == "split":
                    currentSplits += 1
                    # this only occurs when canSplit is true
                    # new hand can't split if it takes up index 3 of self.hands
                    self.hands[i + currentSplits] = Hand(self.deck, canSplit = i + currentSplits < 3)
                    # no hands can split if self.hands is full
                    if i + currentSplits >= 3:
                        for j in range(i, 4):
                            self.hands[j].canSplit = False
            if hand.value > 21: 
                #TODO: Update money
                pass
