NAME: HEERA SRIDHAR
UTA ID: 1001529609
PROGRAMMING LANGUAGE: Python

DESCRIPTION:
The program has been implemented using depth limt and alpha-beta Pruning.

CODE STRUCTURE:

The class Minimax performs the decision making and contains Implementing alpha-beta pruning,depth-limited version of minimax.

The Minimax contains the following methods:

1.Decision() which returns Minimax's decision.
2.maximum() which performs maximizing operations.
3.minimum() which perfoms minimizing operations. 
4.nextTurn() which returns the utility/score that needs to be maximized or minimized.
5.result() calculates the new state after a move.
6.availableMoves() returns the moves that canbe done on a state.

HOW TO RUN AND EXECUTE:

To run the code, execute maxconnect4.py with the following:

1. For interactive mode:
   python maxconnect4.py interactive [input_file] [computer-next/human-next]    [depth]
   eg: python maxconnect4.py interactive input1.txt computer-next 10

2. one-move mode:
    python maxconnect4.py one-move [input_file] [output_file] [depth]
    eg: python maxconnect4.py one-move input2.txt output1.txt 10

3. For measuring the execution time, type the following:
    eg: time python maxconnect4.py one-move input2.txt output1.txt 10

REFERENCES:
1.https://omega.uta.edu/~gopikrishnav/classes/common/4308_5360/slides/alpha_beta.pdf.