import puzzle
from datetime import datetime


def main(input):
    print('### day 25 ###')
    start1 = datetime.now()
    p1res = part1(input)
    stop1 = datetime.now()
    print(f'p1: {p1res}')
    print(f'p1 took: {stop1 - start1}\n')


def part1(input: str) -> int:
    card_public_key, door_public_key = get_input(input)
    card_loop_size = find_loop_size(card_public_key, 7)
    print('card loop size', card_loop_size)
    door_loop_size = find_loop_size(door_public_key, 7)
    print('door loop size', door_loop_size)

    return transform(door_public_key, card_loop_size)


def find_loop_size(public_key, subject_number):
    secret_loop_size = 0
    v = 1
    while v != public_key:
        secret_loop_size += 1
        v = transform_step(v, subject_number)
    return secret_loop_size


def transform(subject_number, loop_size):
    v = 1
    for i in range(loop_size):
        v = transform_step(v, subject_number)
    return v


def transform_step(value, subject_number) -> int:
    value *= subject_number
    return value % 20201227


def get_input(input: str):
    lines = input.split('\n')
    public_key_card = int(lines[0])
    public_key_door = int(lines[1])
    return public_key_card, public_key_door


if __name__ == "__main__":
    main(puzzle.input)
