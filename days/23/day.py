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
    circle = get_input(input)

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
        # print(
        #     f'-- move {move} \n cups {str(circle)} \n pick up: {[c1.Value, c2.Value, c3.Value]} \n destination: {destination}\n\n')
        circle.remove_three()

        circle.insert_after(destination, [c1, c2, c3])
        circle.Head = circle.Head.Next

    circle.Head = circle.find(1)
    return str(circle)[1:]


def part2(input: str) -> int:
    circle = get_input(input)
    circle.extend(1_000_000)

    for move in range(10_000_000):
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

    return -1


class Circle():
    def __init__(self, cups: list[int]):
        self.min = min(cups)
        self.max = max(cups)

        self.Head = Cup(cups[0])

        cur = self.Head
        new = cur
        for i in range(1, len(cups)):
            new = Cup(cups[i])
            cur.Next = new
            cur = new

        new.Next = self.Head

    def extend(self, target):
        cur = self.Head.Next
        while cur.Next != self.Head:
            cur = cur.Next

        for i in range(self.max + 1, target +1):
            cur.Next = Cup(i)
            cur = cur.Next

        cur.Next = self.Head



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
        if self.Head.Value == value:
            return self.Head

        cur = self.Head.Next
        while cur != self.Head:
            if cur.Value == value:
                return cur
            cur = cur.Next

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
    return Circle(list(map(lambda x: int(x), list(input))))


if __name__ == "__main__":
    main(puzzle.input)
