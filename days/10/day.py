import re
import puzzle
from datetime import datetime
from itertools import permutations


def main():
    print('### day 10 ###')
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
    outputs = get_input(puzzle.input)

    joltage_diffs = {1: 0, 2: 0, 3: 0}
    for i in range(len(outputs) - 1):
        joltage_diffs[outputs[i + 1] - outputs[i]] += 1

    return joltage_diffs[1] * joltage_diffs[3]


def part2():
    outputs = get_input(puzzle.input)

    return count_possible_configurations(outputs, 0)


def count_possible_configurations(outputs, cur):
    memo = {len(outputs) - 1: 1}
    return count_rec(outputs, cur, memo)


def count_rec(outputs, current_i, memo: dict[int, int]):
    if current_i in memo.keys():
        return memo[current_i]

    if current_i == len(outputs) - 1:
        return 1

    res = 0
    for step in get_possible_next_adapters(outputs, current_i):
        res += count_rec(outputs, current_i + step, memo)

    memo[current_i] = res
    return res


def get_possible_next_adapters(outputs, index):
    v = outputs[index]
    res = []
    for i in range(1, 4):
        if index + i == len(outputs):
            break
        diff = outputs[index + i] - v
        if diff <= 3:
            res.append(i)
    return res


def get_input(input):
    outputs = [int(x) for x in input.split('\n')]
    outputs.sort()
    outputs.append(outputs[len(outputs) - 1] + 3)
    outputs.insert(0, 0)
    return outputs


if __name__ == "__main__":
    main()
