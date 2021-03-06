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


def pre_calc(rules: dict[int, list[list]]):
    lookup = {}
    for n in range(len(rules)):
        for rule_key in rules:
            if is_complete(rules[rule_key]):
                lookup[rule_key] = merge1(rules[rule_key])
            else:
                for r_i in range(len(rules[rule_key])):
                    rule = rules[rule_key][r_i]
                    for p_i in range(len(rule)):
                        p = rule[p_i]
                        if p in lookup:
                            rules[rule_key] = merge(rules[rule_key][r_i], p_i, lookup[p])
    return lookup


def merge(rule, to_replace_index, replace_withs):
    before = rule[:to_replace_index]
    after = rule[to_replace_index + 1:]

    new = []
    for replace_with in replace_withs:
        new.append(before + [replace_with] + after)

    return new

def merge1(rules):
    new = []
    for rule in rules:
        new.append(''.join(rule))

    return new

def is_complete(rules: list[list]) -> bool:
    for rule in rules:
        for p in rule:
            if isinstance(p, int):
                return False
    return True


def part1(input: str) -> int:
    rules, messages = get_input(input)
    lookup = pre_calc(rules)

    n_valid = 0
    for m in messages:
        if matches(lookup, 0, m):
            print('match', m)
            n_valid += 1

    return n_valid


def part2(input: str) -> int:
    rules, messages = get_input(input)

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    n_valid = 0
    for m in messages:
        if matches(rules, ):
            n_valid += 1

    return n_valid


def matches(rules, rule_id, message: str) -> (str, bool):
    if message in rules[rule_id]:
        return True
    return False


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
