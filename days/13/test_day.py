from unittest import TestCase
import unittest
from day import part1, part2, is_valid, get_rules, find_earliest_match
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(1, part1(puzzle.input))

    def test_part2(self):
        self.assertEqual(2, part2(puzzle.input))

    def test_is_valid(self):
        rules = get_rules(puzzle.test_input.split('\n')[1])
        self.assertFalse(is_valid(rules, 545))
        self.assertTrue(is_valid(rules, 1068781))

    def test_earliest_match(self):
        self.assertEqual(754018, find_earliest_match('67,7,59,61'))
        self.assertEqual(3417, find_earliest_match('17,x,13,19'))
        self.assertEqual(779210, find_earliest_match('67,x,7,59,61'))
        self.assertEqual(1261476, find_earliest_match('67,7,x,59,61'))
        self.assertEqual(1202161486, find_earliest_match('1789,37,47,1889'))


if __name__ == '__main__':
    unittest.main()
