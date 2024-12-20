import connect
import time

# preferred order of columns to make a move to
column_order = [3, 2, 4, 1, 5, 6, 0]


def iterative_deepening(board, player, last_move, alpha, beta):
    start_time = time.time()
    time_limit = 2
    # Maximum depth deepening could (potentially) reach if it had enough time
    depth_limit = 43

    for max_depth in range(1, depth_limit):
        best_move, value = minmax(
            board, player, last_move, alpha, beta, max_depth, 0)

        if time.time() - start_time > time_limit or value == 10000:
            break

    print(f"approximate time taken for move: {time.time() - start_time }")
    print(f"depth reached: {max_depth}")
    print(f"move made to column: {best_move}, move value: {value}")

    return best_move, value


def minmax(board, player, last_move, alpha, beta, max_depth, current_depth):
    """MinMax algorithm, returns best move and its value

    Args:
        board (nested list): gameboard
        player (int): player whose move we are evaluating
        last move (int): the last move made by the other player
        alpha (float/int): alpha value for pruning
        beta (float/int): beta value for pruning
        max_depth (int): depth limit (most likely never reached)
        current_depth: current depth we are on
    """

    if last_move is not None:
        if player == 1:
            if connect.check_winner(board, last_move, 2):
                return last_move, 10000
        else:
            if connect.check_winner(board, last_move, 1):
                return last_move, -10000

    columns = connect.possible_columns(board, column_order)

    if current_depth == max_depth or len(columns) == 0:
        if len(columns) == 0:
            return last_move, 0
        value = connect.score_position(board, player)
        return last_move, value

    # Max player
    if player == 2:
        value = -100000
        best_move = None
        for column in columns:
            row = connect.check_top(board, column)
            board[row-1][column] = 2
            _, new_value = minmax(board, 1, column, alpha,
                                  beta, max_depth, current_depth + 1)
            board[row-1][column] = 0

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
        row = connect.check_top(board, column)
        board[row-1][column] = 1
        _, new_value = minmax(board, 2, column, alpha,
                              beta, max_depth, current_depth + 1)
        board[row-1][column] = 0

        if new_value < value:
            value = new_value
            best_move = column
        beta = min(beta, value)
        if beta <= alpha:
            break

    return best_move, value
