def ui_start():
    player = input("Choose player 1 or player 2 by writing 1 or 2: ")
    if player == "1" or player == "2":
        print(f"{player} chosen")
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0]]
        print_board(board)
        playing_stage(player, board)
        
    else:
        print("Invalid player")
        ui_start()

def playing_stage(player, board):
    print(f"Player {player} turn ")
    column = input("Choose column 1-7 to drop a piece there: ")
    if column == "" or not column.isdigit():
        print("Invalid placement") 
        playing_stage(player, board)
    
    if int(column) > 7 or int(column) < 1:
        print("Invalid placement") 
        playing_stage(player, board)
   
    new_board = drop_piece(int(player), board, int(column))
    
    if new_board[0] == False:
        print("Invalid placement")
        playing_stage(player, board)
    
    print_board(new_board[0])
    row = new_board[1]

    if check_winner(board, row, int(column)-1, player):
        print(f"Winner was player {player}!")
        print(" ")
        ui_start()
    
    if check_full(board):
        print(f"Board full, no winners!")
        ui_start()

    if int(player) == 1:
        playing_stage(2, new_board[0])
    else:
        playing_stage(1, new_board[0])
        
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

def drop_piece(player, board, column):
    row_count = 0
    for row in reversed(board):
        row_count += 1
        if row[column-1] == 0:
            row[column-1] = player
            return (board, -row_count) # Return row in backwards order
        
    else:
        return (False, board)

def check_winner(board, row, column, player):
    directions = (
                        ( -1, 1),             ( 1, 1),
                        ( -1, 0),             ( 1, 0),
                        ( -1, -1), ( 0, -1),  ( 1, -1),
                    )   # No need to check up directions since the last added piece is always on top
 
    for dc, dr in directions:
        count = 0
        r = row+dr
        c = column+dc

        if -6 <= r < 0 and 0 <= c < 7:
            # Check down vertical ( 0, -1)  
            if r == row-1 and c == column:
                count = 0
                while -6 <= r and board[r+1][c] == player:
                    count += 1
                    r += 1
            
            # Check left horizontal  <- ( -1, 0)
            elif r == row and c == column-1:
                count = 0
                if board[r][c+1] == player:
                    count += 1
                    if board[r][c+2] == player:
                        count += 1

                while 0 <= c and board[r][c] == player:
                    count += 1
                    c -= 1

            # Check right horizontal -> ( 1, 0)
            elif r == row and c == column+1:
                count = 0
                if board[r][c-1] == player:
                    count += 1
                    if board[r][c-2] == player:
                        count += 1

                while c <= 6 and board[r][c] == player:
                    count += 1
                    c += 1

            # Check up right diagonal ( 1, 1)
            elif r == row-1 and c == column+1:
                count = 1
                if board[r+2][c-2] == player:
                    count += 1
                    if board[r+3][c-3] == player:
                        count += 1
                
                while c <= 6 and -6 <= r and board[r][c] == player:
                    count +=1
                    r -= 1
                    c += 1
                
            # Check up left diagonal ( -1, 1)
            elif r == row-1 and c == column-1:
                count = 1
                if board[r+2][c+2] == player:
                    count += 1
                    if board[r+3][c+3] == player:
                        count += 1
                        
                while c <= 6 and -6 <= r and board[r][c] == player:
                    count +=1
                    r -= 1
                    c -= 1

            # Check down right diagonal ( 1, -1)
            elif r == row+1 and c == column+1:
                count = 1
                if board[r-2][c-2] == player:
                    count += 1
                    if board[r-3][c-3] == player:
                        count += 1

                while c <= 6 and -6 <= r and board[r][c] == player:
                    count +=1
                    r += 1
                    c += 1

            # Check down left diagonal ( -1, -1)
            elif r == row+1 and c == column-1:
                count = 1
                if board[r-2][c+2] == player:
                    count += 1
                    if board[r-3][c+3] == player:
                        count += 1

                while c <= 6 and -6 <= r and board[r][c] == player:
                    count +=1
                    r += 1
                    c -= 1

            if count >= 4:
                return True

    return False 


