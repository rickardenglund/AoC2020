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
    possible_neighbours = get_neighbours(pieces)
    corner_pieces = [key for key in possible_neighbours if len(possible_neighbours[key]) == 2]
    return reduce(lambda a, b: a * b, corner_pieces, 1)


def get_neighbours(pieces):
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
    return possible_neighbours


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


SEA_MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


class Piece():
    def __init__(self, id, arr):
        self.id = id
        self.arr = arr


class Image():
    def __init__(self, first_corner: Piece):
        self.parts = {first_corner.id: first_corner}

    # def insert(self, image, next_to):


def part2(input: str) -> int:
    pieces = get_input(input)
    possible_neighbours = get_neighbours(pieces)
    corner_pieces = [key for key in possible_neighbours if len(possible_neighbours[key]) == 2]

    first_corner = corner_pieces[0]
    to_visit = {first_corner}
    visited = []
    rott = get_neighbours_rotated(pieces, first_corner, possible_neighbours[first_corner])
    for n in rott:
        print(n)

    while len(to_visit) > 0:
        piece = to_visit.pop()
        for neighbour in possible_neighbours[piece]:
            if neighbour not in visited:
                to_visit.add(neighbour)
        print('visited', piece)
        visited.append(piece)

    return len(visited)


def get_neighbours_rotated(pieces, current_key, neighbours):
    current = pieces[current_key]
    current_sides = [
        current[0],
        current[:, current.shape[1] - 1],
        current[current.shape[0] - 1][::-1],
        current[:, 0][::-1]
    ]

    res = [None] * 4
    for side_index in range(len(current_sides)):
        for neighbour_key in neighbours:
            rotated = rotate(pieces[neighbour_key], current_sides[side_index], side_index)
            if rotated:
                res[side_index] = rotated
    return res


def rotate(neighbour, side_to_match, target_side):
    neighbour_sides = [
        neighbour[0],
        neighbour[:, neighbour.shape[1] - 1],
        neighbour[neighbour.shape[0] - 1][::-1],
        neighbour[:, 0][::-1]
    ]

    if target_side == 0:
        if all(side_to_match == neighbour_sides[0]):
            return np.rot90(np.rot90(neighbour))
        elif all(side_to_match == neighbour_sides[1]):
            return np.rot90(neighbour)
        elif all(side_to_match == neighbour_sides[2]):
            return neighbour
        elif all(side_to_match == neighbour_sides[3]):
            return np.rot90(np.rot90(np.rot90(neighbour)))
        return None
    elif target_side == 1:
        if all(side_to_match == neighbour_sides[0]):
            return np.rot90(np.rot90(np.rot90(neighbour)))
        elif all(side_to_match == neighbour_sides[1]):
            return np.rot90(np.rot90(neighbour))
        elif all(side_to_match == neighbour_sides[2]):
            return np.rot90(neighbour)
        elif all(side_to_match == neighbour_sides[3]):
            return neighbour
        return None
    elif target_side == 2:
        if all(side_to_match == neighbour_sides[0]):
            return neighbour
        elif all(side_to_match == neighbour_sides[1]):
            return np.rot90(np.rot90(np.rot90(neighbour)))
        elif all(side_to_match == neighbour_sides[2]):
            return np.rot90(np.rot90(neighbour))
        elif all(side_to_match == neighbour_sides[3]):
            return np.rot90(neighbour)
        return None
    elif target_side == 3:
        if all(side_to_match == neighbour_sides[0]):
            return np.rot90(np.rot90(np.rot90(neighbour)))
        elif all(side_to_match == neighbour_sides[1]):
            return np.rot90(np.rot90(neighbour))
            return np.rot90(np.rot90(np.rot90(neighbour)))
        elif all(side_to_match == neighbour_sides[2]):
            return np.rot90(neighbour)
        elif all(side_to_match == neighbour_sides[3]):
            return neighbour
        return None


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
