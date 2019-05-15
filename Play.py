#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:52:41 2019

@author: pprashan
"""

from Deck import Deck
from Hand import Hand
from Chip import Chip
import Utils
 
playing = True


player_chips = Chip()   
#the game
    
while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    
    
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    Utils.take_bet(player_chips)
    
    Utils.show_some(player_hand,dealer_hand)
    
    
    while Utils.playing:
        Utils.hit_or_stand(deck,player_hand) 
        Utils.show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            Utils.player_busts(player_hand,dealer_hand,player_chips)
            break
    Utils.playing = True
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            Utils.hit(deck,dealer_hand)    
    
        # Show all cards
        Utils.show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            Utils.dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            Utils.dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            Utils.player_wins(player_hand,dealer_hand,player_chips)

        else:
            Utils.push(player_hand,dealer_hand)  
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
    
    


