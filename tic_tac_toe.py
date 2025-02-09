# -*- coding: utf-8 -*-
"""tic-tac-toe.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vLcWPjfDNRm5bwnO2TtmNGFM3MHerFZI
"""

from typing import List

def printBoard(xState: List[int], zState: List[int]):

    zero = ' '
    one = 'X' if xState[1] else 'O' if zState[1] else 1
    two = 'X' if xState[2] else 'O' if zState[2] else 2
    three = 'X' if xState[3] else 'O' if zState[3] else 3
    four = 'X' if xState[4] else 'O' if zState[4] else 4
    five = 'X' if xState[5] else 'O' if zState[5] else 5
    six = 'X' if xState[6] else 'O' if zState[6] else 6
    seven = 'X' if xState[7] else 'O' if zState[7] else 7
    eight = 'X' if xState[8] else 'O' if zState[8] else 8
    nine = 'X' if xState[9] else 'O' if zState[9] else 9
    print(f"{one} | {two} | {three}")
    print(f"---------")
    print(f"{four} | {five} | {six}")
    print(f"---------")
    print(f"{seven} | {eight} | {nine}")

def checkWin(xState: List[int], zState: List[int]) -> int:

    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win in wins:
        if sum(xState[i] for i in win) == 3:
            print("X Won the match")
            return 1
        if sum(zState[i] for i in win) == 3:
            print("O Won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0] * 10
    zState = [0] * 10
    turn = 1

    print("*Welcome to Tic Tac Toe*")
    while True:
        printBoard(xState, zState)

        if turn == 1:
            print("X's Chance")
        else:
            print("O's Chance")

        value = int(input("Please enter a position (1-9): "))

        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1

        result = checkWin(xState, zState)
        if result != -1:
            printBoard(xState, zState)
            print("Match Over")
            break

        turn = 1 - turn