from copy import deepcopy
from collections import deque
from minmax import minmax


def ui_start():
    """Basic game start ui, "menu"
    """
    board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
    ]

    ai_player = input(
        "Choose if you want to play against AI or not (yes/no): ")
    if ai_player == "yes":
        player = input("Choose if you want to go first or second (1/2): ")
        if player == "2":
            print_board(board)
            print(" ")
            print("AI making move")
            playing_stage(2, board, True, True)
        elif player == "1":
            print_board(board)
            playing_stage(1, board, True, False)

    elif ai_player == "no":
        print("Chose to not play against AI.")
        print_board(board)
        playing_stage(1, board)

    print("Input not accepted, try again.")
    print("")
    ui_start()


def playing_stage(player, board, ai=False, ai_turn=False):
    """Game playing stage ui
    """
    if ai_turn is False:
        print(f"Player {player} turn ")
        column = input("Choose column 1-7 to drop a piece there: ")
        if column == "" or not column.isdigit():
            print("Invalid placement")
            playing_stage(player, board, ai)

        if int(column) > 7 or int(column) < 1:
            print("Invalid placement")
            playing_stage(player, board, ai)

        new_board = drop_piece(player, board, int(column)-1)

        if new_board is False:
            print("Invalid placement")
            playing_stage(player, board, ai)

        print_board(new_board)

        if check_winner(new_board, int(column)-1, player):
            print(f"Winner was player {player}!")
            print(" ")
            ui_start()

        if check_full(new_board):
            print("Board full, no winners!")
            ui_start()

        if ai is False:
            if player == 1:
                playing_stage(2, new_board)
            else:
                playing_stage(1, new_board)
        else:
            playing_stage(2, new_board, True, True)

    else:
        print("AI turn")
        best_move, value = minmax(board, 2, float("-inf"), float("inf"))
        new_board = drop_piece(2, board, best_move)
        print_board(new_board)

        if check_winner(new_board, best_move, 2):
            print("Winner was AI!")
            print(" ")
            ui_start()

        elif check_full(board):
            print("Board full, no winners!")
            ui_start()

        playing_stage(1, new_board, True)


def drop_piece(player, board, column):
    """Changes and returns given column on the board where first move possible, 
    returns False if move not possible
    """
    for row in reversed(board):
        if row[column] == 0:
            row[column] = int(player)
            return deepcopy(board)
    return False


def check_full(board):
    """Checks top row of board to see if board is full,
       (no need to check lower rows, since top row is always last to get filled in game)"""
    for i in board[0]:
        if i == 0:
            return False
    return True


def print_board(board):
    """Prints board on display"""
    print()
    for row in board:
        print_row = deque()
        print_row.append("|")
        for slot in row:
            if slot == 1:
                print_row.append("○")
            elif slot == 2:
                print_row.append("●")
            else:
                print_row.append(" ")
            print_row.append("|")

        print(' '.join(str(x) for x in print_row))
        print("-----------------------------")
    print("  1   2   3   4   5   6   7")


def check_top(board, column):
    """Returns the top row of given column"""
    row_count = -6
    for i in range(0, 6):
        if board[i][column] != 0:
            return row_count
        row_count += 1
    return 0


def check_winner(board, column, player):
    """Checks if the last move was a winning move by calling the winning move check functions, 
    returns True if yes, False if no.
    """
    row = check_top(board, column)

    if check_winner_vertical(board, column, row, player) or \
            check_winner_horizontal_right(board, column, row, player) or \
            check_winner_horizontal_left(board, column, row, player) or \
            check_winner_up_right(board, column, row, player) or \
            check_winner_down_right(board, column, row, player) or \
            check_winner_up_left(board, column, row, player) or \
            check_winner_down_left(board, column, row, player):
        return True
    return False


def check_winner_vertical(board, column, row, player):
    """ Check down vertical ( 0, -1) """
    count = 1
    r = row+1
    c = column

    while board[r][c] == player:
        count += 1
        r += 1
        if count >= 4:
            return True
    return False


def check_winner_horizontal_left(board, column, row, player):
    """ Check left horizontal  ( -1, 0) <- """
    count = 1
    r = row
    c = column-1

    if c+2 <= 6:
        if board[r][c+2] == player:
            count += 1
    while 0 <= c and board[r][c] == player:
        count += 1
        c -= 1
        if count >= 4:
            return True
    return False


def check_winner_horizontal_right(board, column, row, player):
    """ Check right horizontal ( 1, 0) -> """
    count = 1
    r = row
    c = column+1

    if 0 <= c-2:
        if board[r][c-2] == player:
            count += 1
    while c <= 6 and board[r][c] == player:
        count += 1
        c += 1
        if count >= 4:
            return True
    return False


def check_winner_up_right(board, column, row, player):
    """ Check up right diagonal ( 1, 1) ↗ """
    count = 1
    r = row-1
    c = column+1

    if 0 <= c-1 and r+1 <= 0:
        if board[r+2][c-2] == player:
            count += 1
    while c <= 6 and -6 <= r and board[r][c] == player:
        count += 1
        r -= 1
        c += 1
        if count >= 4:
            return True
    return False


