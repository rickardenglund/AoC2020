import itertools
import functools


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
    f = open("input.txt", "r")
    contents = f.readlines()
    f.close()

    return list(map(lambda x: int(x), contents))


def get_combo(numbers, n, target):
    for values in itertools.combinations(numbers, n):
        if sum(values) == target:
            return functools.reduce(lambda a, b: a * b, values, 1)

    raise Exception('no combo found')


if __name__ == "__main__":
    main()
