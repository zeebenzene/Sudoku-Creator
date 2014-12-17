import os
import random

class Board:
    def __init__(self, boardName):
        if boardName != '':
            self.wholeBoard = self.openBoard(boardName)
        else:
            self.wholeBoard = [[0 for i in range(1,10)] for x in range(9)]

    def createBoardSeed(self):
        for i in range(1,10):
            location = random.choice(self.freePool)
            row = location[0]
            col = location[1]
            self.wholeBoard[row][col] = i
            self.freePool.remove(location)

    def createBlankBoard(self):
        return [[0 for i in range(1, 10)] for x in range(9)]

    def openBoard(self, boardName):
        sep = os.sep
        appendName = sep + 'resources' + sep + boardName
        filePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        file = open(filePath + appendName, 'r')
        lines = file.readlines()

        board = [[int(elem) for elem in line.split(' ')] for line in lines]
        return board


    def getElement(self, row, col):
        return self.wholeBoard[col][row]
    def removeElement(self, row, col):
        self.wholeBoard[col][row] = 0
    def setElement(self, row, col, val):
        self.wholeBoard[col][row] = val

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

    def getAvailableInSpace(self, x, y):
         if self.getElement(x, y) == 0:
            fullList = [i for i in range(1, 10)]
            rowAvail = self.getAvailableInRow(y)
            colAvail = self.getAvaliableInColumn(x)
            subAvail = self.getAvailableInSubBoard(self.modIndex(y), self.modIndex(x))
            filterLambda = lambda z: (z in rowAvail) and (z in colAvail) and (z in subAvail)
            return filter(filterLambda, fullList)
         else:
             return "filled"

    def getEmptySpacesInSubBoard(self,rows,cols):
        res = []
        for y in range((rows*3), ((rows+1)*3)):
            for x in range((cols*3), ((cols+1)*3)):
                if self.wholeBoard[y][x] == 0:
                    res.append((y,x))
        return res

    def getFreeLocations(self):
        locations = []
        for x in range(0, 9):
            for y in range(0, 9):
                if self.getElement(x, y) == 0:
                    locations.append((x, y))
        return locations

    def modIndex(self, idx):
        return idx/3

    def getAvailableInSubBoard(self, x, y):
        list = self.getSubBoardAsList(x, y)
        return self.getAvailableInList(list)
    def getAvailableInRow(self, y):
        list = self.getRow(y)
        return self.getAvailableInList(list)
    def getAvaliableInColumn(self, x):
        list = self.getColumn(x)
        return self.getAvailableInList(list)

    def getAvailableInList(self, list):
        fullList = [x for x in range(1, 10)]
        return filter(lambda x: x not in list, fullList)

    def prettyPrint(self):
        for row in self.wholeBoard:
            print(row)