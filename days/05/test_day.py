from unittest import TestCase
import unittest
from day import part1, part2, parse


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(828, part1())

    def test_part2(self):
        self.assertEqual(565, part2())

    def test_parse(self):
        self.assertEqual((70, 7), parse('BFFFBBFRRR'))
        self.assertEqual((100, 5), parse('BBFFBFFRLR'))


if __name__ == '__main__':
    unittest.main()
