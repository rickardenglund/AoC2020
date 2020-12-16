import re
import puzzle
from datetime import datetime


def main(input):
    print('### day 16 ###')
    start1 = datetime.now()
    p1res = part1(input)
    stop1 = datetime.now()
    print(f'p1: {p1res}')

    start2 = datetime.now()
    p2res = part2(input)
    stop2 = datetime.now()
    print(f'p2: {p2res}')

    print(f'p1 took: {stop1 - start1}\np2 took: {stop2 - start2}')


class Rule():
    possible_positions = []

    def __init__(self, name, range1: tuple[int, int], range2: tuple[int, int]):
        self.name = name
        self.range1 = range1
        self.range2 = range2

    def matches(self, v: int) -> bool:
        return self.range1[0] <= v <= self.range1[1] or \
               self.range2[0] <= v <= self.range2[1]

    def set_possible_positions(self, n):
        self.possible_positions = list(range(n))

    def test(self, i: int, value: int):
        if i in self.possible_positions:
            if not self.matches(value):
                self.remove_possible_index(i)

    def remove_possible_index(self, i: int):
        self.possible_positions = [v for v in self.possible_positions if v != i]

    def __str__(self):
        return f'{self.possible_positions}'


def part1(input: str) -> int:
    class_rules, nearby_tickets,my_ticket = get_input(input)

    error_rate = 0
    for ticket in nearby_tickets:
        for v in ticket:
            if not matches_any(class_rules, v):
                error_rate += v
                break
    return error_rate


def matches_any(rules: dict[str, Rule], v: int) -> bool:
    for rule_key in rules:
        if rules[rule_key].matches(v):
            return True
    return False

#guess 37050
def part2(input: str) -> int:
    class_rules, nearby_tickets,my_ticket = get_input(input)
    valid_tickets = []
    for ticket in nearby_tickets:
        if match(class_rules, ticket):
            valid_tickets.append(ticket)

    for rule in class_rules:
        class_rules[rule].set_possible_positions(len(valid_tickets[0]))

    solved_rules = {}

    for round in range(len(class_rules)):
        for ticket in valid_tickets:
            for iv in range(len(ticket)):
                for rule_key in class_rules:
                    class_rules[rule_key].test(iv, ticket[iv])

        to_complete = []
        for rule_key in class_rules:
            if len(class_rules[rule_key].possible_positions) == 1:
                to_complete.append(rule_key)

        for rule_key in to_complete:
            solved_rules[rule_key] = class_rules[rule_key]
            del class_rules[rule_key]

        for rule_key in solved_rules:
            pos = solved_rules[rule_key].possible_positions[0]
            for ck in class_rules:
                class_rules[ck].remove_possible_index(pos)

    product = 1
    for key in solved_rules:
        name:str = solved_rules[key].name
        pos = solved_rules[key].possible_positions[0]
        if name.startswith('departure'):
            product *= my_ticket[pos]
    return product


def match(class_rules, ticket):
    for v in ticket:
        if not matches_any(class_rules, v):
            return False
    return True


def get_input(input: str):
    class_pattern = re.compile(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)')

    [class_strings, my_ticket_string, nearby_tickets] = input.split('\n\n')
    class_matches = class_pattern.findall(class_strings)
    class_rules = {}
    for (name, r1_start, r1_stop, r2_start, r2_stop) in class_matches:
        class_rules[name] = Rule(name, (int(r1_start), int(r1_stop)), (int(r2_start), int(r2_stop)))

    nearby_tickets = nearby_tickets.split('\n')[1:]
    nearby_tickets = [[int(value) for value in values.split(',')] for values in nearby_tickets]

    my_ticket_string = my_ticket_string.split('\n')[1]
    my_ticket = [int(v) for v in my_ticket_string.split(',')]

    return class_rules, nearby_tickets, my_ticket


if __name__ == "__main__":
    main(puzzle.input)
