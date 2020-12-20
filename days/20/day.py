import re
from functools import reduce


import puzzle
from datetime import datetime
import numpy as np


def main(input):
    print('### day 20 ###')
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
    pieces = get_input(input)
    possible_neighbours: dict[int, set[int]] = {}
    for key in pieces:
        possible_neighbours[key] = set()

    for key in pieces:
        for other_key in pieces:
            if key == other_key:
                continue

            if fits(pieces[key], pieces[other_key]):
                possible_neighbours[key].add(other_key)
                possible_neighbours[other_key].add(key)
    count = 0
    for key in pieces:
        if len(pieces[key]) == 2:
            count += 1
    corner_pieces = [key for key in possible_neighbours if len(possible_neighbours[key]) == 2]
    return reduce(lambda a,b:a*b, corner_pieces, 1)


def fits(p1: np.ndarray, p2: np.ndarray) -> bool:
    p1_sides = [
        p1[0],
        p1[:, p1.shape[1] - 1],
        p1[p1.shape[0] - 1],
        p1[:, 0],
        p1[0][::-1],
        p1[:, p1.shape[1] - 1][::-1],
        p1[p1.shape[0] - 1][::-1],
        p1[:, 0][::-1]
    ]

    p2_sides = [
        p2[0],
        p2[:, p2.shape[1] - 1],
        p2[p2.shape[0] - 1],
        p2[:, 0],
        p2[0][::-1],
        p2[:, p2.shape[1] - 1][::-1],
        p2[p2.shape[0] - 1][::-1],
        p2[:, 0][::-1]
    ]

    for s1 in p1_sides:
        for s2 in p2_sides:
            if all(s1 == s2):
                return True
    return False


def part2(input: str) -> int:
    inputs = get_input(input)

    return len(inputs) * 2


def get_input(input: str) -> dict[int, np.ndarray]:
    id_pattern = re.compile(r'Tile (\d+):')
    parts = input.split('\n\n')

    pieces = {}
    for part in parts:
        lines = part.split('\n')
        m = id_pattern.match(lines[0])
        id = int(m.group(1))
        rows = []
        for row in lines[1:]:
            rows.append(list(row))
        pieces[id] = np.array(rows)

    return pieces


if __name__ == "__main__":
    main(puzzle.input)
