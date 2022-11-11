from Deck import Deck

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
        
# run tests
test_deck()
