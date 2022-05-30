board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
solution_board = []
pX, pY = 0, 0
possible_moves = []
start = True
signs = {'empty': -1,
         'knight': 'X',
         'visited': '*',
         'possible moves': 'digit 0 - 7'}
moves = [[2, -1], [2, 1],       # North
         [1, 2], [-1, 2],       # East
         [-2, 1], [-2, -1],     # South
         [-1, -2], [1, -2]]     # West
solver_move_counter = 0


def create_board():
    global board
    global solution_board
    x, y = check_input("board")
    board = [[signs['empty']] * x for _ in range(y)]
    solution_board = [[signs['empty']] * x for _ in range(y)]


def check_input(purpose='move'):
    questions = {'board': "Enter your board dimensions:",
                 'start': "Enter the knight's starting position:",
                 'move': "Enter your next move:"}
    answer = input(questions[purpose])
    try:
        pos = answer.split()
        if len(pos) != 2:
            raise ValueError
        x, y = int(pos[0]), int(pos[1])
        if purpose == "start" and not (1 <= y <= len(board) and 1 <= x <= len(board[0])):
            raise ValueError
        elif purpose == "board" and not (x > 0 and y > 0):
            raise ValueError
        elif purpose == 'move' and not((x, y) in possible_moves):
            raise ValueError
        return x, y
    except ValueError:
        if purpose == "board":
            print("Invalid dimensions!")
        elif purpose == "start":
            print("Invalid position!")
        elif purpose == 'move':
            print("Invalid move!", end=' ')
        else:
            print("Some unidentified error appeared. Try again")
        return check_input(purpose)


def move_knight():
    global pX
    global pY
    global possible_moves
    global start
    if start:
        x, y = check_input("start")
        start = False
    else:
        x, y = check_input()
        board[len(board) - pY][pX - 1] = signs['visited']
    pX = x
    pY = y
    board[len(board) - y][x - 1] = signs['knight']
    for point in possible_moves:
        if point[0] == pX and point[1] == pY:
            continue
        board[len(board) - point[1]][point[0] - 1] = signs['empty']
    possible_moves = []


def print_board(b):
    cell_size = len(str(len(b) * len(b[0])))
    row_numbers_size = len(str(len(b)))
    up_down_border = (' ' * row_numbers_size) + ('-' * (len(b[0]) * (cell_size + 1) + 3))
    print(up_down_border)
    for i, x in enumerate(b):
        x = ['_' * cell_size if y == signs['empty'] else ((' ' * (cell_size - len(str(y)))) + str(y)) for y in x]
        fields = " "
        for field in x:
            fields += field + " "
        column_number = (' ' * (row_numbers_size - len(str(len(b) - i)))) + str((len(b) - i))
        row = f"{column_number}|{fields}|"
        print(row)
    print(up_down_border)
    border_numbers = (' ' * row_numbers_size) + "  "
    for i in range(len(b[0])):
        num_mark = ' ' * (cell_size - len(str(i+1))) + str(i+1)
        border_numbers += num_mark + " "
    print(border_numbers)


def next_moves(x, y, depth=1):
    global board
    counter = 0
    for move in moves:
        move_x = x + move[1]
        move_y = y + move[0]
        if 0 < move_x <= len(board[0]) and 0 < move_y <= len(board) and board[len(board) - move_y][move_x - 1] != signs['visited']:
            counter += 1
            if depth > 0:
                possible_moves.append((move_x, move_y))
                board[len(board) - move_y][move_x - 1] = next_moves(move_x, move_y, depth - 1) - 1
    return counter


def start_solving():
    print_board(board)
    while True:
        move_knight()
        if next_moves(pX, pY) == 0:
            moves_done = len([1 for i in board for j in i if j in {signs['knight'], signs['visited']}])
            if moves_done == (len(board) * len(board[0])):
                print_board(board)
                print("What a great tour! Congratulations!")
                break
            else:
                print_board(board)
                print('No more possible moves!')
                print(f"Your knight visited {moves_done} squares!")
                break
        print_board(board)


def check_solutions_loop(x, y, sb):
    global solution_board
    global solver_move_counter
    solver_move_counter += 1
    sb[len(sb) - y][x - 1] = solver_move_counter
    for move in moves:
        move_x = x + move[1]
        move_y = y + move[0]
        if (0 < move_x <= len(sb[0])) and (0 < move_y <= len(sb)) and (sb[len(sb) - move_y][move_x - 1] < 0):
            if check_solutions_loop(move_x, move_y, sb):
                break
    if solver_move_counter == len(sb) * len(sb[0]):
        solution_board = sb
        return True
    else:
        sb[len(sb) - y][x - 1] = -1
        solver_move_counter -= 1
        return False


def menu():
    create_board()
    move_knight()
    next_moves(pX, pY)
    while True:
        response = input("Do you want to try the puzzle? (y/n):")
        if response in {'y', 'n'}:
            check = check_solutions_loop(pX, pY, solution_board)
            if not check:
                print("No solution exists!")
            elif response == 'y':
                start_solving()
            elif response == 'n':
                print("Here's the solution!")
                print_board(solution_board)
            break
        else:
            print("Invalid input!")


if __name__ == '__main__':
    menu()
