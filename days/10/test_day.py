from unittest import TestCase
import unittest
import puzzle
from day import part1, part2, get_steps, count, get_input


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(2368, part1())

    def test_part2(self):
        self.assertEqual(1727094849536, part2())

    def test_get_steps(self):
        self.assertEqual(get_steps([0, 1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(get_steps([0, 1, 2, 3, 6], 2), [1])

    def test_count(self):
        self.assertEqual(1, count([0, 1, 2, 3], 3))
        self.assertEqual(1, count([0, 1, 2, 3], 2))
        self.assertEqual(2, count([0, 1, 2, 3], 1))
        smalltest = get_input(puzzle.small)
        self.assertEqual(8, count(smalltest, 0))


if __name__ == '__main__':
    unittest.main()
