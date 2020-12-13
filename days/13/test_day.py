from unittest import TestCase
import unittest
from day import part1, part2, get_rules, find_earliest_match, is_prime
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(171, part1(puzzle.input))

    def test_part2(self):
        self.assertEqual(539746751134958, part2(puzzle.input))

    def test_earliest_match(self):
        self.assertEqual(754018, find_earliest_match('67,7,59,61'))
        self.assertEqual(3417, find_earliest_match('17,x,13,19'))
        self.assertEqual(779210, find_earliest_match('67,x,7,59,61'))
        self.assertEqual(1261476, find_earliest_match('67,7,x,59,61'))
        self.assertEqual(1202161486, find_earliest_match('1789,37,47,1889'))

    def test_is_prime(self):
        self.assertTrue(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(43))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(55))


if __name__ == '__main__':
    unittest.main()
