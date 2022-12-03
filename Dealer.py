from Deck import Deck
from Hand import Hand

class Dealer:
    def __init__(self, deck: Deck):
        self.hand = Hand(deck, canSplit = False)
        self.deck = deck
    def play(self):
        # if hand value > 17, stand
        while(self.hand.value <= 17):
            # if hand value == not soft 17
            if self.hand.value == 17:
                pass
                # check if soft 17
                # TODO: if not self.hand.isSoft17: 
                    # TODO: Write Hand.isSoft17
                    # break
            # else hit
            else:
                self.hand.hit()
            