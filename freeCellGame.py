"""
Author: Trevor Stalnaker
File: freeCellGame.py
Version 5
"""

from cards import *
from tableau import *
from freeCell import *
from homeCell import *
from move import Move

class FreeCellGame():

    #Methods that are used for creating / replaying a game

    """
    The main constructor method for the free cell game
    """
    def __init__(self):
        
        #Create lists for the distinct pile objects
        
        self._tableaux = list()
        self._freecells = list()
        self._homecells = list()
        
        #Creates a list for containing potential moves
        
        self.potentialMoves = list()
        
        #Constructs a new game for the model
        
        self.construct()
        self.newGame()

    """
    Constructs a new game without creating a new model
    """
    def newGame(self):
        self.reset()

    """
    Allows a player to restart the current game
    """
    def restart(self):
        self.reset(self._restartDeck)

    """
    A method used to both start a new game and restart an old one
    """
    def reset(self, deck = None):
        self.clear()
        self._moveLog = []
        if deck == None:
            self._deck = Deck()
            self._deck.shuffle()
        else:
            self._deck = deck
        self.deal()
        self.getPotentialMoves()
            
    """
    Constructor class for the free cell game
    """
    def construct(self):
        for x in range(4):
            self._freecells.append(FreeCell())
            self._homecells.append(HomePile())
            self._tableaux.append(Tableau())
        for x in range(4):
            self._tableaux.append(Tableau())
    """
    Deals the cards to set a game
    """
    def deal(self):
        self._restartDeck = Deck(self._deck)
        for x in range(7):
            for y in range(4):
                self._tableaux[y].add(self._deck.deal())
        for x in range(6):
            for y in range(4, 8):
                self._tableaux[y].add(self._deck.deal())

    """
    Clears the cards from all of the cells
    """
    def clear(self):
        for x in range(4):
            self._freecells[x].clear()
            self._homecells[x].clear()
            self._tableaux[x].clear()
        for x in range(4,8):
            self._tableaux[x].clear()

    #Methods for getting move counts

    """
    Returns the number of moves performed by a player using the move log
    """
    def getMoveCount(self):
        return len(self._moveLog)

    """
    Returns the number of potential moves in a game at any given point
    """
    def getPotentialMoveCount(self):
        return len(self.potentialMoves)
            

    #Methods dealing with moving cards between piles


    """
    The moves neccessary for a tableaux
    """
    def moveTableau(self, gPile, cardPosition, rPile, card, rpos):
        if gPile.isMovable(cardPosition) and type(rPile) == Tableau:
            if rPile.isLegal(card):
                self._moveLog.append(Move(gPile, cardPosition, rPile, rpos))
                rPile.addPile(gPile, cardPosition)
                self.getPotentialMoves()
                return True
            else:
                return False
        else:
            return False

    """
    The moves neccessary for a free cell
    """
    def moveSingleCard(self, gPile, cardPosition, rPile, card, rpos):
            if rPile.isLegal(card):
                self._moveLog.append(Move(gPile, cardPosition, rPile, rpos))
                rPile.add(card)
                gPile.pop()
                self.getPotentialMoves()
                return True
            else:
                return False

    """
    Combines move methods to step through the game
    """
    def step(self, move):
        (gPile, gpos, rPile, rpos) = move.returnValues()
        card = gPile.getCardAt(gpos)
        if type(gPile) == Tableau and gpos != gPile.len() - 1:
            return self.moveTableau(gPile,gpos, rPile, card, rpos)
        else:
            if type(gPile) != HomePile:
                return self.moveSingleCard(gPile, gpos, rPile, card, rpos)

    #Methods used to convert text into a move for a terminal application of the game
            
    """
    Converts text provided by the terminal application of the game into a move and then runs the move
    """
    def textToMove(self, givingPile, cardPosition, recievingPile):
        if not self.validInput(givingPile, cardPosition, recievingPile): return False
        move = self.converter(givingPile, cardPosition, recievingPile)
        return self.step(move)
        
    """
    Used to convert incoming text into usable data
    """
    def converter(self, givingPile, gpos, recievingPile):
        gPile = self.convertStringToPileValues(givingPile)
        rPile = self.convertStringToPileValues(recievingPile)
        gpos = int(gpos)
        rpos = rPile.len()
        move = Move(gPile, gpos, rPile, rpos)
        return move

    """
    Checks the incoming input to determine if it is valid
    """
    def validInput(self, givingPile, gpos, recievingPile):
        gPile = self.convertStringToPileValues(givingPile)
        rPile = self.convertStringToPileValues(recievingPile)
        if gPile != None and rPile != None:
            if isInt(gpos):
                if int(gpos) < gPile.len():
                    return True    
        return False

    """
    Converts strings into pile values if possible
    """
    def convertStringToPileValues(self, string):
        string = string.lower()
        if string in ["t1","t2","t3","t4","t5","t6","t7","t8", \
                      "h1","h2","h3","h4","f1","f2","f3","f4"]:
            pileNumber = int(string[1])
            if string[0] == "t":
                return self._tableaux[pileNumber-1]
            elif string[0] == "h":
                return self._homecells[pileNumber-1]
            else:
                return self._freecells[pileNumber-1]
        return None

    #Methods dealing with winning and losing conditions

    """
    Determines if the game has a winner
    """
    def isWinner(self):
        if self._homecells[0].maxSize() and \
           self._homecells[1].maxSize() and \
           self._homecells[2].maxSize() and \
           self._homecells[3].maxSize():
            return True
        else:
            return False

    """
    Determines if there are still moves on the board
    """
    def areMoves(self):
        if self.getPotentialMoveCount() == 0:
            return False
        elif self.getPotentialMoveCount() == 1 and self._moveLog[-2] == self.potentialMoves[0]:
            return False
        else:
            return True

    #Additional Methods

    """
    Allows a user to take back a move
    """
    def undo(self):
        if self.getMoveCount() > 0:
            move = self._moveLog.pop()
            (gPile, gpos, rPile, rpos) = move.returnValues()
            card = rPile._lyst[rpos]
            #Deals with the case of a tableau stack
            if rpos != rPile.len() - 1:
                gPile.addPile(rPile, rpos)
            #Deals with the other cases involving single cards
            else:
                gPile.add(card)
                rPile.pop()
            self.getPotentialMoves()

    """
    An auto-pilot feature that allows the user to make the "best possible" move (Essentially a Hint)
    Works well when coupled with the undo method
    """
    def autoMove(self):
        self.step(self.getHint())

    """
    Returns a hint for the human player
    """
    def getHint(self):
        self.potentialMoves.sort()
        self.potentialMoves.reverse()
        return self.potentialMoves[0]

    """
    Runs through the current model of the game and determines how many moves are possible
    """
    def getPotentialMoves(self):
        #check the legality of moving each card at the end of a tableau and freecell
        self.potentialMoves = []

        #Runs through all the tableaux in the game
        for tableau in self._tableaux:
            if not tableau.isEmpty():
                gpos = tableau.len()-1
                card = tableau.getCardAt(gpos)
                
                #Checks if cards can be moved to homecells
                for cell in self._homecells:
                    if cell.isLegal(card):
                        self.potentialMoves.append(Move(tableau, gpos, cell))

                #Checks if cards can be moved to freecells      
                for cell in self._freecells:
                    if cell.isLegal(card):
                        self.potentialMoves.append(Move(tableau, gpos, cell))
                        
                #Checks if cards can be moved between tableaux        
                self.getPotentialTableauMoves(tableau)

        #Runs through all the freecells in the game    
        for freecell in self._freecells:
            if not freecell.isEmpty():
                gpos = 0
                card = freecell.getCardAt(0)

                #Checks if cards can be moved to homecells
                for cell in self._homecells:
                    if cell.isLegal(card):
                        self.potentialMoves.append(Move(freecell, gpos, cell))

                #Checks if cards can be moved to tableaux
                for cell in self._tableaux:
                    if cell.isLegal(card):
                        self.potentialMoves.append(Move(freecell, gpos, cell))

    """
    Runs through a given tableau and determines the position from which it is movable
    """
    def movableTableau(self, tableau):
        pos = tableau.len()-1
        card = tableau.getCardAt(pos)
        while pos >= 0:
            newCard = tableau.getCardAt(pos-1)
            if newCard.rank  == card.rank + 1 and newCard.color != card.color:
                card = newCard
                pos -= 1
            else:
                return pos

    """
    Runs through the movable stack within a tableau and determines possible moves
    """
    def getPotentialTableauMoves(self, tableau):
        pos = self.movableTableau(tableau)
        length = tableau.len()
        while pos < length:
            card = tableau.getCardAt(pos)
            for cell in self._tableaux:
                if cell.isLegal(card):
                    self.potentialMoves.append(Move(tableau, pos, cell))
            pos += 1

    """
    String representation of a free cell game
    """
    def __str__(self):
        tempstr = "Home Cells:\n"
        for x in range(4):
            tempstr += str("h"+str(x+1)+": "+str(self._homecells[x])+"\n")
        tempstr += "\nFree Cells:\n"
        for x in range(4):
            tempstr += str("f"+str(x+1)+": "+str(self._freecells[x])+"\n")
        tempstr += "\nTableaux:\n"
        for x in range(8):
            tempstr += str("t"+str(x+1)+": "+str(self._tableaux[x])+"\n")
        tempstr += "\nMove Count: " + str(self.getMoveCount()) + "\n"
        tempstr += "\nPotential Moves: " + str(self.getPotentialMoveCount()) + "\n"
        return tempstr
    
"""
Verifies if a given value is indeed an integer
"""
def isInt(integer):
    try:
        int(integer)
        return True    
    except:
        return False
    
