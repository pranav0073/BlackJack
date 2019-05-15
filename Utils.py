#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:08:08 2019

@author: pprashan
"""
 
playing = True

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips you want to bet?"))
        except ValueError:
            print("Sorry, be must be an integer!")
        else:
            if(chips.bet  > chips.total):
                print("Sorry, your bet can't exceed ", chips.total)
            else:
                break;

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck, hand):
    global playing
    
    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's' ")
        if(x[0].lower() == 'h'):
            hit(deck, hand)
        elif(x[0].lower() == 's'):
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry again")
            continue
        break
    
def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
## Functions to hanle the game scenarios
    
def player_busts(player,dealer, chips):
    print("player busts!")
    chips.lose_bet()
    
    
def player_wins(player, dealer, chips):
    print("player wins")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
    
#the game