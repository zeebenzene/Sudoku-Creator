import os
import random

class Board:
    def __init__(self, boardName):
        if boardName != '':
            self.wholeBoard = self.openBoard(boardName)
        else:
            self.wholeBoard = [[0 for i in range(1,10)] for x in range(9)]
            self.freePool = self.getFreeLocations()
            self.createBoardSeed()
            self.createSolvedBoard()

    def createBoardSeed(self):
        for i in range(1,10):
            location = random.choice(self.freePool)
            row = location[0]
            col = location[1]
            self.wholeBoard[row][col] = i
            self.freePool.remove(location)

    def createSolvedBoard(self):
        tried = {}
        path = []
        self.prettyPrint()
        count = 0
        # while there are still free elements
        while(len(self.freePool)> 0):
            location = random.choice(self.freePool)  #get a random free location
            row = location[0]
            col = location[1]
            potential = self.getAvailableInSpace(row,col)  #get the available elements for that location

            if(len(potential) ==0):
                while(len(potential) == 0):
                    if(len(path) ==0):
                        print("Puzzle could not be created") #This should hopefully never happen
                        return 0
                    lastTried = path[-1]

                    self.freePool.append(lastTried)
                    path.remove(lastTried)
                    self.wholeBoard[lastTried[0]][lastTried[1]] = 0
                    potential = self.getAvailableInSpace(lastTried[0],lastTried[1])
                    for ele in tried[lastTried]:
                        if ele in potential:
                            potential.remove(ele)
                    if len(potential) == 0:
                        del tried[lastTried]
                    else:
                        location = lastTried
                        row = lastTried[0]
                        col = lastTried[1]

            self.freePool.remove(location)
            answer = random.choice(potential)
            self.wholeBoard[row][col] = answer
            path.append(location)
            if(count <20):
                print(location)
                print(answer)
                print(potential)
                self.prettyPrint()
                count += 1
            if(location not in tried):
                tried[location] = [answer]
            else:
                tried[location].append(answer)
        return 1

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
        return self.wholeBoard[row][col]
    def removeElement(self, row, col):
        self.wholeBoard[row][col] = 0

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
            rowAvail = self.getAvailableInRow(x)
            colAvail = self.getAvaliableInColumn(y)
            subAvail = self.getAvailableInSubBoard(self.modIndex(x), self.modIndex(y))
            filterLambda = lambda x: (x in rowAvail) and (x in colAvail) and (x in subAvail)
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

    def checkForInvisNums(self, rowIdx,colIdx,location):
        res = []
        for ele in [0,1,2]:
            if rowIdx !=ele:
                emptySpaces = self.getEmptySpacesInSubBoard(ele,colIdx)
                sameRowPotential = []
                differentRowPotential = []
                for space in emptySpaces:
                    if space[0] == location[0]:
                        sameRowPotential += self.getAvailableInSpace(space[0],space[1])
                    else:
                        differentRowPotential += self.getAvailableInSpace(space[0],space[1])
                for answer in sameRowPotential:
                    if answer not in differentRowPotential:
                        if answer not in res:
                            res.append(answer)
        for ele2 in [0,1,2]:
            if colIdx !=ele2:
                emptySpaces = self.getEmptySpacesInSubBoard(rowIdx,ele2)
                sameColPotential = []
                differentColPotential = []
                for space in emptySpaces:
                    if space[1] == location[1]:
                        sameColPotential += self.getAvailableInSpace(space[0],space[1])
                    else:
                        differentColPotential += self.getAvailableInSpace(space[0],space[1])
                for answer in sameColPotential:
                    if answer not in differentColPotential:
                        if answer not in res:
                            res.append(answer)
        return res


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