def check_winner_down_left(board, column, row, player):
    """  Check down left diagonal ( -1, -1) ↙ """
    count = 1
    r = row+1
    c = column-1

    if c+2 <= 6 and -6 <= r-2:
        if board[r-2][c+2] == player:
            count += 1
    while 0 <= c and r <= 0 and board[r][c] == player:
        count += 1
        r += 1
        c -= 1
        if count >= 4:
            return True
    return False


def check_winner_up_left(board, column, row, player):
    """  Check up left diagonal ( -1, 1) ↖ """
    count = 1
    r = row-1
    c = column-1

    if c+2 <= 6 and r+2 < 0:
        if board[r+2][c+2] == player:
            count += 1
    while 0 <= c and -6 <= r and board[r][c] == player:
        count += 1
        r -= 1
        c -= 1
        if count >= 4:
            return True
    return False


def check_winner_down_right(board, column, row, player):
    """ Check down right diagonal ( 1, -1) ↘"""
    count = 1
    r = row+1
    c = column+1

    if 0 <= c-2 and -6 <= r-2:
        if board[r-2][c-2] == player:
            count += 1
    while c <= 6 and r <= 0 and board[r][c] == player:
        count += 1
        r += 1
        c += 1
        if count >= 4:
            return True
    return False


def score_position(board, player):
    """Board value heuristics, takes sections from boards rows and 
       passes them to the evaluate function
    """
    score = 0

    # Score center column extra
    no_break = 0
    zero = 0
    for i in range(-6, 0):
        if board[i][3] == 0:
            zero += 1
            if zero >= 2 and no_break >= 2:
                score += 500
            if zero >= 3 and no_break >= 1:
                score += 250
        elif board[i][3] == player:
            score += 1000
            no_break += 1
        else:
            if no_break >= 4:
                score = float("inf")
                return score
            score = 0

    # Score horizontal
    for r in range(0, 6):
        score += evaluate(board[r], player)

    # Score vertical
    for c in range(0, 7):
        col = deque()
        for r in range(0, 6):
            col.append(board[r][c])
        score += evaluate(col, player)

    # Score diagonal, down right to top left
    section = deque([board[-3][0], board[-4][1], board[-5][2], board[-6][3]])
    score += evaluate(section, player)

    section = deque([board[-2][0], board[-3][1], board[-4]
                    [2], board[-5][3], board[-6][4]])
    score += evaluate(section, player)

    section = deque([board[-1][0], board[-2][1], board[-3][2],
                    board[-4][3], board[-5][4], board[-6][5]])
    score += evaluate(section, player)

    section = deque([board[-1][1], board[-2][2], board[-3][3],
                    board[-4][4], board[-5][5], board[-6][6]])
    score += evaluate(section, player)

    section = deque([board[-1][2], board[-2][3], board[-3]
                    [4], board[-4][5], board[-5][6]])
    score += evaluate(section, player)

    section = deque([board[-1][3], board[-2][4], board[-3][5], board[-4][6]])
    score += evaluate(section, player)

    # Score diagonal, down left to top right
    section = deque([board[-3][6], board[-4][5], board[-5][4], board[-6][3]])
    score += evaluate(section, player)

    section = deque([board[-2][6], board[-3][5], board[-4]
                    [4], board[-5][3], board[-6][2]])
    score += evaluate(section, player)

    section = deque([board[-1][6], board[-2][5], board[-3][4],
                    board[-4][3], board[-5][2], board[-6][1]])
    score += evaluate(section, player)

    section = deque([board[-1][5], board[-2][4], board[-3][3],
                    board[-4][2], board[-5][1], board[-6][0]])
    score += evaluate(section, player)

    section = deque([board[-1][4], board[-2][3], board[-3]
                    [2], board[-4][1], board[-5][0]])
    score += evaluate(section, player)

    section = deque([board[-1][3], board[-2][2], board[-3][1], board[-4][0]])
    score += evaluate(section, player)

    return score


def evaluate(section, player):
    """Evaluates given section for player vs opponent
    """
    score = 0
    opp = 2
    if player == 2:
        opp = 1

    own_point = 0
    opp_point = 0
    blanks = 0

    for i in section:
        if own_point >= 4:
            return float("inf")

        if opp_point >= 4:
            return float("-inf")

        if i == player:
            own_point += 1
            if opp_point != 0:
                opp_point = 0
                blanks = 0

        if i == opp:
            opp_point += 1
            if own_point != 0:
                own_point = 0
                blanks = 0
        else:
            blanks += 1

    if own_point >= 4:
        return float("inf")
    if own_point == 3:
        score += 100000
    if own_point == 2:
        if blanks > 1:
            score += 150

    if opp_point == 4:
        return float("-inf")
    if opp_point == 3:
        score -= 10000
    if opp_point == 2:
        score -= 150

    return score


def possible_columns(player, board):
    """Generates and returns list of possible columns, uses drop_piece function 
       to evaluate if column is free for a move
    """
    order = deque([3, 2, 4, 1, 5, 0, 6])
    columns = deque()
    for i in order:
        new_board = drop_piece(player, deepcopy(board), i)
        if new_board is not False:
            columns.append(i)
    return columns
