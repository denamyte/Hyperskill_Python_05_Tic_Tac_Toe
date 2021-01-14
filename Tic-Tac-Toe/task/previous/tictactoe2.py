from typing import List


Cells = List[List[str]]
size = 3
size_range = range(size)
dashes = '-' * 9
pipe = '|'


def main():
    s = input('Enter cells: ')
    cells = parse_input(s)
    render(cells)


def parse_input(s: str) -> Cells:
    return [list(s[x * size:(x + 1) * size]) for x in size_range]


def render(cells: Cells):
    print(dashes)
    for y in size_range:
        print(pipe, *cells[y], pipe)
    print(dashes)


main()
