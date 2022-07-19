def print_board(board):
    print("Board Printing")

    for row in board:
        print(row)

def check_mark(rowIn, colIn, player):
    if (rowIn > 2 or colIn > 2):
        return False
    elif board[rowIn][colIn] != '-':
        return False
    else:
        return True

def set_mark(rowIn, colIn, player):
    if (player == "Player1"):
        board[rowIn][colIn] = 'X'
    else:
        board[rowIn][colIn] = 'O'


board = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
    ]
counter = 0
player = "-"

print_board(board)
while counter < 9:
    mod = counter % 2

    if mod == 0:
        player = "Player1"
    else:
        player = "Player2"

    #print (counter, player)

    rowIn = int (input(player + " select row: "))
    colIn = int (input(player + " select col: "))

    print (player, " made selection ", rowIn, colIn)

    result = check_mark(rowIn, colIn, player)

    while not check_mark(rowIn, colIn, player):
        print (player, "wrong selection, please try again")
        rowIn = int (input(player + " select row: "))
        colIn = int (input(player + " select col: "))

    set_mark(rowIn, colIn, player)

    counter = counter + 1
    print_board(board)
