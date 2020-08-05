"""
Author: Trevor Stalnaker
File: cards.py
Project 9

Module for playing cards, with classes Card and Deck
""" 
import random

class Card(object):
    """ A card object with a suit, rank, and file name.
    The file name refers to the card's image on disk."""

    RANKS = tuple(range(1, 14))

    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    BACK_NAME = 'DECK/b.gif'

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        if not (rank in Card.RANKS):
            raise RuntimeError('Rank must be in ' + str(Card.RANKS))
        if not (suit in Card.SUITS):
            raise RuntimeError('Suit must be in ' + str(Card.SUITS))
        self.rank = rank
        self.suit = suit
        
        if self.suit == "Spades" or self.suit == "Clubs":
            self.color = "Black"
        else:
            self.color = "Red"
            
        self.fileName = 'DECK/' + str(rank) + suit[0].lower() + '.gif'
        
    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

class Deck(object):
    """A deck object that is made up of individual card objects."""
    
    def __init__(self, deck = None):
        """Creates a deck of cards"""
        self._cards = []
        if deck != None:
            for card in deck._cards:
                self._cards.append(card)
                    
        else:
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                     c = Card(rank, suit)
                     self._cards.append(c)
                     
    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self._cards)

    def deal(self):
        """Removes and returns the top card"""
        if len(self) == 0:
            return None
        else:
            return self._cards.pop(0)
        
    def __len__(self):
        """Returns the number of cards left in deck"""
        return len(self._cards)

    def __str__(self):
        """Returns string representation of the deck."""
        result = ""
        for c in self._cards:
            result = result + str(c) + "\n"
        return result

    def isEmpty(self):
        """Tests if deck is empty"""
        if len(self._cards) == 0:
            return True
        else:
            return False



