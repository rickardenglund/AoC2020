import re
import puzzle
from datetime import datetime


def main(input):
    print('### day 19 ###')
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
    rules, messages = get_input(input)

    n_valid = 0
    for m in messages:
        match_len = is_valid(rules, 0, m)
        print(m, match_len)
        if match_len == len(m):
            print('match', m)
            n_valid += 1

    return n_valid


def is_valid(rules, rule_id, message) -> int:
    rule = rules[rule_id]

    while True:
        if isinstance(rule, str):
            if message[0] == rule:
                return 1
            else:
                return 0

        for r in rule:
            i = 0
            for r_i in range(len(r)):
                delta = is_valid(rules, r[r_i], message[i:])
                if delta == 0:
                    break
                i += delta

            if i == len(message):
                return i
        return 0


def part2(input: str) -> int:
    inputs = get_input(input)

    return len(inputs) * 2


def get_input(input: str):
    [rules_str, messages] = input.split('\n\n')

    rules = {}
    for line in rules_str.split('\n'):
        parts = line.split(' ')
        id = int(parts[0][:-1])
        if not parts[1].isdigit():
            rules[id] = parts[1][1:-1]
            continue

        rulelist = []
        cur_rule = []
        i = 1
        while i < len(parts):
            if parts[i] == '|':
                rulelist.append(cur_rule)
                cur_rule = []
                i += 1
                continue
            cur_rule.append(int(parts[i]))
            i += 1
        rulelist.append(cur_rule)
        rules[id] = rulelist

    return rules, messages.split('\n')


if __name__ == "__main__":
    main(puzzle.input)
