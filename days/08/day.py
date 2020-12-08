import re
import puzzle
from datetime import datetime
from enum import Enum


def main():
    print('### day 08 ###')
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
    program = read_program()

    return run_program(program)[1]


class State(Enum):
    COMPLETED = 0
    LOOP = 1


def run_program(program):
    visited = set()
    ip = 0
    acc = 0
    while not ip in visited:
        if ip >= len(program):
            return (State.COMPLETED, acc)
        visited.add(ip)
        if program[ip][0] == 'acc':
            acc += program[ip][1]
            ip += 1
        elif program[ip][0] == 'jmp':
            ip += program[ip][1]
        elif program[ip][0] == 'nop':
            ip += 1

    return (State.LOOP, acc)


def part2():
    program = read_program()

    for line_i in range(len(program)):
        altered_program = program.copy()
        if program[line_i][0] == 'nop':
            altered_program[line_i] = ('jmp', program[line_i][1])
        elif program[line_i][0] == 'jmp':
            altered_program[line_i] = ('nop', program[line_i][1])
        else:
            continue

        state, acc = run_program(altered_program)
        if state == State.LOOP:
            continue
        elif state == State.COMPLETED:
            return acc


def read_program():
    lines = puzzle.input.split('\n')
    lineparts = (line.split(' ') for line in lines)
    program = [(parts[0], int(parts[1])) for parts in lineparts]
    return program


if __name__ == "__main__":
    main()
