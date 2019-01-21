#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *
from Minimax import *

def oneMoveGame(currentGame,depth):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)
    tree = Minimax(currentGame, depth)
    move = tree.Decision()
    result = currentGame.playPiece(move)
    gameState(currentGame, move)
    currentGame.gameFile.close()

def gameState(currentGame, move):
    print('\n\nMove count %d: Turn %d: column %d\n' % (currentGame.pieceCount, currentGame.currentTurn, move+1))
    if currentGame.currentTurn == 1:
        currentGame.currentTurn = 2
    elif currentGame.currentTurn == 2:
        currentGame.currentTurn = 1
    print 'Current Game state:'
    currentGame.printGameBoard()
    currentGame.countScore()
    print('Score: User = %d, Computer = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    currentGame.printGameBoardToFile()

def interactiveGame(currentGame, depth):
    while currentGame.pieceCount != 42:
        if currentGame.currentTurn == 1:
            nextMove = input("Enter the column between [1-7] where you want to insert your next coin : ")
            if not currentGame.playPiece(nextMove-1):
                print "This column is full!"
                continue
            if nextMove < 1 or nextMove > 7:
                print "Enter a column between [1-7]!"
            currentGame.gameFile = open("Human.txt", 'w')
            gameState(currentGame, nextMove-1)
        elif currentGame.pieceCount != 42:
            minimaxTree = Minimax(currentGame, depth)
            move = minimaxTree.Decision()
            result = currentGame.playPiece(move)
            currentGame.gameFile = open("Computer.txt", 'w')
            gameState(currentGame, move)
    currentGame.gameFile.close()
    if currentGame.player1Score > currentGame.player2Score:
        print "User won"
    elif currentGame.player2Score > currentGame.player1Score:
        print "Computer won"
    else:
        print "Game Drawn"

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        if argv[3] == 'computer-next': #override current turn according to commandline arguments
            currentGame.currentTurn = 2
        else: #human-next
            currentGame.currentTurn = 1
        interactiveGame(currentGame,argv[4]) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,argv[4]) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



