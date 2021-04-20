"""
Author: Trevor Stalnaker
File: freecell.py
Version 3
"""

from abstractPile import AbstractPile

class FreeCell(AbstractPile):

    def __init__(self):
        AbstractPile.__init__(self, 1)

    def isLegal(self, newCard):
        if self.isEmpty():
            return True
        else:
            return False
