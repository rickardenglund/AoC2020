import functools


def main():
    print('### day 02 ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    n_valid = 0
    input = get_input()
    for (letter, limits, password) in input:
        if valid(password, int(limits[0]), int(limits[1]), letter):
            n_valid += 1

    return n_valid


def valid(password, min, max, letter):
    counts = functools.reduce(count_letter, password, {})
    count = counts.get(letter, 0)

    return min <= count <= max


def count_letter(agg, letter):
    new_count = agg.get(letter, 0) + 1
    agg[letter] = new_count

    return agg


def part2():
    n_valid = 0
    input = get_input()
    for (letter, limits, password) in input:
        if valid2(password, int(limits[0]), int(limits[1]), letter):
            n_valid += 1

    return n_valid


def valid2(password, first_i, second_i, letter):
    try:
        first = password[first_i - 1] == letter
        second = password[second_i - 1] == letter
        return first != second
    except Exception as e:
        print('error', password, first_i, second_i, letter)
        raise e


def get_input():
    f = open("input.txt", "r")
    contents = f.readlines()
    f.close()

    passwords = []
    for line in contents:
        line = line.split()
        limits = line[0].split('-')
        letter = line[1][0]
        password = line[2]

        passwords.append((letter, limits, password))
    return passwords


if __name__ == "__main__":
    main()
