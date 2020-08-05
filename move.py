"""
Author: Trevor Stalnaker
File: move.py
Version 1
"""

from tableau import *
from freeCell import *
from homeCell import *

class Move():

    def __init__(self, gPile, gpos, rPile, rpos = None):

        self.gPile = gPile
        self.gpos = gpos
        self.rPile = rPile
        if rpos == None:
            self.rpos = rPile.len()
        else:
            self.rpos = rpos
        self.setRank()

    def returnValues(self):
        return (self.gPile, self.gpos, self.rPile, self.rpos)

    def setRank(self):
        if type(self.gPile) == Tableau:
            if type(self.rPile) == HomePile:
                self.rank = 5
            if type(self.rPile) == Tableau:
                self.rank = 3
            if type(self.rPile) == FreeCell:
                self.rank = 2
        if type(self.gPile) == FreeCell:
            if type(self.rPile) == HomePile:
                self.rank = 5
            if type(self.rPile) == Tableau:
                self.rank = 4
            if type(self.rPile) == FreeCell:
                self.rank = 1

    def __str__(self):
        return str(self.gPile) + " at position " + str(self.gpos) + " to " + str(self.rPile) + " at position " + str(self.rpos)

    def __eq__(self, other):
        return self.rank == other.rank
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __gt__(self, other):
        return self.rank > other.rank
