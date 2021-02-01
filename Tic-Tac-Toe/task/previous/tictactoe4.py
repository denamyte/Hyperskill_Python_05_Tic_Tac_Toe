from typing import List

Cells = List[List[str]]
cells: Cells
size = 3
size_range = range(size)
crd_prompt, cells_prompt = 'Enter the coordinates: ', 'Enter cells: '
dashes, pipe, x_player, o_player = '-' * 9, '|', 'X', 'O',
er_not_num = 'You should enter numbers!'
er_not_range = 'Coordinates should be from 1 to 3!'
er_occupied = 'This cell is occupied! Choose another one!'
x_in_range = lambda x: x in size_range

# CountDict = Dict[str, int]
# counts: CountDict = {}
# wins: CountDict = {x_player: 0,
#                    o_player: 0}


def main():
    global cells
    s = input(cells_prompt).replace('_', ' ')
    cells = parse_cells_str(s)
    render()
    set_coordinates(input_coordinates(), x_player)
    render()


def parse_cells_str(s: str) -> Cells:
    return [list(s[x * size:(x + 1) * size]) for x in size_range]


def render():
    print(dashes)
    for y in size_range:
        print(pipe, *cells[y], pipe)
    print(dashes)


def input_coordinates() -> List[int]:
    while True:
        raw = input(crd_prompt).split()
        if len(raw) != 2 or sum(map(str.isnumeric, raw)) != 2:
            error = er_not_num
        else:
            crd = [int(x) - 1 for x in raw]
            if sum(map(x_in_range, crd)) != 2:
                error = er_not_range
            elif occupied(crd):
                error = er_occupied
            else:
                return crd
        print(error)


def occupied(crd: List[int]) -> bool:
    return cells[crd[0]][crd[1]] != ' '


def set_coordinates(crd: List[int], player: str):
    cells[crd[0]][crd[1]] = player


# def count_and_analyse(s: str, cells: Cells):
#     global result
#     if count_occurrences(s) or count_wins(cells):
#         result = 'Impossible'
#     elif sum(wins.values()) == 1:
#         result = f'{x_player if wins[x_player] else o_player} wins'
#     elif sum(counts.values()) == size * size:
#         result = 'Draw'
#     else:
#         result = 'Game not finished'
#
#
# def count_occurrences(s: str) -> bool:
#     flat: List[str] = list(s)
#     for key in [x_player, o_player]:
#         counts[key] = flat.count(key)
#     return abs(counts[x_player] - counts[o_player]) > 1
#
#
# def count_wins(cells: Cells) -> bool:
#     for pl in [x_player, o_player]:
#         for index in size_range:
#             # count horizontal wins:
#             sub_cells = cells[index][index:(index + 1) * size]
#             wins[pl] += sub_cells.count(pl) // size
#             # count vertical wins:
#             wins[pl] += [cells[0][index], cells[1][index], cells[2][index]].count(pl) // size
#         # count diagonal wins:
#         wins[pl] += [cells[0][0], cells[1][1], cells[2][2]].count(pl) // size
#         wins[pl] += [cells[0][2], cells[1][1], cells[2][0]].count(pl) // size
#     return sum(wins.values()) > 1


main()
