import itertools
import functools
import puzzle
import re


def main():
    print('### day 01 ###')

    print('p1:', part1())
    print('p2:', part2())


TARGET = 2020


def part1():
    numbers = get_numbers()
    return get_combo(numbers, 2, TARGET)


def part2():
    numbers = get_numbers()
    return get_combo(numbers, 3, TARGET)


def get_numbers():
    pattern = re.compile(r'(\d+)\n')
    matches = pattern.findall(puzzle.input)

    return list(
        map(mod_input, matches)
    )


def mod_input(match):
    w1 = match
    return int(w1)


def get_combo(numbers, n, target):
    for values in itertools.combinations(numbers, n):
        if sum(values) == target:
            return functools.reduce(lambda a, b: a * b, values, 1)

    raise Exception('no combo found')


if __name__ == "__main__":
    main()
