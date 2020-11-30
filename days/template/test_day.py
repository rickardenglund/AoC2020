from unittest import TestCase
from day import part1, part2


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(2, part1())

    def test_part2(self):
        self.assertEqual(-2, part2())
