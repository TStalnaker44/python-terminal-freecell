"""
Author: Trevor Stalnaker
File: main.py
Version 3
"""

from freeCellGame import *

def main():
    game = FreeCellGame()
    print(game)
    while not game.isWinner() and game.areMoves():
        userMove = input("What is your next move?\n<FromPile>:<Position>:<ToPile>\n>>")
        if userMove == "RESTART":
            game.restart()
            print(game)
        elif userMove == "NEW GAME":
            game.newGame()
            print(game)
        elif userMove == "UNDO":
            game.undo()
            print(game)
        elif userMove == "HINT":
            print("Hint: " + str(game.getHint()) + "\n")
            print(game)
        elif userMove == "AUTO PILOT":
            game.autoMove()
            print(game)
        else:
            moveLyst = userMove.split(":")
            if len(moveLyst) != 3:
                print("Illegal Move")
            else:
                if not game.textToMove(moveLyst[0], moveLyst[1], moveLyst[2]):
                    print("Illegal Move")
            print("\n" + str(game))
    if game.isWinner():
        print("You Win!")
    else:
        print("No More Moves!  You Lose!")

if __name__ == "__main__":
    main()


