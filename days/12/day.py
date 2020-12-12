import re
import puzzle
from datetime import datetime
from ship import Ship
from ship2 import Ship2


def main():
    print('### day 12 ###')
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
    actions = puzzle.input.split('\n')
    ship = Ship()
    for action in actions:
        ship.action(action[0], int(action[1:]))

    return ship.distance()


def part2():
    actions = puzzle.input.split('\n')
    ship = Ship2()
    for action in actions:
        ship.action(action[0], int(action[1:]))

    return round(ship.distance())


if __name__ == "__main__":
    main()
