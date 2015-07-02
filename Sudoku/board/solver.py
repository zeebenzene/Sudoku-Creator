from board import Board
import time

def solve(board):
    loops = 0
    emptySpaces = board.getFreeLocations()
    lastCount = len(emptySpaces)
    tier = 1
    while lastCount > 0:
        for ele in emptySpaces:
            possibleValues = board.getAvailableInSpace(ele[0],ele[1])
            if tier == 2:
                rowIndex = board.modIndex(ele[0])
                colIndex = board.modIndex(ele[1])
                emptySubBoardSpaces =  board.getEmptySpacesInSubBoard(rowIndex,colIndex)
                availableInSpaces = []
                for space in emptySubBoardSpaces:
                    if space != ele:
                        availableInSpaces.append(board.getAvailableInSpace(space[0],space[1]))
                for available in availableInSpaces:
                    for elt in available:
                        if elt in possibleValues:
                            possibleValues.remove(elt)
            elif tier == 3:
                rowIndex = board.modIndex(ele[0])
                colIndex = board.modIndex(ele[1])
                cantBe = board.checkForInvisNums(rowIndex,colIndex,ele)

                for ele2 in cantBe:
                    if ele2 in possibleValues:
                        possibleValues.remove(ele2)

            if len(possibleValues) == 1:
                board.wholeBoard[ele[0]][ele[1]] = possibleValues[0]
                emptySpaces.remove(ele)
        if len(emptySpaces) == lastCount:
            if(tier == 3):
                break
            else:
                tier +=1
        else:
            if(tier >1):
                tier -=1
            lastCount = len(emptySpaces)

    return[tier*(loops+len(emptySpaces))]