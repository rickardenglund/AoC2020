from unittest import TestCase
import unittest
from day import part1, part2, is_valid


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(104054607, part1())

    def test_part2(self):
        self.assertEqual(13935797, part2())

    def test_is_valid(self):
        numbers = list(range(1, 6))
        self.assertTrue(is_valid(6, numbers, 5))
        self.assertFalse(is_valid(10, numbers, 5))


if __name__ == '__main__':
    unittest.main()
