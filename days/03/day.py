import re
import puzzle


def main():
    print('### day 03 ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    map = puzzle.input.split('\n')
    x_step = 3
    y_step = 1

    n_trees = count_slope(map, x_step, y_step)

    return n_trees


def part2():
    map = puzzle.input.split('\n')
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    product = 1
    for (x_step, y_step) in slopes:
        product *= count_slope(map, x_step, y_step)

    return product


def count_slope(map, x_step, y_step):
    # print('slope', x_step, y_step)
    cur_x = 0
    cur_y = 0
    n_trees = 0
    while cur_y < len(map):
        # print('pos:', cur_x, cur_y)
        if map[cur_y][cur_x] == '#':
            n_trees += 1
        cur_x = (cur_x + x_step) % len(map[cur_y])
        cur_y += y_step
    return n_trees


if __name__ == "__main__":
    main()
