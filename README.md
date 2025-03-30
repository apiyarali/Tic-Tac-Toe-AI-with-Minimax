# Tic-Tac-Toe AI with Minimax

This project implements an AI for playing Tic-Tac-Toe optimally using the Minimax algorithm. The AI ensures that it never loses, making the game either a win for the AI or a tie if played optimally.

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. Additionally, install the required package by running:

```sh
pip3 install -r requirements.txt
```

### Installation & Setup

Clone the repository.

## Project Structure
- `runner.py`: Handles the graphical interface and game execution.
- `tictactoe.py`: Contains the core logic, including the Minimax implementation.

## How to Play
Run the game using:

```sh
python runner.py
```

You will be able to play against the AI, which will always make the optimal move.

## Function Overview

### 1. `player(board)`
- Determines which player's turn it is (`X` or `O`).
- The game starts with `X`, then alternates each turn.

### 2. `actions(board)`
- Returns a set of possible moves as tuples `(i, j)` where `i` and `j` are row and column indices.
- Only empty cells are valid moves.

### 3. `result(board, action)`
- Returns a new board state after making a move.
- The function does not modify the original board.
- Raises an exception if the move is invalid.

### 4. `winner(board)`
- Checks for a winner (`X` or `O`).
- Returns `None` if no player has won.

### 5. `terminal(board)`
- Returns `True` if the game is over (win or tie), otherwise `False`.

### 6. `utility(board)`
- Returns `1` if `X` wins, `-1` if `O` wins, `0` for a tie.

### 7. `minimax(board)`
- Returns the optimal move `(i, j)` for the current player.
- If multiple optimal moves exist, any one of them is acceptable.
- Returns `None` if the game is over.

## Additional Information
- Individual functions can be tested by importing them:
  ```python
  from tictactoe import initial_state
  ```
## Expected Behavior
The AI plays optimally and will never lose. The best outcome a human player can achieve is a draw if they also play optimally.

## License
This project is for educational purposes and follows Harvard's CS80 AI curriculum.

## Acknowledgments
- CS80 AI Course for project inspiration.
