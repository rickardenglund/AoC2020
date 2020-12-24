import puzzle
from datetime import datetime


def main(input_str):
    print('### day 24 ###')
    start1 = datetime.now()
    p1res = part1(input_str)
    stop1 = datetime.now()
    print(f'p1: {p1res}')

    start2 = datetime.now()
    p2res = part2(input_str)
    stop2 = datetime.now()
    print(f'p2: {p2res}')

    print(f'p1 took: {stop1 - start1}\np2 took: {stop2 - start2}')


WHITE = 'w'
BLACK = 'b'


def part1(input_str: str) -> int:
    instructions = get_input(input_str)
    blacks = setup_floor(instructions)

    return len(blacks)


def part2(input_str: str) -> int:
    instructions = get_input(input_str)
    blacks = setup_floor(instructions)

    for day in range(100):
        new_blacks = next_day(blacks)
        blacks = new_blacks

    return len(blacks)


def setup_floor(instructions):
    blacks = set()
    for i in instructions:
        cube_coord = to_cube_coordinate(i)

        if cube_coord in blacks:
            blacks.remove(cube_coord)
        else:
            blacks.add(cube_coord)

    return blacks


NEIGHBOUR_OFFSETS = [(1, 0, -1), (-1, 0, 1), (0, 1, -1), (0, -1, 1), (1, -1, 0), (-1, 1, 0)]


def next_day(old_blacks: set):
    new_blacks = set()
    neighbours_to_visit = set()
    for neighbour in old_blacks:
        for (ox, oy, oz) in NEIGHBOUR_OFFSETS:
            (x, y, z) = neighbour
            neighbours_to_visit.add((x + ox, y + oy, z + oz))

        update_tile(neighbour, new_blacks, old_blacks)

    for neighbour in neighbours_to_visit:
        update_tile(neighbour, new_blacks, old_blacks)

    return new_blacks


def update_tile(c, new_blacks, old_blacks):
    count = count_neighbours(old_blacks, c)
    if c in old_blacks:  # is black
        if not (count[BLACK] == 0 or count[BLACK] > 2):
            new_blacks.add(c)
    else:  # is white
        if count[BLACK] == 2:
            new_blacks.add(c)


def count_neighbours(blacks, pos):
    counts = {BLACK: 0, WHITE: 0}
    for (ox, oy, oz) in NEIGHBOUR_OFFSETS:
        (x, y, z) = pos
        if (x + ox, y + oy, z + oz) in blacks:
            counts[BLACK] += 1
        else:
            counts[WHITE] += 1
    return counts


def to_cube_coordinate(instruction: list[str]) -> (int, int, int):
    x, y, z = (0, 0, 0)
    for i in instruction:
        if i == 'e':
            x += 1
            y -= 1
        elif i == 'w':
            x -= 1
            y += 1
        elif i == 'nw':
            z -= 1
            y += 1
        elif i == 'se':
            z += 1
            y -= 1
        elif i == 'ne':
            x += 1
            z -= 1
        elif i == 'sw':
            x -= 1
            z += 1
        else:
            raise Exception('invalid direction', i)
    return x, y, z


def get_input(input: str):
    instructions = []
    for line in input.split('\n'):
        instruction = []
        i = 0
        while i < len(line):
            if line[i:i + 2] in ['nw', 'sw', 'ne', 'se']:
                instruction.append(line[i:i + 2])
                i += 2
            elif line[i] in ['e', 'w']:
                instruction.append(line[i])
                i += 1
            else:
                raise Exception('invalid line', line)
        instructions.append(instruction)

    return instructions


def mod_input(match):
    w1, w2 = match
    return w2, w1


if __name__ == "__main__":
    main(puzzle.input)
