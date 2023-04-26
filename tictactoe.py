"""
Tic Tac Toe Player
"""
import copy
import math

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
    x_player_counter = 0
    o_player_counter = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == 'X':
                x_player_counter += 1
            elif board[i][j] == 'O':
                o_player_counter += 1

    if x_player_counter > o_player_counter:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Invalid action!')

    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return X
            elif board[i][0] == 'O':
                return O
            else:
                return None

    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return X
            elif board[0][i] == 'O':
                return O
            else:
                return None

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return X
        elif board[0][0] == 'O':
            return O
        else:
            return None

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return X
        elif board[0][2] == 'O':
            return O
        else:
            return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not None in board[0] and not None in board[1] and not None in board[2]):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
