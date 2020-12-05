import re
import puzzle


ID_MULTIPLIER = 8


def main():
    print('### day 05 ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    seats = get_input()
    seat_ids = list(map(lambda seat: seat[0] * ID_MULTIPLIER + seat[1], seats))

    return max(seat_ids)


def part2():
    seats = get_input()
    seat_ids = list(map(lambda seat: seat[0] * ID_MULTIPLIER + seat[1], seats))
    seat_ids.sort()

    for i in range(len(seat_ids)):
        if seat_ids[i + 1] == seat_ids[i] + 2:
            return seat_ids[i] + 1


def get_input():
    seat_partitioning = puzzle.input.split('\n')

    return list(
        map(parse, seat_partitioning)
    )


def parse(space_partitioning):
    row_str = space_partitioning[0:7]
    col_str = space_partitioning[7:]

    row_str = row_str.replace('F', '0').replace('B', '1')
    col_str = col_str.replace('R', '1').replace('L', '0')

    return int(row_str, 2), int(col_str, 2)


if __name__ == "__main__":
    main()
