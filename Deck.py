

from Card import Card
import random

class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
            'Queen':10, 'King':10, 'Ace':11}
    def __init__(self):
        self.deck = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                
                self.deck.append(Card(suit,rank,Deck.values[rank]))
    
    def __str__(self):
        return (f"this deck cotains {len(self.deck)} cards")
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        """
        this returns the first card in the deck after shuffle
        """
        self.shuffle()
        return self.deck.pop(0)


if __name__ == "__main__":
    deck = Deck()
    print(deck.deck[0])
    deck.shuffle()
    print(deck.deck[0])
   