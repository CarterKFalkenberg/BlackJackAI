import random 
class Deck:

    # create deck (made up of 6 decks)
    def __init__(self):
        # keep track of which card was last dealt
        self.current_card_index = -1
        # 24 aces, 2s, 3s, ..., 9s
        self.cards = ["A" for i in range(24)]
        self.cards += [int(i/24)+2 for i in range(24*8)]
        # 96 10s (24 10s, Js, Qs, Ks)
        self.cards += [10 for i in range(96)]
        random.shuffle(self.cards)
        
    # deal the next card and update self.current_card_index
    def dealCard(self):
        self.current_card_index += 1
        return self.cards[self.current_card_index]



    
    
        


