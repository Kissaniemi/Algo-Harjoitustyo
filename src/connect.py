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

    # if check_winner(board, row, int(column)-1, player):
     #   print(f"Winner was player {player}!")
     #   ui_start()
    
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
            return (board, -row_count)      # Return row in backwards order
        
    else:
        return (False, board)


ui_start()