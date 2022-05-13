# methods for printing game states
def imp():
    print("Impossible")


def gnf():
    print("Game not finished")


def draw():
    print("Draw")


def wins(winner):
    print(f"{winner} wins")


# method of checking winning states
def win_state(s):
    imp_winner = []
    if s[0][0] == s[0][1] == s[0][2] != "_":
        imp_winner.append(s[0][0])
    if s[1][0] == s[1][1] == s[1][2] != "_":
        imp_winner.append(s[1][0])
    if s[2][0] == s[2][1] == s[2][2] != "_":
        imp_winner.append(s[2][0])
    if s[0][0] == s[1][0] == s[2][0] != "_":
        imp_winner.append(s[0][0])
    if s[0][1] == s[1][1] == s[2][1] != "_":
        imp_winner.append(s[0][1])
    if s[0][2] == s[1][2] == s[2][2] != "_":
        imp_winner.append(s[0][2])
    if s[0][0] == s[1][1] == s[2][2] == s[0][2] == s[2][0] != "_":
        imp_winner.append(s[0][0])
    elif s[0][0] == s[1][1] == s[2][2] != "_":
        imp_winner.append(s[0][0])
    elif s[0][2] == s[1][1] == s[2][0] != "_":
        imp_winner.append(s[0][2])
    return imp_winner


# method of player's move (inputting coordinates by player 'player' ['X' or 'O'])
def player_move(board, player):
    while True:
        move_x = input("Enter the coordinates:").split()
        # print(move_x)
        # if ((not x.isnumeric()) for x in move_x):
        if len(move_x) != 2:
            print("You should enter exactly two numbers separated by one whitespace")
            continue
        if not(move_x[0].isnumeric() and move_x[1].isnumeric()):
            print("You should enter numbers")
            continue
        move_x = [int(x) for x in move_x]
        if not(1 <= move_x[0] <= 3 and 1 <= move_x[1] <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        elif board[move_x[0]-1][move_x[1]-1] in ['X', 'O']:
            print("This cell is occupied! Choose another one!")
            continue
        else:
            board[move_x[0]-1][move_x[1]-1] = player
            break
    return board


def print_board(board):
    print(f"""
    ---------
    | {board[0][0]} {board[0][1]} {board[0][2]} |
    | {board[1][0]} {board[1][1]} {board[1][2]} |
    | {board[2][0]} {board[2][1]} {board[2][2]} |
    ---------
    """)
