import os
import random


# wholeBoard = [[i for i in range(1,10)] for x in range(9)]

class Board:
    def __init__(self, boardName):
        self.wholeBoard = [[0 for i in range(1,10)] for x in range(9)]
        self.freePool = self.createFreePool()

    def createSolvedBoard(self):
        # select 9 random locations from the free pool and put numbers 1 - 9 in them
        for i in range(1,10):
            location = random.choice(self.freePool)
            x = location[0]
            y = location[1]
            self.wholeBoard[x][y] = i
            self.freePool.remove(location)


        tried = {}
        iterations = []
        # while there are still free elements
        while(len(self.freePool)> 0):
            location = random.choice(self.freePool)  #get a random free location
            potential = self.getPotential(tried,location[0],location[1])  #get the available elements for that location
            if(len(potential) ==0):
                while(len(potential) == 0):
                    if(len(iterations) ==0):
                        print("Puzzle could not be created") #This should hopefully never happen
                        break
                    lastTried = iterations[-1]
                    iterations.remove(lastTried)
                    self.wholeBoard[lastTried[0],lastTried[1]] = 0
                    self.freePool.append(lastTried)
                    potential = self.getPotential(tried,lastTried[0],lastTried[1])

            answer = random.choice(potential)
            self.wholeBoard[location[0],location[1]] = answer
            iterations.append(location)
            self.freePool.remove(location)
            if(location not in tried):
                tried[location] = [answer]
            else:
                tried[location].append(answer)
        return self.wholeBoard

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

    def getPotential(self,tried,location,x,y):
        potential = self.getAvailableInSpace(self,x,y)
        if (x,y) in tried:    
            for ele in tried(x,y):
                potential.remove(ele)
        return potential

    def getElement(self, x, y):
        return self.wholeBoard[y][x]

    def getColumn(self, index):
        return  [row[index] for row in self.wholeBoard]

    def getRow(self, index):
        return self.wholeBoard[index]

    #starting at 0 - 2

    def getSubBoardAsList(self, xs, ys):
        subBoardAsList = []
        for y in range((ys*3), ((ys+1)*3)):
            for x in range((xs*3), ((xs+1)*3)):
                val = self.wholeBoard[y][x]
                subBoardAsList.append(val)
        return subBoardAsList

    def getAvaliableInSpace(self, x, y):
        if self.getElement(x, y) == 0:
            fullList = [i for i in range(1, 10)]
            rowAvail = self.getAvailableInRow(y)
            colAvail = self.getAvaliableInColumn(x)
            subAvail = self.getAvailableInSubBoard(self.modIndex(x), self.modIndex(y))

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

board = Board("board1.txt")

print(board.createSolvedBoard())
#print(board.getAvailableInSubBoard(0, 0))
#print(board.getAvailableInRow(0))
#print(board.getAvaliableInColumn(0))
#print(board.getElement(2, 0))
#print(board.getAvaliableInSpace(2, 2))
