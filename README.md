Tic Tac Toe Game
Overview
  This is a simple implementation of the classic Tic Tac Toe game in Python. 
  The game is played in the console, with two players taking turns to place their marks ('X' or 'O') on a 3x3 grid.
Features:
 >Two-player mode
 >Console-based interface
 >Win condition checks
 >Dynamic board display
How to Run:
 1.Ensure you have Python installed on your system.
 2.Save the provided code in a file named tic_tac_toe.py.
 3.Open a terminal or command prompt.
 4.Navigate to the directory where the file is saved.
 5.Run the game by executing the command:
bash
  Copy this:
  >python tic_tac_toe.py
How to Play:
 >The game starts by displaying the Tic Tac Toe board with numbered positions (1-9).
 >Players take turns entering a position number (1-9) to place their mark ('X' or 'O').
 >The game continues until one player wins or all positions are filled (a draw).
 >The board is updated and displayed after each move.
 >The game ends when a player wins or all positions are filled.
Code Structure:
 >printBoard(xState, zState): Prints the current state of the Tic Tac Toe board.
 >checkWin(xState, zState): Checks if either player has won the game.
 >main loop: Manages the game flow, including player turns and win condition checks.
Example Gameplay:

*Welcome to Tic Tac Toe*
 1 | 2 | 3
---------
 4 | 5 | 6
---------
 7 | 8 | 9
X's Chance
Please enter a position (1-9): 1
X | 2 | 3
---------
 4 | 5 | 6
---------
 7 | 8 | 9
O's Chance
Please enter a position (1-9): 2
X | O | 3
---------
 4 | 5 | 6
---------
 7 | 8 | 9
...
Known Issues:
 >The game does not handle invalid inputs (e.g., entering a non-numeric value or a position already occupied).
 >The game does not check for a draw condition (all positions filled with no winner).
Future Enhancements:
  =>Add input validation to handle invalid inputs.
  =>Implement a draw condition check.
  =>Add a single-player mode with an AI opponent.
