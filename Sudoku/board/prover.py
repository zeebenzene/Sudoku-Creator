# from board import Board
from random import randrange

class Prover():
    def __init__(self, board):
        self.board = board
        self.boardToProve = board
        self.count = 0

    def isRemoveValid(self, x, y):
        self.boardToProve = self.board
        self.boardToProve.setElement(x, y, 0)

        freelocs = self.boardToProve.getFreeLocations()
        possibleValsForLoc = self.getPossibleValsForLocs(freelocs, self.boardToProve)

        self.recursivelyFillWholeBoard(0, {}, freelocs, possibleValsForLoc)

        if(self.count > 1):
            return False
        elif self.count == 0:
            return False
        elif self.count == 1:
            return True


    def recursivelyFillWholeBoard(self, curIdx, prevLocToVals, freelocs, possibleValsForLoc):
        if(self.count <= 1):
            if len(prevLocToVals) < len(freelocs):
                curloc = freelocs[curIdx]
                possiblevals = possibleValsForLoc[curloc]

                for val in possiblevals:
                    valid = self.numIsValid(val, curloc, prevLocToVals)
                    if valid:
                        prevLocToVals[curloc] = val
                        self.recursivelyFillWholeBoard(curIdx+1, prevLocToVals, freelocs, possibleValsForLoc)
            else:
                self.count += 1


    def numIsValid(self, num, curLoc, prevLocToVals):
        x1, y1 = curLoc
        neighborhood = self.getNeighborhood(curLoc, prevLocToVals)
        if num in neighborhood:
            return False
        return True

    def getNeighborhood(self, curLoc, prevLocToVals):
        x1, y1 = curLoc
        neighborhood = []
        for loc in prevLocToVals.keys():
            x2, y2 = loc
            if self.locInSameColRowSub(x1, y1, x2, y2):
                neighborhood.append(prevLocToVals[loc])
        return neighborhood

    def locInSameColRowSub(self, x1, y1, x2, y2):
        board = self.board
        if x1 == x2 and y1 == y2:
            return False
        if x1 == x2 or y1 == y2:
            return True
        elif board.modIndex(x1) == board.modIndex(x2) and board.modIndex(y1) == board.modIndex(y2):
            return True
        else:
            return False

    def printRestoredBoard(self, newboard, locToVals):
        print('restored board: ')
        for loc in locToVals:
            newboard.setElement(loc[0], loc[1], locToVals[loc])
        newboard.prettyPrint()
        print '\n'
        for loc in locToVals:
            newboard.removeElement(loc[0], loc[1])

    def getPossibleValsForLocs(self, freeLocs, newBoard):
        possibleNums = {}
        for loc in freeLocs:
            x, y = loc
            possibleNums[loc] = newBoard.getAvailableInSpace(x, y)
        return possibleNums
