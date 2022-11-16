from Deck import Deck
from Hand import Hand
class Player:
    def __init__(self, deck: Deck):
        self.hands = [Hand(deck, canSplit=True), None, None, None]
