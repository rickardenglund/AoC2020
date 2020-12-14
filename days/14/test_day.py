from unittest import TestCase
import unittest
from day import part1, part2, apply, get_bit, get_addresses
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(15919415426101, part1(puzzle.input))

    def test_test_part1(self):
        self.assertEqual(165, part1(puzzle.test_input))

    def test_apply(self):
        self.assertEqual(73, apply('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11))

    def test_get_bit(self):
        self.assertEqual(1, get_bit(0b101, 0))
        self.assertEqual(0, get_bit(0b101, 1))
        self.assertEqual(1, get_bit(0b101, 2))
        self.assertEqual(0, get_bit(0b101, 3))

    def test_part2(self):
        self.assertEqual(3443997590975, part2(puzzle.input))

    def test_test_part2(self):
        self.assertEqual(208, part2(puzzle.test2_input))

    def test_get_addresses(self):
        self.assertEqual({26, 27, 58, 59}, get_addresses('000000000000000000000000000000X1001X', 42))


if __name__ == '__main__':
    unittest.main()
