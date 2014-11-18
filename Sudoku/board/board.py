import os
import random


# wholeBoard = [[i for i in range(1,10)] for x in range(9)]

class Board:
    def __init__(self, boardName):
        self.wholeBoard = [[0 for i in range(1,10)] for x in range(9)]
        # self.wholeBoard = self.openBoard(boardName)
        self.freePool = self.createFreePool()

    def createSolvedBoard(self):
        # select 9 random locations from the free pool and put numbers 1 - 9 in them
        for i in range(1,10):
            location = random.choice(self.freePool)
            row = location[0]
            col = location[1]
            self.wholeBoard[row][col] = i
            self.freePool.remove(location)


        tried = {}
        path = []
        # while there are still free elements
        while(len(self.freePool)> 0):
            location = random.choice(self.freePool)  #get a random free location
            self.freePool.remove(location)
            row = location[0]
            col = location[1]
            potential = self.getAvaliableInSpace(row,col)  #get the available elements for that location
            if potential == "filled":
            	print(location)
            	self.prettyPrint()
            if(len(potential) ==0):
                while(len(potential) == 0):
                    if(len(path) ==0):
                        print("Puzzle could not be created") #This should hopefully never happen
                        break
                    lastTried = path[-1]
                    path.remove(lastTried)
                    self.freePool.append(lastTried)
                    self.wholeBoard[lastTried[0]][lastTried[1]] = 0
                    potential = self.getAvaliableInSpace(lastTried[0],lastTried[1])
                    for ele in tried[lastTried]:
                        if ele in potential:
                            potential.remove(ele)
                    if len(potential) == 0:
                        del tried[lastTried]
                    else:
                    	self.freePool.remove(lastTried)
                    	row = lastTried[0]
                    	col = lastTried[1]
                    

            answer = random.choice(potential)
            self.wholeBoard[row][col] = answer
            path.append(location)
            if(location not in tried):
                tried[location] = [answer]
            else:
                tried[location].append(answer)

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
        if list.count(value) == 1:
            return False
        else:
            return True

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

    def getAvaliableInSpace(self, row, col):
        if self.getElement(row, col) == 0:
            fullList = [i for i in range(1, 10)]
            rowAvail = self.getAvailableInRow(row)
            colAvail = self.getAvaliableInColumn(col)
            subAvail = self.getAvailableInSubBoard(self.modIndex(row), self.modIndex(col))

            filterLambda = lambda x: (x in rowAvail) and (x in colAvail) and (x in subAvail)
            return filter(filterLambda, fullList)
        else:
            return "filled"

    def modIndex(self, idx):
        if 0 <= idx <= 2:
            return 0
        if 2 < idx <= 5:
            return 1
        if 5 < idx <= 8:
            return 2

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

board = Board("board2.txt")
board.createSolvedBoard()
board.prettyPrint()
#print(board.getAvailableInSubBoard(0, 0))
#print(board.getAvailableInRow(0))
#print(board.getAvaliableInColumn(0))
#print(board.getElement(2, 0))
#print(board.getAvaliableInSpace(0, 1))
