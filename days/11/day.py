import re
import puzzle
from datetime import datetime
from enum import Enum


def main():
    print('### day 11 ###')
    start1 = datetime.now()
    p1res = part1()
    stop1 = datetime.now()
    print(f'p1: {p1res}')

    start2 = datetime.now()
    p2res = part2()
    stop2 = datetime.now()
    print(f'p2: {p2res}')

    print(f'p1 took: {stop1 - start1}\np2 took: {stop2 - start2}')


def part1():
    state = get_input(puzzle.input)
    return simulate(state, count_immediate_neighbours)


def simulate(state, count_neighbours):
    previous_state = []

    while state != previous_state:
        previous_state = state
        state = next_round(state, count_neighbours)

    count = 0
    for line in state:
        for p in line:
            if p == OCCUPIED:
                count += 1

    return count


def next_round(state: list[str], count_neighbours) -> list[str]:
    out = []
    for y in range(len(state)):
        out.append(state[y].copy())

        for x in range(len(state[y])):
            neighbours = count_neighbours(state, x, y)
            if state[y][x] == EMPTY and neighbours[OCCUPIED] == 0:
                out[y][x] = OCCUPIED
            elif state[y][x] == OCCUPIED and neighbours[OCCUPIED] >= 4:
                out[y][x] = EMPTY
    return out


def count_immediate_neighbours(state, x, y) -> dict[str, int]:
    count: dict[str, int] = {
        EMPTY: 0,
        OCCUPIED: 0,
        FLOOR: 0
    }

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == dx == 0 or dy + y < 0 or dx + x < 0 or dy + y >= len(state) or dx + x >= len(state[0]):
                continue

            p = state[dy + y][dx + x]
            count[p] += 1

    return count


def count_distant_neighbours(state, x, y) -> dict[str, int]:
    count: dict[str, int] = {
        EMPTY: 0,
        OCCUPIED: 0,
        FLOOR: 0
    }

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == dx == 0 or dy + y < 0 or dx + x < 0 or dy + y >= len(state) or dx + x >= len(state[0]):
                continue

            p = state[dy + y][dx + x]
            count[p] += 1

    return count


def part2():
    state = get_input(puzzle.input)
    return simulate(state, count_distant_neighbours)


FLOOR = '.'
OCCUPIED = '#'
EMPTY = 'L'


def get_input(input):
    lines = input.split('\n')
    lines = [list(line) for line in lines]
    return lines


if __name__ == "__main__":
    main()
