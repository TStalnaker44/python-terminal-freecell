"""
Author: Trevor Stalnaker
File: abstractPile.py
Version 3
"""

from cards import *

class AbstractPile():

    def __init__(self, maxSize):
        self._lyst = list()
        self._maxSize = maxSize

    def add(self, card):
        self._lyst.append(card)

    def peek(self):
        return self._lyst[len(self._lyst) - 1]

    def isEmpty(self):
        if len(self._lyst) == 0:
            return True
        else:
            return False
        
    def len(self):
        return len(self._lyst)

    def maxSize(self):
        if self._maxSize == self.len():
            return True
        else:
            return False

    def getCardAt(self, position):
        if position < self.len(): 
            return self._lyst[position]

    def clear(self):
        self._lyst = []

    def pop(self):
        if not self.isEmpty():
            self._lyst.pop()


    def __str__(self):
        tempstr = "["
        for card in self._lyst:
            tempstr += str(card)
            if self._lyst.index(card) != len(self._lyst) - 1:
                tempstr += ", "
        tempstr += "]"
        return tempstr
        
        
        
    
