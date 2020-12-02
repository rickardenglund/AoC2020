from unittest import TestCase
import unittest
from dayx import part1, part2


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(2, part1())

    def test_part2(self):
        self.assertEqual(2, part2())



if __name__ == '__main__':
    unittest.main()
