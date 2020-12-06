import puzzle
import string
from functools import reduce


def main():
    print('### day 06 ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    groups = [group.split('\n') for group in puzzle.input.split('\n\n')]

    answers_per_group = [
        reduce(lambda agg, member_answers: agg.union(member_answers), group, set())
        for group in groups
    ]

    return sum([len(group_answers) for group_answers in answers_per_group])


def part2():
    groups = [group.split('\n') for group in puzzle.input.split('\n\n')]

    common_answers_per_group = [
        reduce(lambda agg, member_answers: agg.intersection(member_answers), group, set(string.ascii_lowercase))
        for group in groups
    ]

    return sum([len(group_answers) for group_answers in common_answers_per_group])



if __name__ == "__main__":
    main()
