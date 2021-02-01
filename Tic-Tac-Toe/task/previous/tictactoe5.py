from typing import List

size = 3
size_range = range(size)
Cells = List[List[str]]
cells: Cells = [[*' ' * size] for _ in size_range]
moves = 0
crd_prompt = 'Enter the coordinates: '
dashes, pipe = '-' * 9, '|',
players = ['X', 'O']
player = players[0]
er_not_num = 'You should enter numbers!'
er_not_in_range = 'Coordinates should be from 1 to 3!'
er_occupied = 'This cell is occupied! Choose another one!'
is_in_range = lambda v: v in size_range


def main():
    global player, moves
    game_result = ''
    render()
    while not game_result:
        moves += 1
        input_coordinates()
        render()
        player = players[moves % 2]
        game_result = analyse_game_state()
    print(game_result)


def render():
    print(dashes)
    for y in size_range:
        print(pipe, *cells[y], pipe)
    print(dashes)


def input_coordinates():
    while True:
        raw = input(crd_prompt).split()
        if len(raw) != 2 or sum(map(str.isnumeric, raw)) != 2:
            error = er_not_num
        else:
            y, x = [int(s) - 1 for s in raw]
            if not all(map(is_in_range, [y, x])):
                error = er_not_in_range
            elif cells[y][x] != ' ':
                error = er_occupied
            else:
                cells[y][x] = player
                break
        print(error)


def analyse_game_state() -> str:
    winner = get_winner()
    if winner:
        return f'{winner} wins'
    elif moves == size * size:
        return 'Draw'
    else:
        return ''


row_win = lambda p, i: all([cell == p for cell in cells[i]])
col_win = lambda p, i: all([line[i] == p for line in cells])
row_or_col_win = lambda p: any([row_win(p, i) or col_win(p, i) for i in size_range])
main_diag_win = lambda p: all([cell == p for cell in [cells[0][0], cells[1][1], cells[2][2]]])
second_diag_win = lambda p: all([cell == p for cell in [cells[0][2], cells[1][1], cells[2][0]]])


def get_winner() -> str:
    for p in players:
        if row_or_col_win(p) or main_diag_win(p) or second_diag_win(p):
            return p
    return ''


main()
