import re
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


def play_game(seed, target_round):
    state = {}
    for i in range(len(seed)):
        state[seed[i]] = [i + 1]
    prev_num = seed[len(seed) - 1]

    current_round = len(seed) + 1
    while current_round <= target_round:
        if len(state.get(prev_num, [])) <= 1:
            new_num = 0
        else:
            l = state[prev_num][-2:]
            new_num = l[1] - l[0]

        state[new_num] = new_history(state, current_round, new_num)

        prev_num = new_num

        # print(f'{current_round}: {prev_num}')
        current_round += 1
        if current_round % 100_000 == 0:
            print(f'round:{current_round}/{target_round}')

    return prev_num


def new_history(state, current_round, num):
    hist = state.get(num, [])
    if len(hist) <= 1:
        return hist + [current_round]

    hist[0] = hist[1]
    hist[1] = current_round
    return hist


if __name__ == "__main__":
    main(puzzle.input)
