import re
import puzzle
from datetime import datetime


def main(input):
    print('### day 18 ###')
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
    expressions = input.split('\n')
    return sum([evaluate(parse(exp)) for exp in expressions])


def part2(input: str) -> int:
    inputs = get_input(input)

    return len(inputs) * 2


def evaluate(expr: list) -> int:
    if isinstance(expr, int):
        return expr
    if len(expr) == 1:
        return evaluate(expr[0])
    if expr[1] == '+':
        return evaluate(
            [evaluate(expr[0]) + evaluate(expr[2])]
            + expr[3:]
        )
    if expr[1] == '*':
        return evaluate(
            [evaluate(expr[0]) * evaluate(expr[2])]
            + expr[3:]
        )
    if expr[0] == '(' or expr[0] == ')':
        raise Exception('found paren', expr)

    raise Exception('bad expression:', expr)


def parse(string: str):
    pattern = re.compile(r'([\d+\+*\(\)])')
    symbols = []
    for part in pattern.findall(string):
        try:
            n = int(part)
            symbols.append(n)
        except:
            symbols.append(part)
    return to_tree(symbols)


def to_tree(symbols: list):
    res = []
    i = 0
    while i < len(symbols):
        if symbols[i] == '(':
            closing_i = i + find_closing(symbols[i + 1:])
            subexp = to_tree(symbols[i + 1:closing_i])
            res.append(subexp)
            i = closing_i + 1
        else:
            res.append(symbols[i])
            i += 1
    return res


def find_closing(symbols):
    depth = 1
    i = 1
    for s in symbols:
        if s == '(':
            depth += 1
        if s == ')':
            depth -= 1
        if depth == 0:
            return i
        i += 1
    raise Exception('no matching bracket found', symbols)


if __name__ == "__main__":
    main(puzzle.input)
