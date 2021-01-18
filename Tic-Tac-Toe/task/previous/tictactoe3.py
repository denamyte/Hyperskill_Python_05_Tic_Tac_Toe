from typing import List, Dict

Cells = List[List[str]]
CountDict = Dict[str, int]
size = 3
size_range = range(size)
dashes = '-' * 9
pipe = '|'
x_player, o_player = 'X', 'O',
counts: CountDict = {}
wins: CountDict = {x_player: 0,
                   o_player: 0}
result: List[str] = []


def main():
    s = input('Enter cells: ').replace('_', ' ')
    cells = parse_input(s)
    count_and_analyse(s, cells)
    render(cells)


def parse_input(s: str) -> Cells:
    return [list(s[x * size:(x + 1) * size]) for x in size_range]


def count_and_analyse(s: str, cells: Cells):
    if count_occurrences(s) or count_wins(cells):
        result.append('Impossible')
    elif sum(wins.values()) == 1:
        result.append(f'{x_player if wins[x_player] else o_player} wins')
    elif sum(counts.values()) == size * size:
        result.append('Draw')
    else:
        result.append('Game not finished')


def count_occurrences(s) -> bool:
    flat = list(s)
    for key in [x_player, o_player]:
        counts[key] = flat.count(key)
    return abs(counts[x_player] - counts[o_player]) > 1


def count_wins(cells: Cells) -> bool:
    for pl in [x_player, o_player]:
        for index in size_range:
            # count horizontal wins:
            sub_cells = cells[index][index:(index + 1) * size]
            wins[pl] += sub_cells.count(pl) // size
            # count vertical wins:
            wins[pl] += [cells[0][index], cells[1][index], cells[2][index]].count(pl) // size
        # count diagonal wins:
        wins[pl] += [cells[0][0], cells[1][1], cells[2][2]].count(pl) // size
        wins[pl] += [cells[0][2], cells[1][1], cells[2][0]].count(pl) // size
    return sum(wins.values()) > 1


def render(cells: Cells):
    print(dashes)
    for y in size_range:
        print(pipe, *cells[y], pipe)
    print(dashes)
    print(result[0])


main()
