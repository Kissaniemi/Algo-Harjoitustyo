import connect

def minmax(board, player, alpha, beta, depth=4):
    """MinMax algorithm (currently without alpha-beta pruning)
    based on the wikipedia pseudocode for minmax algorithm https://en.wikipedia.org/wiki/Minimax, 
    with additions based on the minmax algorithm from https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html (Same code also found elsewhere)
    """

    moves = connect.possible_boards(player, board)
    if not moves:
        return board, 0
    terminal_node = connect.check_full(board)
    opp = 2
    if player == 2:
        opp = 1

    if depth == 0 or terminal_node:
            for i in range(0,7):
                if connect.check_winner(board, i, player):
                    return board, float("-inf") if player == 1 else float("inf")
                if connect.check_winner(board, i, opp):
                    return board, float("inf") if player == 1 else float("-inf")
                
            return board, connect.score_position(board, player)
    
    if player == 2:  # Max player
        value = float("-inf")
        best_move = None
        for move in moves:
            _, new_value = minmax(move[0], 1, alpha, beta, depth -1)
            if new_value > value:
                value = new_value
                best_move = move[1]
            alpha = max(alpha, value)
            if alpha >= beta:
                break

        if best_move == None:
            best_move = move[1]   

        return best_move, value
    
    else: # Min player
        value = float("inf")
        best_move = None
        for move in moves:    
            _, new_value = minmax(move[0], 2, alpha, beta, depth -1)
            if new_value < value:
                value = new_value
                best_move = move[1]
            beta = min(beta, value)
            if beta <= alpha:
                break
        
        if best_move == None:
            best_move = move[1]

        return best_move, value

