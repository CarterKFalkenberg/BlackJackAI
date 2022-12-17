from Deck import Deck
from Hand import Hand

class Dealer:
    def __init__(self, deck: Deck):
        self.hand = Hand(deck, canPossiblySplit = False)
        self.deck = deck
    def play(self):
        # if hand value > 17, stand
        while(self.hand.value <= 17):
            # if hand value == not soft 17
            if self.hand.value == 17:
                # check if soft 17
                if self.hand.isSoft17: 
                    self.hand.hit()
                else:
                    break
            # else hit
            else:
                self.hand.hit()

    # determines if dealer has blackjack
    def hasBlackJack(self):
        if self.hand.value == 21 and len(self.hand.cards) == 2:
            return True
        return False
            