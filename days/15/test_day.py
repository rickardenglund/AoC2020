from unittest import TestCase
import unittest
from day import part1, part2
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(595, part1(puzzle.input))

    def test_part2(self):
        self.assertEqual(1708310, part2(puzzle.input))


if __name__ == '__main__':
    unittest.main()
