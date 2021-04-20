"""
Author: Trevor Stalnaker
File: homePile.py
Version 3
"""

from cards import Card
from abstractPile import AbstractPile

class HomePile(AbstractPile):

    def __init__(self):
        AbstractPile.__init__(self, 13)

    def isLegal(self, newCard):
        if self.isEmpty():
            if newCard.rank == 1:
                return True
            else:
                return False
        else:
            card = self.peek()
            if card.suit == newCard.suit and card.rank == newCard.rank - 1:
                return True
            else:
                return False

def main():
    h1 = HomePile()
    c1 = Card(1, "Hearts")
    c2 = Card(6, "Spades")
    print(h1.isLegal(c1))
    print(h1.isLegal(c2))
    

    
