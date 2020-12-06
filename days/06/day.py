import puzzle
import string
from functools import reduce
from datetime import datetime


def main():
    print('### day 06 ###')
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
    groups = (group.split('\n') for group in puzzle.input.split('\n\n'))

    answers_per_group = (
        reduce(lambda agg, member_answers: agg.union(member_answers), group, set())
        for group in groups
    )

    return reduce(lambda agg, group_answers: agg + len(group_answers), answers_per_group, 0)


def part2():
    groups = (group.split('\n') for group in puzzle.input.split('\n\n'))

    common_answers_per_group = (
        reduce(lambda agg, member_answers: agg.intersection(member_answers), group, set(string.ascii_lowercase))
        for group in groups
    )

    return reduce(lambda agg, group_answers: agg + len(group_answers), common_answers_per_group, 0)


if __name__ == "__main__":
    main()
