import re
import puzzle
from datetime import datetime


def main(input):
    print('### day 17 ###')
    start1 = datetime.now()
    p1res = part1(input)
    stop1 = datetime.now()
    print(f'p1: {p1res}')

    start2 = datetime.now()
    p2res = part2(input)
    stop2 = datetime.now()
    print(f'p2: {p2res}')

    print(f'p1 took: {stop1 - start1}\np2 took: {stop2 - start2}')


def count_active_neighbours(active_cubes, active_cube):
    (x, y, z, w) = active_cube
    n_neighbours = 0
    for dw in range(-1, 2):
        for dz in range(-1, 2):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if 0 == dx == dy == dz == dw:
                        continue

                    neighbour = (x + dx, y + dy, z + dz, w + dw)
                    if neighbour in active_cubes:
                        n_neighbours += 1

    return n_neighbours


def count_me_and_active_neightbours(counts, active_cubes, me):
    (x, y, z, w) = me
    for dw in range(-1, 2):
        for dz in range(-1, 2):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    cube = (x + dx, y + dy, z + dz, w + dw)
                    if cube not in counts.keys():
                        counts[cube] = count_active_neighbours(active_cubes, cube)
    return counts


def cycle(active_cubes):
    new_active_cubes = set()
    counts = {}

    for active_cube in active_cubes:
        count_me_and_active_neightbours(counts, active_cubes, active_cube)

    for cube in counts:
        if cube in active_cubes:
            if 2 <= counts[cube] <= 3:
                new_active_cubes.add(cube)
        else:
            if counts[cube] == 3:
                new_active_cubes.add(cube)
    return new_active_cubes


def part1(input: str) -> int:
    return -1


def part2(input: str) -> int:
    active_cubes = get_input(input)

    for i in range(6):
        active_cubes = cycle(active_cubes)

    return len(active_cubes)


def get_input(input: str):
    active_cells = set()
    lines = input.split('\n')

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                active_cells.add((x, y, 0, 0))
    return active_cells


if __name__ == "__main__":
    main(puzzle.input)
