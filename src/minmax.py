import connect

def minmax(board, player, depth=4):
    """MinMax algorithm (currently without alpha-beta pruning)
    based on the wikipedia pseudocode for minmax algorithm https://en.wikipedia.org/wiki/Minimax, 
    with additions based on the minmax algorithm from https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html (Same code also found elsewhere)
    """

    moves = connect.possible_boards(player, board)
    terminal_node = connect.check_full(board)

    if depth == 0 or terminal_node:
            return board, connect.score_position(board, player)
    
    if player == 2:  # Max player
        value = float("-inf")
        best_move = None
        for move in moves:
            _, new_value = minmax(move[0], 1, depth -1)
            if new_value > value:
                value = new_value
                best_move = move[1]
        return best_move, value
    
    else: # Min player
        value = float("inf")
        best_move = None
        for move in moves:    
            _, new_value = minmax(move[0], 2, depth -1)
            new_value = -new_value
            if new_value < value:
                value = new_value
                best_move = move[1]

        return best_move, value


