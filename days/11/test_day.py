from unittest import TestCase
import unittest
from day import part1, part2, get_input, next_round, count_immediate_neighbours, spot_outcome


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(2344, part1())

    def test_part2(self):
        self.assertEqual(2076, part2())

    def test_nex_round(self):
        before = get_input('''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##''')
        after = get_input('''#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##''')
        print(after)
        print(next_round(before, count_immediate_neighbours,
                         lambda current, neighbours: spot_outcome(current, neighbours, 4)))


if __name__ == '__main__':
    unittest.main()
