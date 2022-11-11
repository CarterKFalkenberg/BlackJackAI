from Deck import Deck
class Hand:
    # init 
    def __init__(self, deck: Deck, canSplit: bool):
        self.deck = deck
        self.cards = [deck.dealCard(), deck.dealCard()]
        self.canSplit = canSplit
        self.value = 0
        self.updateValue()
    
    # sets value to the value of the hand
    # to be implemented
    def updateValue(self):
        #self.value = ...
        pass

    # eventually will be computer based, but for now used based
    # will return string of: hit, stand, double down, or split
    # to be implemented
    def makeMove(self):
        pass

    # add a card to the hand
    # this will be used for Double Down as well (logic is dealt with in makeMove)
    def hit(self):
        self.cards.append(self.deck.dealCard())
        self.updateValue()

    # simply gets rid of one card and adds a new one (logic of new hand is dealt with in player class)
    def split(self):
        self.cards[0] = self.deck.dealCard()
        self.updateValue()
