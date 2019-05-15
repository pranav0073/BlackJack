#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:28:49 2019

@author: pprashan
"""

from Card import Card
from Deck import Deck

class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
        
    def add_card(self,card):
        if(type(card) == Card):
            self.cards.append(card)
            self.value += card.value
            if(card.rank == "Ace"):
                self.aces += 1
            
    
    def adjust_for_ace(self):
        while self.value  > 21 and self.aces:
            self.value -= 10
            self.aces -=1
            

if __name__ == "__main__":
    test_deck = Deck()
    test_deck.shuffle()
    test_player = Hand()
    test_player.add_card(test_deck.deal())
    test_player.add_card(test_deck.deal())
    print(test_player.cards[0])
    print(test_player.cards[1])
    print(test_player.value)
    
    