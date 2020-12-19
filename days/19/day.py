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
        match, matches = starts_with(rules, 0, m)
        if matches and match == m:
            print('match', m)
            n_valid += 1

    return n_valid


def part2(input: str) -> int:
    rules, messages = get_input(input)

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    n_valid = 0
    for m in messages:
        match, matches = starts_with(rules, 0, m)
        if matches and match == m:
            n_valid += 1

    return n_valid


def starts_with(rules, rule_id, message: str) -> (str, bool):
    rule = rules[rule_id]

    if len(message) == 0:
        return '', False

    if isinstance(rule, str):
        return message[0], message[0] == rule

    for r in rule:
        match = ''
        matching_rules = 0
        for r_i in range(len(r)):
            submatch, matches = starts_with(rules, r[r_i], message[len(match):])
            if not matches:
                break
            match += submatch
            matching_rules += 1
        if matching_rules == len(r) and message.startswith(match):
            return match, True
    return '', False


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
