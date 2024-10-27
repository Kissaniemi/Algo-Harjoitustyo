from copy import deepcopy
import connect


def minmax(board, player, alpha, beta, depth=4):
    """MinMax algorithm, returns best move and its value

    Args:
        board (nested list): gameboard
        player (int): player whose move we are evaluating
        alpha (float/int): alpha value for pruning
        beta (float/int): beta value for pruning
        depth (int, optional): search depth. Defaults to 4.

    """
    columns = connect.possible_columns(player, board)
    if depth == 0 or len(columns) == 0:
        value = connect.score_position(board, player)
        if value == float("-inf"):
            return board, float("-inf")
        if value == float("inf"):
            return board, float("inf")
        if len(columns) == 0:
            return board, 0
        return board, value

    if player == 2:  # Max player
        value = float("-inf")
        best_move = None
        for column in columns:
            new_board = connect.drop_piece(player, deepcopy(board), column)
            _, new_value = minmax(new_board, 1, alpha, beta, depth - 1)
            if new_value > value:
                value = new_value
                best_move = column
            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return best_move, value

    # Min player
    value = float("inf")
    best_move = None
    for column in columns:
        new_board = connect.drop_piece(player, deepcopy(board), column)
        _, new_value = minmax(new_board, 2, alpha, beta, depth - 1)
        if new_value < value:
            value = new_value
            best_move = column
        beta = min(beta, value)
        if beta <= alpha:
            break

    return best_move, value
