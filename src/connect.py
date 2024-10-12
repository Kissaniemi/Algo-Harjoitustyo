
from minmax import minmax
from copy import deepcopy

def ui_start():
    board =[[0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]
    
    ai_player = input("Choose if you want to play against AI or not (yes/no): ")
    if ai_player == "yes":
        player = input("Choose if you want to go first or second (1/2): ")
        if int(player) == 2:
            playing_stage(player, board, True, True)
        else:
            print_board(board)
            playing_stage(player, board, True, False)
        
    elif ai_player == "no":
        print("Chose to not play against AI")
        player = input("Choose player 1 or player 2 by writing '1' or '2' : ")
        if player == "1" or player == "2":
            print(f"{player} chosen")  
            print_board(board)
            playing_stage(player, board)
            
        else:
            print("Invalid player")
            ui_start()

    else:
        print("Input not accepted, try again.")
        print("")
        ui_start()


def playing_stage(player, board, ai=False, ai_turn=False):

    if ai_turn == False:
        print(f"Player {player} turn ")
        column = input("Choose column 1-7 to drop a piece there: ")
        if column == "" or not column.isdigit():
            print("Invalid placement") 
            playing_stage(player, board)
        
        if int(column) > 7 or int(column) < 1:
            print("Invalid placement") 
            playing_stage(player, board)
    
        new_board, rtn_col = drop_piece(int(player), board, int(column))
        
        if new_board == False:
            print("Invalid placement")
            playing_stage(player, board)
        
        print_board(new_board)

        if check_winner(board, int(column)-1, player):
            print(f"Winner was player {player}!")
            print(" ")
            ui_start()
        
        if check_full(board):
            print(f"Board full, no winners!")
            ui_start()
         
        if ai == False:
            if int(player) == 1:
                playing_stage(2, new_board)
            else:
                playing_stage(1, new_board)
        else:
            if int(player) == 1:
                playing_stage(2, new_board, True, True)
            else:
                playing_stage(1, new_board, True, True)

    else:

        best_move, value = minmax(board, player, float("-inf"), float("inf"))
     
        new_board, column = drop_piece(player, board, best_move+1)

        print_board(new_board)

        if check_winner(board, column, player):
            print(f"Winner was player {player}!")
            print(" ")
            ui_start()
        
        if check_full(board):
            print(f"Board full, no winners!")
            ui_start()
         

        if int(player) == 1:
            playing_stage(2, new_board, True)
        else:
            playing_stage(1, new_board, True)


def possible_boards(player, board):
    boards = []
    for i in range(1,8):
        new_board, column = drop_piece(player, deepcopy(board), i)
        if new_board != False:
            boards.append((new_board, column))
    return boards


def drop_piece(player, board, column):
    
    for row in reversed(board):
        if row[column-1] == 0:
            row[column-1] = int(player)
            return deepcopy(board), column-1 # Return row in backwards order
    else:
        return False, None
    

def check_full(board):
    for i in board[0]:
        if i == 0:
            return False
    return True


def print_board(board):
    print( )
    for row in board:
        print(row)
    print(" 1  2  3  4  5  6  7")


def check_top(board, column):
    row_count = -6
    for i in range(0,5):
        if board[i][column] != 0:
            return row_count
        row_count += 1
    return False


def check_winner(board, column, player):
    directions = (
                        ( -1, 1),             ( 1, 1),
                        ( -1, 0),             ( 1, 0),
                        ( -1, -1), ( 0, -1),  ( 1, -1),
                    )   # No need to check up directions since the last added piece is always on top

    row = check_top(board, column)
    
    if row:
        for dc, dr in directions:
            count = 0
            r = row+dr
            c = column+dc

            if -6 <= r < 0 and 0 <= c < 7:
                # Check down vertical ( 0, -1)  
                if r == row-1 and c == column:
                    count = 0
                    while -6 <= r and board[r+1][c] == player and r+1 < 0:
                        count += 1
                        r += 1
                
                # Check left horizontal  <- ( -1, 0)
                elif r == row and c == column-1:
                    count = 0
                    if c+1 < 7:
                        if board[r][c+1] == player:
                            count += 1
                            if c+2 < 7:
                                if board[r][c+2] == player:
                                    count += 1

                    while 0 <= c and board[r][c] == player:
                        count += 1
                        c -= 1


                # Check right horizontal -> ( 1, 0)
                elif r == row and c == column+1:
                    count = 0
                    if 0 < c-1:
                        if board[r][c-1] == player:
                            count += 1
                            if 0 < c-2:
                                if board[r][c-2] == player:
                                    count += 1

                    while c <= 6 and board[r][c] == player:
                        count += 1
                        c += 1


                # Check up right diagonal ( 1, 1)
                elif r == row-1 and c == column+1:
                    count = 1
                    if 0 < c-2 and r+2 < 0:
                        if board[r+2][c-2] == player:
                            count += 1
                            if 0 < c-3 and r+3 < 0:
                                if board[r+3][c-3] == player:
                                    count += 1

                    while c <= 6 and -6 <= r and board[r][c] == player:
                        count +=1
                        r -= 1
                        c += 1
                        if c > 6 and -6 > r:
                            break
                    
                # Check up left diagonal ( -1, 1)
                elif r == row-1 and c == column-1:
                    count = 1
                    if c+2 < 7 and r+2 < 0:
                        if board[r+2][c+2] == player:
                            count += 1
                            if c+3 < 7 and r+3 < 0:
                                if board[r+3][c+3] == player:
                                    count += 1

                    while c <= 6 and -6 <= r and board[r][c] == player:
                        count +=1
                        r -= 1
                        c -= 1
                        if c > 6 and -6 > r:
                            break

                # Check down right diagonal ( 1, -1)
                elif r == row+1 and c == column+1:
                    count = 0
                    if 0 < c-2 and -6 < r-2:
                        if board[r-2][c-2] == player:
                            count += 1
                            if 0 < c-3 and -6 < r-3:
                                if board[r-3][c-3] == player:
                                    count += 1

                    while c <= 6 and -6 <= r and board[r][c] == player:
                        count +=1
                        r += 1
                        c += 1
                        if c > 6 and -6 > r:
                            break


                # Check down left diagonal ( -1, -1)
                elif r == row+1 and c == column-1:
                    count = 1
                    if c+2 < 7 and -6 < r-2:
                        if board[r-2][c+2] == player:
                            count += 1
                            if c+3 < 7 and -6 < r-3:
                                if board[r-3][c+3] == player:
                                    count += 1

                    while c <= 6 and -6 <= r and board[r][c] == player:             
                        count +=1
                        r += 1
                        c -= 1
                        if c > 6 and -6 > r:
                            break

                if count >= 4:
                    return True
        return False 


def score_position(board, player):
        score = 0

        # Score center column 3
        no_break = 0
        for i in range(-5,0):
            if board[i][3] == 0:
                score += 100
            elif board[i][3] == player:
                score += 100
                no_break += 1
            else:
                no_break = 0

        score += no_break * 4


        # Score horizontal
        for r in range(6):
            row = []
            for i in range(7):
                row.append(board[r][i])
            for c in range(7-3):
                crow = row[c:c+4]
                score += evaluate(crow, player)
        
        # Score vertical
        for c in range(7):
            col = []
            for i in range(6):
                col.append(board[i][c])
            for r in range(6-3):
                crow = col[r:r+4]
                score += evaluate(crow, player)

        # Score diagonal
        for r in range(6-3):
            for c in range(7-3):
                crow = [board[r+i][c+i] for i in range(4)]
                score += evaluate(crow, player)

        for r in range(6-3):
            for c in range(7-3):
                crow = [board[r+3-i][c+i] for i in range(4)]
                score += evaluate(crow, player)
        
        #print(score)
         
        return score


def evaluate(row, player):
    score = 0
    opp = 2
    if player == 2:
        opp = 1
    
    no_break = 0
    opp_point = 0
    blanks = 0
    between = False
    for i in range(len(row)):
        if row[i] == player:
            no_break += 1
            opp_point = 0
        if row[i] == opp:
            no_break = 0
            opp_point += 1
            blanks = 0
            between = False
        else:
            blanks += 1
            if opp_point == 0:
                between = True

    if no_break == 4:
        score += 10000
    if no_break == 3:
        score += 10
        if between == True:
            score += 1000       
    if no_break == 2:
        if blanks > 1:
            score += 5

    if opp_point == 4:
        score -= 10000
    if opp_point == 3:
        score -= 10
    if opp_point == 2:
        score -= 5

    return score

