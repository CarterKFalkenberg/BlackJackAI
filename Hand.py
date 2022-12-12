from Deck import Deck
class Hand:
    # init 
    def __init__(self, deck: Deck, canSplit: bool, splitCard = None):
        self.deck = deck
        if splitCard is None: 
            self.cards = [deck.dealCard(), deck.dealCard()]
        else:
            self.cards = [splitCard, deck.dealCard()]
        self.canHit = True
        self.canSplit = canSplit and self.cards[0] == self.cards[1] 
        self.value = 0
        self.updateValue()
        self.bet = 10 # we aren't asking user bc it will be constant for AI
    
    # sets value to the value of the hand
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
    def makeMove(self):

        # if they can not make a move (if they cant hit, they can't split either.)
        if not self.canHit:
            return "stand"
        print(self.toString())
        # if they can split, they can do anything (only 2 cards)
        if self.canSplit:
            answer = input("Would you like to stand(1), hit(2), double down(3), or split(4)")
            while answer not in ["1", "2", "3", "4"]:
                answer = input("Invalid answer. Would you like to stand(1), hit(2), double down(3), or split(4)")

        # if 2 cards and can't split, they can hit, stand, double down
        elif len(self.cards) == 2:
            answer = input("Would you like to stand(1), hit(2), or double down(3)")
            while answer not in ["1", "2", "3"]:
                answer = input("Invalid answer. Would you like to stand(1), hit(2), or double down(3)")

        # otherwise, they can stand or hit
        else:
            answer = input("Would you like to stand(1) or hit(2)")
            while answer not in ["1", "2"]:
                answer = input("Invalid answer. Would you like to stand(1) or hit(2)")
    
        numToAnswer = {"1": "stand", "2": "hit", "3": "double down", "4": "split"}
        return numToAnswer[answer]


    # add a card to the hand
    # this will be used for Double Down as well (logic is dealt with in makeMove)
    def hit(self):
        self.cards.append(self.deck.dealCard())
        self.updateValue()

    # hit and double bet. set canHit to False
    def doubleDown(self):
        self.hit()
        self.bet += self.bet
        self.canHit = False

    # simply gets rid of one card and adds a new one (logic of new hand is dealt with in player class)
    # update canSplit
    def split(self):
        self.cards[0] = self.deck.dealCard()
        self.updateValue()
        self.canSplit = self.cards[0] == self.cards[1] 

    # returns true if dealer has value 17 and an ace with value 11
    def isSoft17(self):
        # make sure value is 17
        if self.value != 17:
            raise Exception("Called Hand.isSoft17, but dealer hand not equal to 17") 
        # count how many aces as well as keep track of total
        acesWorthEleven = 0 
        total = 0
        for card in self.cards:
            if card == "A":
                acesWorthEleven += 1
                total += 11
            else:
                total += card
        # adjust the amount of aces that are worth eleven
        while (acesWorthEleven > 0 and total > 21):
            acesWorthEleven -= 1
            total -= 10
        
        # if there are any acesWorthEleven, then it is a soft 17
        if acesWorthEleven > 0:
            return True
        else: 
            return False
    
    # determines if a hand is blackjack
    def hasBlackJack(self):
        if self.value == 21 and len(self.cards) == 2:
            return True
        return False

    # show user their hand
    def toString(self):
        returnStr = "Cards: "
        for card in self.cards:
            returnStr += str(card) + " "
        returnStr += "Value: " + str(self.value)
        return returnStr
        
        