"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count X's and O's
    count_x = 0
    count_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            if cell == O:
                count_o += 1

    # If X is more than O then it is O's turn
    if count_x > count_o:
        return O
    # If O is more than X then it is X's turn
    elif count_o > count_x:
        return X
    # If board is empty then its X's turn
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(3):
        for cells in range(3):
            if board[row][cells] == EMPTY:
                actions.add((row, cells))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Copy the board to keep the original board immutable
    board_copy = copy.deepcopy(board)

    # check if the action is valid
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Illegal Move")

    # Get current player move
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] or \
       board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If winner
    if winner(board):
        return True

    # If empty
    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == X:
        return 1
    elif result == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check if game has ended
    if terminal(board):
        return None

    # Max or min value depending if it's X or O
    if player(board) == X:
        return minmax_val(board, -1, 1, -1)[1]
    return minmax_val(board, -1, 1, 1)[1]


def minmax_val(board, current_max, current_min, xo_val):
    """
    Returns the move and value that maximize the score
    """

    # Check if game has ended
    if terminal(board):
        return utility(board), None

    # Initialize value and action
    value, action = xo_val, None

    # Return the optimal value and action
    for act in actions(board):
        # Maximize
        if xo_val == -1:
            # Max optimal value
            val = minmax_val(result(board, act),
                             current_max, current_min, 1)[0]
            current_max = max(current_max, val)

            if val >= current_min:
                return val, act

            if val > value:
                value, action = val, act
        # Minimize
        elif xo_val == 1:
            # Min optimal value
            val = minmax_val(result(board, act),
                             current_max, current_min, -1)[0]
            current_min = min(current_min, val)

            if val <= current_max:
                return val, act

            if val < value:
                value, action = val, act

    return value, action
