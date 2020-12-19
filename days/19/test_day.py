from unittest import TestCase
import unittest
from day import part1, part2
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(-1, part1(puzzle.input))

    def test_test_part1(self):
        self.assertEqual(2, part1(puzzle.test_input))

    def test_test_part1_small(self):
        self.assertEqual(2, part1(puzzle.test_small))

    def test_test_part1_simple(self):
        self.assertEqual(1, part1(puzzle.test_simple))

    def test_part2(self):
        self.assertEqual(2, part2(puzzle.input))


if __name__ == '__main__':
    unittest.main()
