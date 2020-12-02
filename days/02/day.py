import re
import puzzle


def main():
    print('### day 02 ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    n_valid = 0
    input = get_input()
    for (letter, min, max, password) in input:
        if valid(password, min, max, letter):
            n_valid += 1

    return n_valid


def valid(password, min, max, letter):
    return min <= password.count(letter) <= max


def part2():
    n_valid = 0
    input = get_input()
    for (letter, min, max, password) in input:
        if valid2(password, min, max, letter):
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
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w*)\n')
    matches = pattern.findall(puzzle.input)

    passwords = []
    for (min, max, letter, password) in matches:
        passwords.append((letter, int(min), int(max), password))

    return passwords


if __name__ == "__main__":
    main()
