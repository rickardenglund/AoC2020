def main():
    print('### day XX ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    f = open("input.txt", "r")
    contents = f.readlines()
    f.close()

    return len(contents)


def part2():
    return -2


if __name__ == "__main__":
    main()
