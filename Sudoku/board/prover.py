from board import Board


class Prover():
    def __init__(self, board):
        self.board = board
        self.count = 0

    def isRemoveValid(self, x, y):
        newBoard = self.board
        newBoard.removeElement(x, y)

        remainingLocs = self.board.getFreeLocations()
        possibleValsForFreelocs = self.getPossibleValsForLocs(remainingLocs, newBoard)

        self.proveBoard(newBoard, remainingLocs, possibleValsForFreelocs, 0, [])
        if self.count > 1:
            return False
        elif self.count == 1:
            # print("1 count")
            return True

    def remove(self, x, y):
        self.board.removeElement(x, y)

    def getPossibleValsForLocs(self, freeLocs, newBoard):
        possibleNums = {}
        for loc in freeLocs:
            x, y = loc
            possibleNums[loc] = newBoard.getAvailableInSpace(x, y)
        return possibleNums

    def proveBoard(self, board, remainingLocs, possibleNums, curIdx, prevLocs):
        if curIdx <= len(remainingLocs)-1:
            curLoc = remainingLocs[curIdx] #check all previous locs
            possible = possibleNums[curLoc] #possible nums for this location
            for num in possible:
                #check to see if new num is valid considering the previous
                valid = self.numIsValid(num, curLoc, prevLocs, possibleNums)
                #if num is valid then
                if(valid):
                    newPrev = prevLocs
                    newPrev.append(curLoc)
                    if len(newPrev) == len(remainingLocs):
                        print('ending')
                        self.count += 1
                        # return
                        # if(self.count > 1):
                        #     return
                    else:
                        self.proveBoard(board, remainingLocs, possibleNums, curIdx + 1, newPrev)

    def numIsValid(self, num, curLoc, prevLocs, possibleNums):
        x1, y1 = curLoc
        neighborhood = self.getNeighborhood(curLoc, prevLocs)
        for loc in neighborhood:
            if num == possibleNums[loc]:
                return False
        return True

    def getNeighborhood(self, curLoc, prevLocs):
        x1, y1 = curLoc
        neighborhood = []
        for loc in prevLocs:
            x2, y2 = loc
            if self.locInSameColRowSub(x1, y1, x2, y2) :
                neighborhood.append(loc)
        return neighborhood

    def locInSameColRowSub(self, x1, y1, x2, y2):
        board = self.board
        if x1 == x2 or y1 == y2 :
            return True
        elif board.modIndex(x1) == board.modIndex(x2) and board.modIndex(y1) == board.modIndex(y2):
            return True
        else:
            return False

board = Board("solved.txt")
board.prettyPrint()

prover = Prover(board)
cont = True
for x in range(9):
    for y in range(9):
        if(cont):
            prover = Prover(board)
            if(prover.isRemoveValid(x, y)):
                print('\n\n')
                # prover.remove(x, y)
                board.removeElement(x, y)
                board.prettyPrint()
            else:
                print('COUDL NOT')
                print '\n\n'
                board.prettyPrint()
                cont = False
