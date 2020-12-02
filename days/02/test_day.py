from unittest import TestCase
import unittest
from day import part1, part2, valid


class Test(TestCase):
    def test_parts(self):
        self.assertEqual(645, part1())
        self.assertEqual(737, part2())

    def test_count(self):
        self.assertTrue(valid('asdf', 1, 3, 'a'))
        self.assertFalse(valid('asdf', 1, 3, 'b'))
        self.assertFalse(valid('asaaaadf', 1, 3, 'a'))


if __name__ == '__main__':
    unittest.main()
