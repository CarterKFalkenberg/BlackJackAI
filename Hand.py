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
    # TODO: WRITE TESTS
    def updateValue(self):
        # get total value as if aces were 11, keep track of ace count
        acesWorthEleven = 0 # 
        total = 0
        for card in self.cards:
            if card == "A":
                acesWorthEleven += 1
                total += 11
            else:
                total += card 
        # if over 21, set ace values to 1, not 11
        while(total > 21 and acesWorthEleven > 0):
            acesWorthEleven -= 1 
            total -= 10 # minus value of ace (11) and add new value (1)
        self.value = total


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
