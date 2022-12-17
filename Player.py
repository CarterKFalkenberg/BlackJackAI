from Deck import Deck
from Hand import Hand
class Player:
    def __init__(self, deck: Deck, balance: int):
        self.hands = [Hand(deck, canPossiblySplit = True), None, None, None]
        self.deck = deck
        
    def play(self):
        # keep track of splits
        numSplits = 0 # max is 3
        for i, hand in enumerate(self.hands):
            if not hand:
                break
            
            print("This is hand number " + str(i+1))

            # if blackjack, will be dealt with in Game flow
            while(hand.value < 21): 
                move = hand.makeMove()
                if move == "stand":
                    break
                elif move == "hit":
                    hand.hit()
                    if hand.value >= 21:
                        print(hand.toString())
                elif move == "double down":
                    hand.doubleDown()
                    print(hand.toString())
                    break
                elif move == "split":
                    # keep track of the split card and split. Adjust hand and create a new one
                    splitCard = hand.cards[0]
                    hand.split()
                    print("New hand 1: " + hand.toString())
                    numSplits += 1

                    # new hand is in the pos of the first 'None' in self.hands, whos index is just numSplits
                    # can not throw an error as canSplit was True
                    self.hands[numSplits] = Hand(self.deck, canPossiblySplit = numSplits < 3, splitCard = splitCard)
                    print("New hand 2: " + self.hands[numSplits].toString())

                    # no hands can split if self.hands is full
                    if numSplits >= 3:
                        for j in range(i, 4):
                            self.hands[j].canSplit = False
                            
            # blackjack
            if hand.hasBlackJack():
                print("You got blackjack! Nice job!")

        