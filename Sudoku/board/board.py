import os
import random


# wholeBoard = [[i for i in range(1,10)] for x in range(9)]

class Board:
    def __init__(self, boardName):
        # self.wholeBoard = self.createBlankBoard()
        self.wholeBoard = self.openBoard(boardName)
        self.freePool = self.createFreePool()

    def createBlankBoard(self):
        return [[0 for i in range(1,10)] for x in range(9)]

    def openBoard(self, boardName):
        sep = os.sep
        appendName = sep + 'resources' + sep + boardName
        filePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        file = open(filePath + appendName, 'r')
        lines = file.readlines()

        board = [[int(elem) for elem in line.split(' ')] for line in lines]
        return board

    def createFreePool(self):
        freePool = []
        for i in range(9):
            for j in range(9):
                if(self.getElement(i,j) == 0):
                    freePool.append((i,j))
        return freePool

    def isDuplicateIn(self, list, value):
        return not (list.count(value) == 1)

    def getElement(self, row, col):
        return self.wholeBoard[row][col]
    def getColumn(self, index):
        return  [row[index] for row in self.wholeBoard]
    def getRow(self, index):
        return self.wholeBoard[index]

    #starting at 0 - 2
    def getSubBoardAsList(self, rows, cols):
        subBoardAsList = []
        for y in range((rows*3), ((rows+1)*3)):
            for x in range((cols*3), ((cols+1)*3)):
                val = self.wholeBoard[y][x]
                subBoardAsList.append(val)
        return subBoardAsList

    def rawToSubIndex(self, idx):
        return idx / 3

    def getAvaliableInSpace(self, row, col):
        if self.getElement(row, col) == 0:
            fullList = [i for i in range(1, 10)]
            rowAvail = self.getAvailableInRow(row)
            colAvail = self.getAvaliableInColumn(col)
            subAvail = self.getAvailableInSubBoard(self.rawToSubIndex(row), self.rawToSubIndex(col))

            filterLambda = lambda x: (x in rowAvail) and (x in colAvail) and (x in subAvail)
            return filter(filterLambda, fullList)
        else:
            return "filled"
    def getAvailableInSubBoard(self, row, col):
        list = self.getSubBoardAsList(row, col)
        return self.getAvailableInList(list)
    def getAvailableInRow(self, row):
        list = self.getRow(row)
        return self.getAvailableInList(list)
    def getAvaliableInColumn(self, col):
        list = self.getColumn(col)
        return self.getAvailableInList(list)
    def getAvailableInList(self, list):
        fullList = [x for x in range(1, 10)]
        return filter(lambda x: x not in list, fullList)


    def prettyPrint(self):
        for row in self.wholeBoard:
            print(row)

# board = Board("board2.txt")
# board.createSolvedBoard()
# board.prettyPrint()
#print(board.getAvailableInSubBoard(0, 0))
#print(board.getAvailableInRow(0))
#print(board.getAvaliableInColumn(0))
#print(board.getElement(2, 0))
#print(board.getAvaliableInSpace(0, 1))