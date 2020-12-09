import re
import puzzle
from datetime import datetime
from itertools import combinations


def main():
    print('### day 09 ###')
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
    numbers = get_input(puzzle.input)
    preamble_size = 25

    return find_number(numbers, preamble_size)


def find_number(numbers, preamble_size):
    i = 0
    while i + preamble_size < len(numbers):
        if not is_valid(numbers[i + preamble_size], numbers[i:i + preamble_size], preamble_size):
            return numbers[i + preamble_size]
        i += 1
    return None


def part2():
    numbers = get_input(puzzle.input)
    preamble_size = 25

    target = find_number(numbers, preamble_size)
    xmas_weakness = find_weakness(numbers, target)
    return xmas_weakness


def find_weakness(numbers, target):
    for start_i in range(len(numbers)):
        sum = numbers[start_i]
        for stop_i in range(start_i + 1, len(numbers)):
            sum += numbers[stop_i]
            if sum == target:
                return min(numbers[start_i:stop_i]) + max(numbers[start_i:stop_i])
            if sum > target:
                break


def is_valid(total, numbers, N):
    for (a,b) in combinations(numbers, 2):
        if a + b == total:
            return True
    return False


def get_input(input):
    return [int(x) for x in input.split('\n')]


if __name__ == "__main__":
    main()
