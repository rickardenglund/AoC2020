import puzzle


def do(string):
    symbols = parse_symbols(string)
    polish = shutting_yard_algorithm(symbols)
    res = evaluate(polish)
    return (res)


OP_MUL = '*'
OP_PLUS = '+'
OPERATOR_PRECEDENCE = {OP_PLUS: 1, OP_MUL: 2}
PAREN_START = '('
PAREN_STOP = ')'


def parse_symbols(string):
    parts: list[str] = list(string)
    symbols = []
    for p in parts:
        p = p.strip()
        if len(p) == 0:
            continue
        if p.isdigit():
            symbols.append(int(p))
            continue
        if p in [OP_MUL, OP_PLUS, PAREN_START, PAREN_STOP]:
            symbols.append(p)
            continue
        raise Exception('invalid symbol', p)
    return symbols


# implementation of https://sv.wikipedia.org/wiki/Järnvägsalgoritmen
# return reverse polish notation
def shutting_yard_algorithm(symbols):
    out = []
    stack = []
    for i in range(len(symbols)):
        sym = symbols[i]
        if isinstance(sym, int):
            out.append(sym)
            continue
        if sym in OPERATOR_PRECEDENCE:
            while len(stack) > 0 \
                    and not stack[len(stack) - 1] == PAREN_START \
                    and OPERATOR_PRECEDENCE[sym] > OPERATOR_PRECEDENCE[stack[len(stack) - 1]]:
                op = stack.pop()
                if op == PAREN_STOP:
                    break
                out.append(op)
            stack.append(sym)
            continue
        if sym == PAREN_START:
            stack.append(sym)
            continue
        if sym == PAREN_STOP:
            while stack[len(stack) - 1] != PAREN_START:
                op = stack.pop()
                out.append(op)
            stack.pop()
            continue
    while len(stack) > 0:
        op = stack.pop()
        if op in [PAREN_STOP, PAREN_START]:
            raise Exception('missmatched parenthesis')
        out.append(op)

    return out


def evaluate(ast: list) -> int:
    stack = []
    for sym in ast:
        if isinstance(sym, int):
            stack.append(sym)
        elif sym == OP_MUL:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 * v2)
        elif sym == OP_PLUS:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 + v2)
    return stack.pop()


if __name__ == '__main__':
    for input in puzzle.test.split('\n'):
        print(input, '=', do(input))
    print(sum([do(input) for input in puzzle.input.split('\n')]))
