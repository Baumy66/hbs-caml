import connect4
import players

# Input
blackPlayer = players.FirstColumnAvailable()
redPlayer = players.IfMovesWinsDoItElseRandom()
gamesToTest = 1000

blackWins = 0
redWins = 0
gamesPlayed = 0
while gamesPlayed < gamesToTest:
    winner = False
    board = connect4.Board()
    board.initialize()
    while not winner:
        if(board.turn == board.BLACK):
            currentPlayer = blackPlayer
        else:
            currentPlayer = redPlayer
        move = currentPlayer.chooseMove(board.board, board.turn)
        board.makeMove(move)
        #board.printBoard()
        winner = board.checkForWinner()
        if(winner):
            break
    if(winner == board.RED):
        redWins = redWins + 1
    elif(winner == board.BLACK):
        blackWins = blackWins + 1
    gamesPlayed = gamesPlayed + 1
    #board.printBoard()

print("Testing Complete")
print("Red Wins: " + str(redWins))
print("Black Wins: " + str(blackWins))