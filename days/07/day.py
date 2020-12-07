import re
import puzzle
from datetime import datetime


def main():
    print('### day 07 ###')
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
    tree = get_input()
    count = 0
    for k in tree:
        if contains(tree, k, 'shiny gold'):
            count += 1
    return count - 1 # remove shiny gold


def contains(tree, key, target):
    if key == target:
        return True

    if len(tree[key]) == 0:
        return False
    else:
        return any([contains(tree, color, target) for (n, color) in tree[key]])





def part2():
    inputs = get_input()

    return len(inputs)


def get_input():
    tree = {}
    for line in puzzle.input.split('\n'):
        words = line.split(' ')
        color = f'{words[0]} {words[1]}'
        if line.__contains__("no other bags"):
            tree[color] = []
        else:
            line = line[line.find('contain') + 8:]
            line = line.removesuffix('.')
            contents = line.split(', ')
            content_list = []
            for content in contents:
                content = content.split(' ')
                n = int(content[0])
                content_color = f'{content[1]} {content[2]}'
                content_list.append((n, content_color))

            tree[color] = content_list
    return tree




def mod_input(match):
    w1, w2 = match
    return w2, w1


if __name__ == "__main__":
    main()
