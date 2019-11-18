import random
import copy
import connect4

class Player():
    def __init__(self):
        pass
    
    def chooseMove(board, player):
        pass

class RandomDecisionPlayer(Player):
    def chooseMove(self, board, player):
        while True:
            move = random.randint(0,6)
            if(board[5][move]==0):
                return move


class FirstColumnAvailable(Player):
    def chooseMove(self, board, player):
        if(board[5][0]==0):
            return 0
        if(board[5][1]==0):
            return 1
        if(board[5][2]==0):
            return 2
        if(board[5][3]==0):
            return 3
        if(board[5][4]==0):
            return 4
        if(board[5][5]==0):
            return 5
        if(board[5][6]==0):
            return 6


class IfMovesWinsDoItElseRandom(Player):
    def __init__(self):
        pass

    def chooseMove(self, board, player):
        col = 0
        while col < 7:
            if(board[5][col]!=0):
                col = col + 1
                continue
            b = connect4.Board()
            b.board = copy.deepcopy(board)
            b.turn = player
            b.makeMove(col)
            if(b.checkForWinner() == player):
                return col
            col = col + 1
        while True:
            move = random.randint(0,6)
            if(board[5][move]==0):
                return move