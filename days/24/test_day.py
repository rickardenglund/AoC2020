from unittest import TestCase
import unittest
from day import part1, part2
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(356, part1(puzzle.input))

    def test_test_part1(self):
        self.assertEqual(10, part1(puzzle.test_input))

    def test_part2(self):
        self.assertEqual(3887, part2(puzzle.input))

    def test_test_part2(self):
        self.assertEqual(2208, part2(puzzle.test_input))


if __name__ == '__main__':
    unittest.main()
