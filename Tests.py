import Deck

# TEST FOR DECK:
def test_deck():
    d = Deck()
    cards = d.cards 
    problem = False
    for i in range(1, 9):
        count = 0
        for card in cards:
            if card == i:
                count += 1
        if count != 24:
            print("PROBLEM WITH " + str(i))
            problem = True
    count = 0
    for card in cards:
        if card == "A":
            count += 1
    if count != 24:
        print("PROBLEM WITH ACE")
        problem = True
    count = 0
    for card in cards:
        if card == 10:
            count += 1
    if count != 96:
        print("PROBLEM WITH 10")
        problem = True
    if not problem:
        print("ALL GOOD")
        
