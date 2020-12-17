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


def count_active_neightbours(active_cubes: set[tuple[int, int, int]], active_cube: tuple[int, int, int]) -> int:
    (x, y, z) = active_cube
    n_neighbours = 0
    for dz in range(-1, 2):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if 0 == dx == dy == dz:
                    continue

                neightbour = (x + dx, y + dy, z + dz)
                if neightbour in active_cubes:
                    n_neighbours += 1

    return n_neighbours


def count_me_and_active_neightbours(active_cubes, me):
    counts = {}
    (x, y, z) = me
    for dz in range(-1, 2):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                cube = (x + dx, y + dy, z + dz)
                counts[cube] = count_active_neightbours(active_cubes, cube)
    return counts


def cycle(active_cubes: set[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    new_active_cubes = set()

    for active_cube in active_cubes:
        counts = count_me_and_active_neightbours(active_cubes, active_cube)
        for cube in counts:
            if cube in active_cubes:
                if 2 <= counts[cube] <=3:
                    new_active_cubes.add(cube)
            else:
                if counts[cube] == 3:
                    new_active_cubes.add(cube)

    return new_active_cubes




def part1(input: str) -> int:
    active_cubes = get_input(input)

    for i in range(6):
        active_cubes = cycle(active_cubes)

    return len(active_cubes)


def part2(input: str) -> int:
    inputs = get_input(input)

    return len(inputs) * 2


def get_input(input: str):
    active_cells = set()
    lines = input.split('\n')

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                active_cells.add((x, y, 0))
    return active_cells


if __name__ == "__main__":
    main(puzzle.input)
