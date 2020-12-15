import re

from typing import Dict

import puzzle
from datetime import datetime


def main(input):
    print('### day 15 ###')
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
    return play_game(input, 2020)


# time: 51s, 36s
def part2(input: str) -> int:
    return play_game(input, 30_000_000)


class History():
    prev = None
    prev_prev = None

    def add(self, n):
        self.prev_prev = self.prev
        self.prev = n

    def get_age(self):
        if self.prev_prev is None:
            return 0
        return self.prev - self.prev_prev

    def __str__(self):
        return f'{self.prev},{self.prev_prev}'


def play_game(seed, target_round):
    state = initial_state(seed)

    prev_num = seed[len(seed) - 1]
    h_old = state.get(prev_num, History())
    current_round = len(seed) + 1
    while current_round <= target_round:
        new_num = h_old.get_age()
        h_new = state.get(new_num, History())
        h_new.add(current_round)

        state[new_num] = h_new

        prev_num = new_num
        h_old = h_new
        current_round += 1

    return prev_num


def initial_state(seed)-> Dict[int, History]:
    state: Dict[int, History] = {}
    for i in range(len(seed)):
        if seed[i] in state.keys():
            state[seed[i]].add(i + 1)
        else:
            h = History()
            h.add(i + 1)
            state[seed[i]] = h
    return state


def new_history(state, current_round, num):
    hist = state.get(num, [])
    if len(hist) <= 1:
        return hist + [current_round]

    hist[0] = hist[1]
    hist[1] = current_round
    return hist


if __name__ == "__main__":
    main(puzzle.input)
