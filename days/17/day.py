import re
import puzzle
from datetime import datetime
import itertools


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


def part1(input: str) -> int:
    n_dimensions = 3
    return boot_sequence(input, n_dimensions)


def part2(input: str) -> int:
    n_dimensions = 4
    return boot_sequence(input, n_dimensions)


def boot_sequence(input: str, n_dimensions: int) -> int:
    active_cubes = get_input(input, n_dimensions)

    for i in range(6):
        active_cubes = cycle(active_cubes, n_dimensions)

    return len(active_cubes)


def cycle(active_cubes, n_dimensions: int):
    new_active_cubes = set()
    counts = {}

    for active_cube in active_cubes:
        neighbours = neighbour_iterator(active_cube, n_dimensions)
        for cube in neighbours:
            counts[cube] = count_active_neighbours(active_cubes, cube, n_dimensions)

    for cube in counts:
        if cube in active_cubes:
            if 2 <= counts[cube] <= 3:
                new_active_cubes.add(cube)
        else:
            if counts[cube] == 3:
                new_active_cubes.add(cube)
    return new_active_cubes


def count_me_and_active_neighbours(counts, active_cubes, me, n_dimensions):
    for cube in neighbour_iterator(me, n_dimensions):
        counts[cube] = count_active_neighbours(active_cubes, cube)
    return counts


def count_active_neighbours(active_cubes, cube, n_dimensions):
    count = 0
    for neighbour in neighbour_iterator(cube, n_dimensions):
        if neighbour in active_cubes and cube != neighbour:
            count += 1
    return count


def get_input(input: str, n_dimensions: int):
    active_cells = set()
    lines = input.split('\n')

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                l = [0] * n_dimensions
                l[0] = x
                l[1] = y
                active_cells.add(tuple(l))
    return active_cells


def neighbour_iterator(pos, n_dimensions):
    return (
        tuple([sum(vs) for vs in zip(delta, pos)])
        for delta in (deltas for deltas in itertools.product(range(-1, 2), repeat=n_dimensions)))


if __name__ == "__main__":
    main(puzzle.input)
