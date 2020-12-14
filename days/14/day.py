import re
import puzzle
from datetime import datetime


def main(input):
    print('### day 14 ###')
    start1 = datetime.now()
    p1res = part1(input)
    stop1 = datetime.now()
    print(f'p1: {p1res}')

    start2 = datetime.now()
    p2res = part2(input)
    stop2 = datetime.now()
    print(f'p2: {p2res}')

    print(f'p1 took: {stop1 - start1}\np2 took: {stop2 - start2}')


def apply(mask: str, raw_value: int) -> int:
    out = raw_value
    for i in range(len(mask)):
        mask_i = len(mask) - (i + 1)
        if mask[mask_i] == '1':
            out = set_bit(out, i)
        if mask[mask_i] == '0':
            out = clear_bit(out, i)
        if mask[mask_i] == 'X':
            continue
    return out


def get_bit(n, i):
    mask = 1 << i
    res = (mask & n) >> i
    return res


def set_bit(value, bit):
    return value | (1<<bit)


def clear_bit(value, bit):
    return value & ~(1<<bit)
# def set_bit(n, i):
#     mask = 1 << i
#     return  mask | n
#
#
# def unset_bit(n, i):
#     mask = 1 << i
#     return  mask & n


def part1(input: str) -> int:
    mask_pattern = re.compile(r'mask = ([X01]+)')
    set_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')

    mask = 'no mask'
    mem: dict[int, int] = {}
    lines = input.split('\n')
    for line in lines:
        if line.startswith("mask"):
            match = mask_pattern.match(line)
            mask = match.groups()[0]
        if line.startswith('mem'):
            match = set_pattern.match(line)
            address = int(match.groups()[0])
            raw_value = int(match.groups()[1])
            mem[address] = apply(mask, raw_value)

    sum = 0
    for k in mem.keys():
        sum += mem[k]
    return sum


def part2(input: str) -> int:
    mask_pattern = re.compile(r'mask = ([X01]+)')
    set_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')

    mask = 'no mask'
    mem: dict[int, int] = {}
    lines = input.split('\n')
    for line in lines:
        if line.startswith("mask"):
            match = mask_pattern.match(line)
            mask = match.groups()[0]
        if line.startswith('mem'):
            match = set_pattern.match(line)
            address = int(match.groups()[0])
            value = int(match.groups()[1])
            addresses = get_addresses(mask, address)
            for address in addresses:
                mem[address] = value

    sum = 0
    for k in mem.keys():
        sum += mem[k]
    return sum


def get_addresses(mask: str, raw_address: int) -> set[int]:
    floating_address = ['0'] * len(mask)

    binary_string = list("{0:b}".format(raw_address))
    for i in range(len(binary_string)):
        floating_address[len(floating_address) - len(binary_string) + i] = binary_string[i]

    for i in range(len(mask)):
        if mask[i] == '1':
            floating_address[i] = '1'
        if mask[i] == '0':
            continue
        if mask[i] == 'X':
            floating_address[i] = 'X'

    addresses = do_float(floating_address)
    out = set()
    for a in addresses:
        a = ''.join(a)
        out.add(int(a,2))

    return out


def do_float(floating_address: list[str]):
    for i in range(len(floating_address)):
        if floating_address[i] == 'X':
            l1 = floating_address.copy()
            l1[i] = '1'

            l0 = floating_address.copy()
            l0[i] = '0'

            return do_float(l1) + do_float(l0)

    return [floating_address]

if __name__ == "__main__":
    main(puzzle.input)
