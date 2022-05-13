import ttt_methods as ttt

# create empty board
f = [['_', '_', '_'],
     ['_', '_', '_'],
     ['_', '_', '_']]
# show board at the beginning of game
ttt.print_board(f)

turn = 0
player = None
# ### game starts, always by turn of player X
while True:
    f = ttt.player_move(f, "X" if not(turn % 2) else "O")
    turn += 1
    # show board with current state after player moved
    ttt.print_board(f)
    # check current state of game
    winn = ttt.win_state(f)
    if len(winn) > 1:
        ttt.imp()
        break
    elif winn and winn[0] in ['X', 'O']:
        ttt.wins(winn[0])
        break
    elif '_' not in [y for x in f for y in x]:
        ttt.draw()
        break
