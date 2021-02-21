"""Nested dictionary to contain a full deck of cards"""
"""Each card is tied to an ID number (1-52)"""

import random
import time
import sys

#coding this thing sucked but I think it would be really useful for future
#games. Can I store this dictionary in a seperate file and just import it to
#any card game I'm looking to build?
cards = {
    1: {
        'suit':'clubs',
        'card':'2',
        'value':2},
    2: {
        'suit':'clubs',
        'card':'3',
        'value':3},
    3: {
        'suit':'clubs',
        'card':'4',
        'value':4},
    4: {
        'suit':'clubs',
        'card':'5',
        'value':5},
    5: {
        'suit':'clubs',
        'card':'6',
        'value':6},
    6: {
        'suit':'clubs',
        'card':'7',
        'value':7},
    7: {
        'suit':'clubs',
        'card':'8',
        'value':8},
    8: {
        'suit':'clubs',
        'card':'9',
        'value':9},
    9: {
        'suit':'clubs',
        'card':'10',
        'value':10},
    10: {
        'suit':'clubs',
        'card':'jack',
        'value':10},
    11: {
        'suit':'clubs',
        'card':'queen',
        'value':10},
    12: {
        'suit':'clubs',
        'card':'king',
        'value':10},
    13: {
        'suit':'clubs',
        'card':'ace',
        'value':11},
    14: {
        'suit':'diamonds',
        'card':'2',
        'value':2},
    15: {
        'suit':'diamonds',
        'card':'3',
        'value':3},
    16: {
        'suit':'diamonds',
        'card':'4',
        'value':4},
    17: {
        'suit':'diamonds',
        'card':'5',
        'value':5},
    18: {
        'suit':'diamonds',
        'card':'6',
        'value':6},
    19: {
        'suit':'diamonds',
        'card':'7',
        'value':7},
    20: {
        'suit':'diamonds',
        'card':'8',
        'value':8},
    21: {
        'suit':'diamonds',
        'card':'9',
        'value':9},
    22: {
        'suit':'diamonds',
        'card':'10',
        'value':10},
    23: {
        'suit':'diamonds',
        'card':'jack',
        'value':10},
    24: {
        'suit':'diamonds',
        'card':'queen',
        'value':10},
    25: {
        'suit':'diamonds',
        'card':'king',
        'value':10},
    26: {
        'suit':'diamonds',
        'card':'ace',
        'value':11},
    27: {
        'suit':'hearts',
        'card':'2',
        'value':2},
    28: {
        'suit':'hearts',
        'card':'3',
        'value':3},
    29: {
        'suit':'hearts',
        'card':'4',
        'value':4},
    30: {
        'suit':'hearts',
        'card':'5',
        'value':5},
    31: {
        'suit':'hearts',
        'card':'6',
        'value':6},
    32: {
        'suit':'hearts',
        'card':'7',
        'value':7},
    33: {
        'suit':'hearts',
        'card':'8',
        'value':8},
    34: {
        'suit':'hearts',
        'card':'9',
        'value':9},
    35: {
        'suit':'hearts',
        'card':'10',
        'value':10},
    36: {
        'suit':'hearts',
        'card':'jack',
        'value':10},
    37: {
        'suit':'hearts',
        'card':'queen',
        'value':10},
    38: {
        'suit':'hearts',
        'card':'king',
        'value':10},
    39: {
        'suit':'hearts',
        'card':'ace',
        'value':11},
    40: {
        'suit':'spades',
        'card':'2',
        'value':2},
    41: {
        'suit':'spades',
        'card':'3',
        'value':3},
    42: {
        'suit':'spades',
        'card':'4',
        'value':4},
    43: {
        'suit':'spades',
        'card':'5',
        'value':5},
    44: {
        'suit':'spades',
        'card':'6',
        'value':6},
    45: {
        'suit':'spades',
        'card':'7',
        'value':7},
    46: {
        'suit':'spades',
        'card':'8',
        'value':8},
    47: {
        'suit':'spades',
        'card':'9',
        'value':9},
    48: {
        'suit':'spades',
        'card':'10',
        'value':10},
    49: {
        'suit':'spades',
        'card':'jack',
        'value':10},
    50: {
        'suit':'spades',
        'card':'queen',
        'value':10},
    51: {
        'suit':'spades',
        'card':'king',
        'value':10},
    52: {
        'suit':'spades',
        'card':'ace',
        'value':11},
    }

#this section is what I'm currently working on, setting up the classes. That being said
#I'm having a hard time determining what the classes should actually be, what methods 
#should be under it, and what variables I need to define in the __init__ section. Also
#I have no idea what __init__ is supposed to be
class Hand(object):
    def __init__(self,hand,total,number_of_cards):
        self.hand = []
        self.total = 0
        self.number_of_cards = 0
  
#this section is actually functional aside from the self.hand part, which means I'm close
#to getting this script functional.  
def deal_cards():
    player_card_id = random.choice(list(cards))
    player_card = cards[player_card_id]
    self.hand.append(player_card)
    cards.pop(player_card_id)
    
    dealer_card_id = random.choice(list(cards))
    dealer_card = cards[dealer_card_id]
    dealer_hand.append(dealer_card)
    cards.pop(dealer_card_id)
     
def draw_card():
    card_id = random.choice(list(cards))
    card = cards[card_id]
    self.hand.append(card)
        
#ignore all lines below this one. As of now none of it is functional but I haven't deleted
#it because I want to use/tweak it once I set classes   
        
        
if len(player_hand) == 2:
    if player_total == 21:
        print('Blackjack!')
    else:
        print('Player is holding cards:')
        for card in player_hand:
            x = card['card']
            suit = card['suit']
            player_total += card['value']
            print(f'{x.title()} of {suit.title()}')
        print(f'\nHand value: {player_total}')
        print('\nHit or stand? ')
        move = input()

    if move == 'hit':
        draw_card()
        player_total += card['value']
        x = card['card']
        suit = card['suit']
        
        print('Drawing card...')
        time.sleep(1)
        
        print(f'\nPlayer draws card: {x} of {suit}')
            
        if player_total > 21:
            print(f'Player busts. Hand total is {player_total}')
        elif player_total == 21:
            print('Blackjack!')
        else:
            print('Player is holding: ')
            for card in player_hand:
                x = card['card']
                suit = card['suit']
                print(f'\n{x} of {suit}')
            print(f'Hand value: {player_total}')
    else:
        print(f'Dealer must beat {player_total}')
    
if __name__ == '__main__':
    