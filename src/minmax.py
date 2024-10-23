import connect
from copy import deepcopy

def minmax(board, player, alpha, beta, depth=4):
    """MinMax algorithm (currently without alpha-beta pruning)
    based on the wikipedia pseudocode for minmax algorithm https://en.wikipedia.org/wiki/Minimax, 
    with additions based on the minmax algorithm from https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html (Same code also found elsewhere)
    """

    columns = connect.possible_columns(player, board)
    if len(columns) < 2:
        columns = connect.preferred_order(columns)

    if not columns:
        return board, 0
    
    terminal_node = connect.check_full(board)
    opp = 2
    if player == 2:
        opp = 1

    if depth == 0 or terminal_node:
            for i in range(0,7):
                if connect.check_winner(board, i, player):
                    return board, float("-inf") if player == 1 else float("inf")
                elif connect.check_winner(board, i, opp):
                    return board, float("inf") if player == 1 else float("-inf")
                
            return board, connect.score_position(board, player)
    
    if player == 2:  # Max player
        value = float("-inf")
        best_move = columns[0]
        for column in columns:
            new_board = connect.drop_piece(player, deepcopy(board), column)
            _, new_value = minmax(new_board, 1, alpha, beta, depth -1)
            if new_value > value:
                value = new_value
                best_move = column
            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return best_move, value
    
    else: # Min player
        value = float("inf")
        best_move = columns[0]
        for column in columns:   
            new_board = connect.drop_piece(player, deepcopy(board), column)
            _, new_value = minmax(new_board, 2, alpha, beta, depth -1)
            if new_value < value:
                value = new_value
                best_move = column
            beta = min(beta, value)
            if beta <= alpha:
                break
        
        return best_move, value
