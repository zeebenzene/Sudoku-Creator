from board import Board


class Prover():
    def __init__(self, board):
        self.board = board
        self.count = 0

    def isRemoveValid(self, x, y):
        newBoard = self.board
        newBoard.removeElement(x, y)

        freeLocs = self.board.getFreeLocations()
        possibleNums = self.createPossibleNumsDict(freeLocs, newBoard)

        self.proveBoard(newBoard, freeLocs, possibleNums, 0, [])
        if self.count > 1:
            return False
        elif self.count == 1:
            # print("1 count")
            return True

    def createPossibleNumsDict(self, freeLocs, newBoard):
        possibleNums = {}
        for loc in freeLocs:
            possibleNums[loc] = newBoard.getAvailableInSpace(loc[0], loc[1])
        return possibleNums


    def proveBoard(self, board, freeLocs, possibleNums, curIdx, prevCombos):
        curLoc = freeLocs[curIdx]
        possible = possibleNums[curLoc] #possible nums for this location
        for num in possible:
            #check to see if new num is valid considering the previous
            valid = self.numIsValid(num, curLoc, curIdx, prevCombos, freeLocs)
            #if num is valid then
            if(valid):
                newCombo = prevCombos
                newCombo.append(num)
                if len(newCombo) == len(freeLocs):
                    self.count += 1
                    if(self.count > 1):
                        return
                else:
                    self.proveBoard(board, freeLocs, possibleNums, curIdx + 1, newCombo)

    def numIsValid(self, num, curLoc, curIdx, prevCombos, freeLocs):
        for idx in range(curIdx):
            prevLoc = freeLocs[idx]
            x1, y1 = curLoc
            x2, y2 = prevLoc
            if self.locInSameColRowSub(x1, y1, x2, y2):
                if num == prevCombos[idx]:
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
