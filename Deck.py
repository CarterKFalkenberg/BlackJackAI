import random 
class Deck:

    # create deck (made up of 6 decks)
    def __init__(self):
        # 24 aces, 2s, 3s, ..., 9s
        self.cards = ["A" for i in range(24)]
        self.cards += [int(i/24)+1 for i in range(24*8)]
        # 96 10s (24 10s, Js, Qs, Ks)
        self.cards += [10 for i in range(96)]
        random.shuffle(self.cards)
        


