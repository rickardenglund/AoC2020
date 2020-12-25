from unittest import TestCase
import unittest
from day import part1
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(4126980, part1(puzzle.input))

    def test_test_part1(self):
        self.assertEqual(14897079, part1(puzzle.test_input))

if __name__ == '__main__':
    unittest.main()
