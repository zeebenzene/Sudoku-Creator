from board import Board
from prover import Prover
from random import randrange




levels = {}
levels[1] = 81 - 32
levels[2] = 81 - 28
levels[3] = 81 - 26
levels[4] = 81 - 25

print("Hello and Welcome to Sudoku Creator!")
print("You can ask me to create a puzzle ranging from 1-4. 1 is easy, 4 is EVIL.")
level = ''
while level != "exit":
    level = input("\nPlease input the desired difficulty level: ")
    if(int(level) < 1 or int(level) > 4):
        print("Sorry, but that is not a valid level. Please enter 1-4")
        continue
    else:
        b = Board('')
        b.createEmptySpaces(levels[level])
        print('\n')
        b.prettyPrint()