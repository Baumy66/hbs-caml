import os

class Board:
    RED = 1
    BLACK = 2
    EMPTY = 0
    board = None
    turn = None

    def checkForWinner(self):
        # 0 - No Winner
        # 1 - Red wins
        # 2 - Black Wins
        # -1 - Tie
        winner = self.checkRowsForWinner()
        if(winner != 0):
            return winner
        winner = self.checkVerticalsForWinner()
        if(winner != 0):
            return winner
        winner = self.checkDiagonalsForWinner()
        if(winner == 0):
            if(self.checkForTie()):
                return -1
        return winner
    
    def checkRowsForWinner(self):
        row = 0
        while row < 6:
            col = 0
            while col < 4:
                if(self.board[row][col] != self.EMPTY and self.board[row][col] == self.board[row][col + 1] and self.board[row][col] == self.board[row][col + 2] and self.board[row][col] == self.board[row][col + 3]):
                    return self.board[row][col]
                col = col + 1
            row = row + 1
        return 0
            
    def checkForTie(self):
        if(self.board[5][0] != 0 and self.board[5][1] != 0 and self.board[5][2] != 0 and self.board[5][3] != 0 and self.board[5][4] != 0 and self.board[5][5] != 0 and self.board[5][6] != 0):
            return True
        return False

    def checkVerticalsForWinner(self):
        col = 0
        while col < 7:
            row = 0
            while row < 3:
                if(self.board[row][col] != self.EMPTY and self.board[row][col] == self.board[row+1][col] and self.board[row][col] == self.board[row + 2][col] and self.board[row][col] == self.board[row + 3][col]):
                    return self.board[row][col]
                row = row + 1
            col = col + 1
        return 0

    def checkDiagonalsForWinner(self):
        # Up and Left
        row = 0
        while row < 3:
            col = 0
            while col < 4:
                if(self.board[row][col] != self.EMPTY and self.board[row][col] == self.board[row + 1][col + 1] and self.board[row][col] == self.board[row + 2][col + 2] and self.board[row][col] == self.board[row + 3][col + 3]):
                    return self.board[row][col]
                col = col + 1
            row = row + 1

        # Down and Right
        row = 5
        while row > 2:
            col = 0
            while col < 4:
                if(self.board[row][col] != self.EMPTY and self.board[row][col] == self.board[row - 1][col + 1] and self.board[row][col] == self.board[row - 2][col + 2] and self.board[row][col] == self.board[row - 3][col + 3]):
                    return self.board[row][col]
                col = col + 1
            row = row - 1
        return 0

    def turnToString(self):
        if(self.turn == self.RED):
            return 'Red'
        else:
            return 'Black'

    def solicateInput(self):
        print('It is ' + self.turnToString() + '\'s Turn')
        val = input("Column to Drop: ") 
        convertedValue = self.convertToInteger(val)
        self.makeMove(convertedValue)

    def convertToInteger(self, col):
        if(ord(col) > 96):
            return ord(col) - 97
        elif(ord(col) > 64):
            return ord(col) - 65
        else:
            return ord(col) - 48

    def makeMove(self, column):
        i = 0
        while i < 6:
            if(self.board[i][column]==0):
                self.board[i][column] = self.turn
                break
            i = i + 1
        if(self.turn == self.RED):
            self.turn = self.BLACK
        else:
            self.turn = self.RED
        
    def initialize(self):
        board = []
        self.turn = self.BLACK
        i = 0
        while i < 6:
            board.append([0, 0, 0, 0, 0, 0, 0])
            i = i + 1
        self.board = board

    def printBoard(self):
        print('    ---------------------')
        self.printRow(5)
        self.printRow(4)
        self.printRow(3)
        self.printRow(2)
        self.printRow(1)
        self.printRow(0)
        print('    ---------------------')
        print('     A  B  C  D  E  F  G')

    def printRow(self, rowNumber):
        r = str(rowNumber) + ': |'
        for c in self.board[rowNumber]:
            if(c==self.RED):
                r = r + ' r '
            elif (c==self.BLACK):
                r = r + ' b '
            else:
                r = r + '   '
        print(r)

b = Board()
b.initialize()
os.system('cls')

b.printBoard()
winnerExists = False


while not winnerExists:
    b.solicateInput()
    os.system('cls')
    winnerExists = b.checkForWinner()
    if(winnerExists):
        if(winnerExists == b.RED):
            winner = "Red"
        else:
            winner = "Black"
        print(winner + " Wins Congratulations!")
    b.printBoard()
