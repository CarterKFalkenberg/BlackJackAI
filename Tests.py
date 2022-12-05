from Deck import Deck
from Hand import Hand
from Dealer import Dealer

# TEST FOR DECK:
def test_deck():
    # create deck
    try:
        d = Deck()
    except: 
        print("Problem instantiating Deck object.")
    cards = d.cards 
    problem = False

    # make sure length is correct
    if len(cards) != 52 * 6:
        print("PROBLEM WITH LENGTH OF DECK")
        problem = True

    # make sure there are 24 2s, 3s, ..., 9s
    for i in range(2, 10):
        count = 0
        for card in cards:
            if card == i:
                count += 1
        if count != 24:
            print("PROBLEM WITH " + str(i))
            problem = True
    # make sure there are 24 As
    count = 0
    for card in cards:
        if card == "A":
            count += 1
    if count != 24:
        print("PROBLEM WITH ACE")
        problem = True
    # make sure there are 96 10s
    count = 0
    for card in cards:
        if card == 10:
            count += 1
    if count != 96:
        print("PROBLEM WITH 10")
        problem = True
    # make sure each card is valid (redundant, but just to make sure)
    for i in range(52*6):
        try:
            card = d.dealCard()
        except:
            print("Problem dealing card")
            problem = True
        if card not in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print("Invalid card in deck: " + str(card))
            problem = True
    if not problem:
        print("PASSED: DECK TEST")

# TEST HAND:    
def test_hand():
    problem = False
    d = Deck()
    hand = Hand(d, canSplit = True)
    # start by checking a bunch of aces
    hand.cards = ["A", "A", "A", "A"]
    hand.updateValue()
    if hand.value != 14:
        print("Problem with getting value of AAAA. Expected 14, got " + str(hand.value))
        problem = True
    if not problem:
        print("PASSED: HAND TEST")
    
    # check all cases of 2 non-ace numbers and then adding an ace
    for i in range(1, 11):
        for j in range(1, 11):
            hand.cards = [i, j]
            hand.updateValue()
            if hand.value != i + j:
                print("Problem with getting value of " + str(i) + str(j) + ". Expected " + str(i+j) + ", got " + str(hand.value))
                problem = True
            else:
                hand.cards.append("A")
                originalValue = hand.value
                hand.updateValue()
                if originalValue > 10:
                    if hand.value != originalValue + 1:
                        print("Problem with getting value of " + str(i) + str(j) + "A. Expected " + str(originalValue + 1) + ", got " + str(hand.value))
                        problem = True
                else:
                    hand.updateValue()
                    if hand.value != originalValue + 11:
                        print("Problem with getting value of " + str(i) + str(j) + "A. Expected " + str(originalValue + 11) + ", got " + str(hand.value))
                        problem = True
    
    # check all cases of starting with one ace and then adding an ace
    for i in range(1, 11):
        hand.cards = ["A", i]  
        hand.updateValue()
        if hand.value != 11 + i:
            print("Problem with getting value of A " + str(i) + ". Expected " + str(11+i) + ", got " + str(hand.value))  
            problem = True
        else:
            hand.cards.append("A")
            originalValue = hand.value
            hand.updateValue()
            if originalValue == 21:
                if hand.value != 12:
                    print("Problem with getting value of A " + str(i) + " A. Expected 12, got " + str(hand.value))
            elif hand.value != originalValue + 1:
                print("Problem with getting value of A " + str(i) + " A. Expected " + str(originalValue + 1) + ", got " + str(hand.value))
                problem = True

    # test cases of isSoft17
    for i in range(1,7):
        hand.cards = ["A", i]
        hand.updateValue()
        if i != 6:
            hand.cards.append(6-i)
            hand.updateValue()
        if not hand.isSoft17():
            print("Problem with isSoft17. Should be true, was false")
    for i in range(1, 6):
        hand.cards = ["A", i]
        hand.updateValue()
        if i != 5:
            hand.cards.append(5-i)
        hand.cards.append("A")
        hand.updateValue()
        if not hand.isSoft17():
            print("Problem with isSoft17. Should be true, was false")
        hand.cards.append(10)
        hand.updateValue()
        if hand.isSoft17():
            print("Problem with isSoft17. Expected false, got true")

# TEST DEALER
def test_dealer():
    problem = False
    for i in range(1000):
        dealer = Dealer(Deck())
        dealer.play()
        if dealer.hand.value < 17:
            print("Problem with dealer play method. Expected value >= 17, got value < 17")
            problem = True
        if dealer.hand.value == 17:
            if not dealer.hand.isSoft17():
                print("Problem with soft 17")
                problem = True
        if dealer.hand.value > 27:
            print("Problem with dealer hitting above 16")
            problem = True
    if not problem:
        print("PASSED: DEALER TEST")
        

# run tests
test_deck()
test_hand()
test_dealer()
