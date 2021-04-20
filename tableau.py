"""
Author: Trevor Stalnaker
File: tableau.py
Version 3
"""

from abstractPile import AbstractPile

class Tableau(AbstractPile):

    def __init__(self):
        AbstractPile.__init__(self, 52)

    def isMovable(self, position):
        card = self._lyst[position]
        for x in range(position + 1, len(self._lyst)):
            if self._lyst[x].rank == card.rank - 1 and self._lyst[x].color != card.color:
                card = self._lyst[x]
            else:
                return False
        return True

    def addPile(self, other, position):
        moveCount = 0
        for x in range(position, other.len()):
            self.add(other._lyst[x])
            moveCount += 1
        for x in range(moveCount):
            other.pop()

    def isLegal(self, newCard):
        if self.isEmpty():
            return True
        else:
            card = self.peek()
            if card.color != newCard.color and card.rank == newCard.rank +1:
                return True
            else:
                return False

        
