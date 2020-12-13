import puzzle
from datetime import datetime


def main(input):
    print('### day 13 ###')
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
    ticket, ids = get_input(input)
    wait_times = [(id, (id * (ticket // id) + id) % ticket) for id in ids]
    wait_times = sorted(wait_times, key=lambda tuple: tuple[1])

    return wait_times[0][0] * wait_times[0][1]


def get_input(input: str) -> [int, list[int]]:
    lines = input.split('\n')
    ids = [int(id) for id in lines[1].split(',') if id != 'x']
    return int(lines[0]), ids


def part2(input: str) -> int:
    return find_earliest_match(input.split('\n')[1])


def find_earliest_match(input: str) -> int:
    rules = get_rules(input)

    if not all((is_prime(id) for (offset, id) in rules)):
        raise Exception('not all primes')

    t = 0
    step_size = 1
    for (offset, id) in rules:
        while not ((t + offset) % id == 0):
            t += step_size

        step_size *= id
        # print(f't: {t}, step_size: {step_size}, {(offset, id)}')

    return t


def get_rules(input):
    rules = []
    ids = input.split(',')
    for i in range(len(ids)):
        if ids[i] == 'x':
            continue
        rules.append((i, int(ids[i])))
    return rules


def is_prime(num):
    if num == 1:
        return True
    if num > 1:
        for i in range(2, num//2 + 1):
            if (num % i) == 0:
                return False

        return True
    else:
        return False



if __name__ == "__main__":
    main(puzzle.input)
