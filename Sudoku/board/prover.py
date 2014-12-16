from board import Board


class Prover():
    def __init__(self, board):
        self.board = board
        self.count = 0

    def isRemoveValid(self, x, y):
        newBoard = self.board
        newBoard.removeElement(x, y)

        freeLocs = self.board.getFreeLocations()
        possibleValsForLoc = self.createPossibleValsDict(freeLocs, newBoard)

        self.proveBoard(newBoard, freeLocs, possibleValsForLoc, 0, [])
        if self.count > 1:
            return False
        elif self.count == 1:
            # print("1 count")
            return True

    def createPossibleValsDict(self, freeLocs, newBoard):
        possibleNums = {}
        for loc in freeLocs:
            possibleNums[loc] = newBoard.getAvailableInSpace(loc[0], loc[1])
        return possibleNums


    def proveBoard(self, board, freeLocs, possibleValsForLoc, curIdx, prevLocs):
        curLoc = freeLocs[curIdx]
        possibleValsInLoc = possibleValsForLoc[curLoc] #possible nums for this location
        for num in possibleValsInLoc:
            #check to see if new num is valid considering the previous
            valid = self.locIsValid(num, curLoc, curIdx, prevLocs, freeLocs)
            #if num is valid then
            if(valid):
                newPrevLocs = prevLocs
                newPrevLocs.append(num)
                if len(newPrevLocs) == len(freeLocs):
                    self.count += 1
                    if(self.count > 1):
                        return
                else:
                    self.proveBoard(board, freeLocs, possibleValsForLoc, curIdx + 1, newCombo)

    def locIsValid(self, newVal, curLoc, curIdx, prevLocs, freeLocs):
        x1, y1 = curLoc
        for loc in prevLocs:
            x2, y2 = loc
            if self.locInSameColRowSub(x1, y1, x2, y2):
                if newVal == prevLocs[idx]:
                    return False
        return True

    def locInSameColRowSub(self, x1, y1, x2, y2):
        board = self.board
        if x1 == x2 or y1 == y2 :
            return True
        elif board.modIndex(x1) == board.modIndex(x2) and board.modIndex(y1) == board.modIndex(y2):
            return True
        else:
            return False

board = Board("solved.txt")
# board.prettyPrint()

prover = Prover(board)

for x in range(9):
    for y in range(1):
        if(prover.isRemoveValid(x, y)):
            board.removeElement(x, y)
            board.prettyPrint()
        else:
            # board.prettyPrint()
            print '\n\n'
            break
