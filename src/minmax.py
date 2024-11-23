from copy import deepcopy
import connect

column_order = [3, 2, 4, 1, 5, 0, 6]  # preferred order of columns to make a move

def minmax(board, player, last_move, alpha, beta, depth=6):
    """MinMax algorithm, returns best move and its value

    Args:
        board (nested list): gameboard
        player (int): player whose move we are evaluating
        alpha (float/int): alpha value for pruning
        beta (float/int): beta value for pruning
        depth (int, optional): search depth. Defaults to 6.

    """

    if last_move is not None:
        if player == 1:
            if connect.check_winner(board, last_move, 2) is True:
                return last_move, 10000     
        else:
            if connect.check_winner(board, last_move, 1) is True:
                return last_move, -10000

    columns = connect.possible_columns(board, column_order)

    if depth == 0 or len(columns) == 0:
        value = connect.score_position(board, player)
        if len(columns) == 0:
            return last_move, 0
        return last_move, value

    if player == 2:  # Max player
        value = -100000
        best_move = None
        for column in columns:  
            new_board = connect.drop_piece(player, deepcopy(board), column)
            _, new_value = minmax(new_board, 1, column, alpha, beta, depth - 1)
            if new_value > value:
                value = new_value
                best_move = column
            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return best_move, value

    # Min player
    value = 100000
    best_move = None
    for column in columns: 
        new_board = connect.drop_piece(player, deepcopy(board), column)
        _, new_value = minmax(new_board, 2, column, alpha, beta, depth - 1)
        if new_value < value:
            value = new_value
            best_move = column
        beta = min(beta, value)
        if beta <= alpha:
            break

    return best_move, value

