import puzzle
from datetime import datetime


def main(input):
    print('### day 23 ###')
    start1 = datetime.now()
    p1res = part1(input)
    stop1 = datetime.now()
    print(f'p1: {p1res}')

    start2 = datetime.now()
    p2res = part2(input)
    stop2 = datetime.now()
    print(f'p2: {p2res}')

    print(f'p1 took: {stop1 - start1}\np2 took: {stop2 - start2}')


def part1(input: str) -> str:
    numbers = get_input(input)
    circle = Circle(numbers)

    for move in range(100):
        current = circle.get(0)
        c1 = circle.get(1)
        c2 = circle.get(2)
        c3 = circle.get(3)

        destination = current.Value - 1
        if destination < circle.min:
            destination = circle.max

        while destination in [c1.Value, c2.Value, c3.Value]:
            destination -= 1
            if destination < circle.min:
                destination = circle.max

        destination = circle.find(destination)
        circle.remove_three()

        circle.insert_after(destination, [c1, c2, c3])
        circle.Head = circle.Head.Next

    circle.Head = circle.find(1)
    return str(circle)[1:]


def part2(input: str) -> int:
    numbers = get_input(input)
    circle = Circle(numbers)
    circle.extend(1_000_000)

    for move in range(10_000_000):
        if move % 1_000_000 == 0:
            print(move)
        current = circle.get(0)
        c1 = circle.get(1)
        c2 = circle.get(2)
        c3 = circle.get(3)

        destination = current.Value - 1
        if destination < circle.min:
            destination = circle.max

        while destination in [c1.Value, c2.Value, c3.Value]:
            destination -= 1
            if destination < circle.min:
                destination = circle.max

        destination = circle.find(destination)
        circle.remove_three()

        circle.insert_after(destination, [c1, c2, c3])
        circle.Head = circle.Head.Next

    circle.Head = circle.find(1)
    first_star = circle.get(1).Value
    seconds_start = circle.get(2).Value

    print(first_star, seconds_start, first_star * seconds_start)

    return first_star * seconds_start


class Circle():
    def __init__(self, cups: list[int]):
        self.min = min(cups)
        self.max = max(cups)
        self.Head = 0

        self.Head = Cup(cups[0])
        self.value_index = {cups[0]: self.Head}

        cur = self.Head
        new = cur
        for i in range(1, len(cups)):
            new = Cup(cups[i])
            self.value_index[cups[i]] = new
            cur.Next = new
            cur = new

        new.Next = self.Head

    def extend(self, target):
        cur = self.Head.Next
        while cur.Next != self.Head:
            cur = cur.Next

        for i in range(self.max + 1, target + 1):
            cur.Next = Cup(i)
            self.value_index[i] = cur.Next
            cur = cur.Next

        cur.Next = self.Head
        self.max = target

    def __str__(self):
        res = str(self.Head.Value)
        cur = self.Head.Next

        while cur and cur != self.Head:
            res += str(cur.Value)
            cur = cur.Next
        return res

    def get(self, index):
        cur = self.Head
        for i in range(index):
            cur = cur.Next
        return cur

    def find(self, value):
        return self.value_index[value]
        # if self.Head.Value == value:
        #     return self.Head
        #
        # cur = self.Head.Next
        # while cur != self.Head:
        #     if cur.Value == value:
        #         return cur
        #     cur = cur.Next

    def remove_three(self):
        self.Head.Next = self.Head.Next.Next.Next.Next

    def insert_after(self, destination, values: list[int]):
        old_next = destination.Next
        cur = destination
        for v in values:
            cur.Next = v
            cur = v
        cur.Next = old_next


class Cup():
    def __init__(self, value):
        self.Value = value
        self.Next = None

    def __str__(self):
        return str(self.Value)


def get_input(input: str):
    return list(map(lambda x: int(x), list(input)))


if __name__ == "__main__":
    main(puzzle.input)
