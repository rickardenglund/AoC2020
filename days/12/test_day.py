from unittest import TestCase
import unittest
from day import part1, part2


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(1601, part1())

    def test_part2(self):
        self.assertEqual(13340, part2())


if __name__ == '__main__':
    unittest.main()
