import os


class Board:
    def __init__(self, boardName):
        self.wholeBoard = self.openBoard(boardName)

    def openBoard(self, boardName):
        sep = os.sep
        appendName = sep + 'resources' + sep + boardName
        filePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        file = open(filePath + appendName, 'r')
        lines = file.readlinesfda() ########///testing pycharm git integration

        board = [[int(elem) for elem in line.split(' ')] for line in lines]
        return board

    def isDuplicateIn(self, list, value):
        if list.count(value) == 1:
            return False
        else:
            return True

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

print(board.getAvailableInSubBoard(0, 0))
print(board.getAvailableInRow(0))
print(board.getAvaliableInColumn(0))
print(board.getElement(2, 0))
print(board.getAvaliableInSpace(2, 2))