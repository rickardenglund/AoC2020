from unittest import TestCase
import unittest
from day import part1, part2, starts_with, get_input
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(-1, part1(puzzle.input))

    def test_test_part1(self):
        self.assertEqual(113, part1(puzzle.test_input))

    def test_test_part1_small(self):
        self.assertEqual(2, part1(puzzle.test_small))

    def test_test_part1_simple(self):
        self.assertEqual(1, part1(puzzle.test_simple))

    def test_part2(self):
        self.assertEqual(2, part2(puzzle.input))

    def test_starts_with_simple(self):
        rules, messages = get_input(puzzle.test_simple)

        s, match = starts_with(rules, 1, 'apa')
        self.assertTrue(match)

        s, match = starts_with(rules, 1, 'bpa')
        self.assertFalse(match)

        s, match = starts_with(rules, 0, 'aba')
        self.assertTrue(match)
        self.assertEqual(s, 'aba')

        s, match = starts_with(rules, 0, 'abb')
        self.assertFalse(match)
        self.assertEqual(s, '')

    def test_starts_with_simple(self):
        rules, messages = get_input(puzzle.test_small)

        s, match = starts_with(rules, 0, 'aba')
        self.assertTrue(match)
        self.assertEqual(s, 'aba')

        s, match = starts_with(rules, 0, 'aab')
        self.assertTrue(match)
        self.assertEqual(s, 'aab')


if __name__ == '__main__':
    unittest.main()
