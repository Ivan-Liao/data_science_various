from Card import Card
import random

class Deck():
    dict_blackjack_values = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    list_suits = ['s','h','d','c']
    """
    Deck class. Also keeps track of round specific information.
    Class Attributes:
        dict_blackjack_values - dictionary to convert card to value
        list_suits - list of possible suits
    
    Attributes:
        list_deck
    
    Methods
    
    """
    
    def __init__(self):
        self.list_deck, self.list_discard = self.shuffle()
        
    def shuffle(self):
        list_deck, list_discard = [], []
        for key in self.dict_blackjack_values.keys():
            for suit in self.list_suits:
                list_deck.append(Card(key,suit))
        random.shuffle(list_deck)
        return list_deck, list_discard
        
    def draw(self):
        card_drawn = self.list_deck.pop()
        self.list_discard.append(card_drawn)
        return card_drawn
    
    def deal_start(self, p_hand, c_hand):
        p_hand = [self.draw()] + [self.draw()]
        c_hand = [self.draw()] + [self.draw()]
        return p_hand, c_hand
    
    def is_over(self):
        pass
        