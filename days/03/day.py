import re
import puzzle


def main():
    print('### day 03 ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    lines = puzzle.input.split('\n')

    cur_x = 0
    n_trees =0
    for y in range(len(lines)):
        if lines[y][cur_x] == '#':
            n_trees += 1
        cur_x = (cur_x + 3) % len(lines[y])

    return n_trees


def part2():
    lines = puzzle.input.split('\n')
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

    product = 1
    for (x_step, y_step) in slopes:
        cur_x = 0
        cur_y = 0
        n_trees =0
        while cur_y < len(lines):
            if lines[cur_y][cur_x] == '#':
                n_trees += 1
            cur_x = (cur_x + 3) % len(lines[cur_y])
            cur_y += y_step
        product *= n_trees

    return product


if __name__ == "__main__":
    main()
