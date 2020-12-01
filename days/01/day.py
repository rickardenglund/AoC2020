def main():
    print('### day 01 ###')

    print('p1:', part1())
    print('p2:', part2())


TARGET = 2020


def part1():
    f = open("input.txt", "r")
    contents = f.readlines()
    f.close()

    contents = list(map(lambda x : int(x), contents))

    for i in contents:
        for j in contents:
            if i + j == TARGET:
                return i * j

    raise Exception('No answer')


def part2():
    f = open("input.txt", "r")
    contents = f.readlines()
    f.close()

    contents = list(map(lambda x : int(x), contents))

    for i in contents:
        for j in contents:
            for k in contents:
                if i + j + k == TARGET:
                    return i * j * k

    raise Exception('No answer')


if __name__ == "__main__":
    main()
