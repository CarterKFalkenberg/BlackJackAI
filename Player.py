from Deck import Deck
from Hand import Hand
class Player:
    def __init__(self, deck: Deck):
        self.hands = [Hand(deck, canSplit=True), None, None, None]
    def play(self):
        for i, hand in enumerate(self.hands):
            if not hand:
                break
            if hand.value == 21: #HAND.VALUE NEEDS TO BE IMPLEMENTED
                # BLACKJACK
                pass
            while(hand.value < 21): #HAND.VALUE NEEDS TO BE IMPLEMENTED
                currentSplits = 0
                move = hand.makeMove()
                if move == "stand":
                    break
                elif move == "hit":
                    # hit. NEED TO IMPLEMENT
                    pass
                elif move == "double down":
                    # double down. NEED TO IMPLEMENT
                    pass
                elif move == "split":
                    currentSplits += 1
                    # this only occurs when canSplit is true
                    self.hands[i + currentSplits] = Hand(self.deck, canSplit = i + currentSplits <= 3)
                    if i + currentSplits > 3:
                        for j in range(i, 4):
                            self.hands[j].canSplit = False
            if hand.value > 21: #HAND.VALUE NEEDS TO BE IMPLEMENTED
                # update money # NEEDS TO BE IMPLEMENTED
                pass
