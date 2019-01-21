from MaxConnect4Game import *
import copy


class Minimax:
    def __init__(self, game, depth):
        self.currentTurn = game.currentTurn
        self.game = game
        self.maxDepth = int(depth)

    def Decision(self):
        x = float("inf")
        y = float("-inf")
        mini = []
        moves = availableMoves(self.game.gameBoard)
        for move in moves:
            res = result(self.game, move)
            mini.append(self.minimum(res, x, y))
        final = moves[mini.index(max(mini))]
        return final

    def minimum(self, state, alpha, beta):
        if state.pieceCount == 42 or state.nodeDepth == self.maxDepth:
            return self.nextTurn(state)
        prune = float("inf")
        for move in availableMoves(state.gameBoard):
            newState = result(state, move)
            prune = min(prune, self.maximum(newState, alpha, beta))
            if prune <= alpha:
                return prune
            beta = min(beta, prune)
        return prune

    def maximum(self, state, alpha, beta):
        if state.nodeDepth == self.maxDepth or state.pieceCount == 42:
            return self.nextTurn(state)
        prune = float("-inf")
        for move in availableMoves(state.gameBoard):
            newState = result(state, move)
            prune = max(prune, self.minimum(newState, alpha, beta))
            if prune >= beta:
                return prune
            alpha = max(alpha, prune)
        return prune

    def nextTurn(self, state):
        if self.currentTurn == 1:
            score = state.player1Score * 2 - state.player2Score
        elif self.currentTurn == 2:
            score = state.player2Score * 2 - state.player1Score
        return score

def availableMoves(board):
    available = []
    for col, colVal in enumerate(board[0]):
        if colVal == 0:
            available.append(col)
    return available

def result(oldGame, column):
    game = maxConnect4Game()
    try:
        game.nodeDepth = oldGame.nodeDepth + 1
    except AttributeError:
        game.nodeDepth = 1
    game.pieceCount = oldGame.pieceCount
    game.gameBoard = copy.deepcopy(oldGame.gameBoard)
    if not game.gameBoard[0][column]:
        for i in range(5, -1, -1):
            if not game.gameBoard[i][column]:
                game.gameBoard[i][column] = oldGame.currentTurn
                game.pieceCount += 1
                break
    if oldGame.currentTurn == 1:
        game.currentTurn = 2
    elif oldGame.currentTurn == 2:
        game.currentTurn = 1
    game.checkPieceCount()
    game.countScore()
    return game



