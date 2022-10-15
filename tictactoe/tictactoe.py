"""
Tic Tac Toe Player
"""

import math
import copy # pour copier le plateau

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
    nbX=0
    nbO=0

    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j]==X:
                nbX +=1
            elif board[i][j]==O:
                nbO +=1

    if nbX>nbO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_Actions=set()   # store all possibles actions inside
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if (board[i][j]==EMPTY):      # if the box is empty, we can add this action
                possible_Actions.add((i,j))

    return possible_Actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board) # create a new board (copy)
    result[action[0]][action[1]]=player(board) # we add the symbol of the player
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # we check : rows columns diagonals
    # 3 rows
    # nb 0
    if all(i==board[0][0] for i in board[0]): 
        return board[0][0] ## either X or O
    # nb 1
    elif all(i ==board[1][0] for i in board[1]):
        return board[1][0] # either X or O
    # nb 2
    elif all(i ==board[2][0] for i in board[2]):
        return board[2][0] # either X or O
    
    # 3 colum,s
    # nb 0
    elif board[0][0] ==board[1][0] and board[1][0] ==board[2][0]:
        return board[0][0] # either X or O
    # nb 1
    elif board[0][1] ==board[1][1] and board[1][1] ==board[2][1]:
        return board[0][1] # either X or O
    # nb 2
    elif board[0][2] ==board[1][2] and board[1][2] ==board[2][2]:
        return board[0][2] # either X or O
    # 2 diagonals
    # first one
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    # second
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    # no winner 
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # we check if there is a winner or there is space left on the board
    if(winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None)):
        return True # game is over
    else:
        return False # game is still in progress


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        # win X
        if winner(board) == X:
            return 1
        # win 0
        elif winner(board) == O:
            return -1
        # game tie
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        # max
        if player(board) == X:
            value, move = max_value(board)
            return move
        # min
        else:
            value, move = min_value(board)
            return move

# For the minimax, we must determine the min and max value
def min_value(board):

    if terminal(board):  # if game is over
        return utility(board), None

    val_min = float  ('inf') # represents infinity (math.inf)
    optimal_action_min = None

    for action in actions(board):
        test_max, action_max = max_value(result(board, action))
        if test_max < val_min:
            val_min = test_max
            optimal_action_min = action

            if val_min == -1:
                return val_min, optimal_action_min
    return val_min, optimal_action_min


def max_value(board):

    if terminal(board): # if game is over
        return utility(board), None

    val_max = float('-inf') # represents infinity.
    optimal_action = None # we are looking for that

    for action in actions(board):
        test_min, action_min = min_value(result(board, action))
        if test_min > val_max:
            val_max = test_min
            optimal_action = action
            
            if val_max == 1:
                return val_max, optimal_action
    return val_max, optimal_action



    

