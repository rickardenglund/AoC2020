import re
import puzzle
from datetime import datetime


def main(input):
    print('### day XX ###')
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
    inputs = get_input(input)

    return len(inputs)


def part2(input: str) -> int:
    inputs = get_input(input)

    return len(inputs)*2


def get_input(input: str):
    pattern = re.compile(r'(\w+) (\w+)')
    matches = pattern.findall(input)

    return list(
        map(mod_input, matches)
    )


def mod_input(match):
    w1, w2 = match
    return w2, w1


if __name__ == "__main__":
    main(puzzle.input)
