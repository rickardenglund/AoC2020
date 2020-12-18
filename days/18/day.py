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
    return sum([evaluate(parse(exp, False)) for exp in expressions])


def part2(input: str) -> int:
    expressions = input.split('\n')
    return sum([evaluate(parse(exp, True)) for exp in expressions])


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


def parse(string: str, plus_precedence: bool):
    pattern = re.compile(r'([\d+\+*\(\)])')
    symbols = []
    for part in pattern.findall(string):
        if part.isdigit():
            n = int(part)
            symbols.append(n)
        else:
            symbols.append(part)

    tree = parenthesis(symbols)

    if plus_precedence:
        tree = pluses(tree)

    return tree


def pluses(symbols: list):
    if isinstance(symbols, int):
        return symbols
    if len(symbols) == 1:
        return symbols[0]

    res = []
    i = 0
    while i < len(symbols):
        if i < len(symbols) - 1 and symbols[i + 1] == '+':
            res.append([pluses(symbols[i]), '+', pluses(symbols[i + 2])])
            i += 3
        elif symbols[i] == '+':
            res[len(res) - 1] = [res[len(res) - 1], '+', pluses(symbols[i + 1])]
            i += 2
        else:
            res.append(pluses(symbols[i]))
            i += 1

    return res


def parenthesis(symbols: list):
    res = []
    i = 0
    while i < len(symbols):
        if symbols[i] == '(':
            closing_i = i + find_closing(symbols[i + 1:])
            subexp = parenthesis(symbols[i + 1:closing_i])
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
