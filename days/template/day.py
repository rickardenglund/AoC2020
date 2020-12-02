import re


def main():
    print('### day XX ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    inputs = get_input()

    return len(inputs)


def part2():
    inputs = get_input()

    return len(inputs)


def get_input():
    f = open("input.txt", "r")
    contents = f.read()
    f.close()

    pattern = re.compile(r'(\w+) (\w+)')
    matches = pattern.findall(contents)

    return list(
        map(mod_input, matches)
    )


def mod_input(match):
    w1, w2 = match
    return w2, w1



if __name__ == "__main__":
    main()
