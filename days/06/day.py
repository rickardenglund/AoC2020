import puzzle
import re
from typing import Dict, List, Any
from functools import reduce


def main():
    print('### day 06 ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    lines = puzzle.input.split('\n')

    groups = []
    cur_group = set()
    for line in lines:
        if line == '':
            groups.append(cur_group)
            cur_group = set()

        for yes_answer in line:
            cur_group.add(yes_answer)

    total = 0
    for group in groups:
        total += len(group)

    return total


def part2():
    lines = puzzle.input.split('\n')

    groups: list[tuple[int, dict[str, int]]] = []
    cur_group: dict[str, int] = {}
    cur_group_size = 0
    for line in lines:
        if line == '':
            groups.append((cur_group_size, cur_group))
            cur_group = {}
            cur_group_size = 0
            continue

        for yes_answer in line:
            cur_group[yes_answer] = cur_group.get(yes_answer, 0) + 1

        cur_group_size += 1

    total = 0
    for n_members, answers in groups:
        all_yes = count_all(n_members, answers)
        # print(n_members, answers, all_yes)
        total += all_yes

    return total


def count_all(n_members: int, answers: dict[str, int]) -> int:
    total = 0
    for answer in answers:
        if answers[answer] == n_members:
            total += 1
    return total


def get_input() -> list[set[str]]:
    return groups


if __name__ == "__main__":
    main()
