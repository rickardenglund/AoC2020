from unittest import TestCase
from day import part1, part2, valid


class Test(TestCase):
    def test_count(self):
        self.assertTrue(valid('asdf', 1, 3, 'a'))
        self.assertFalse(valid('asdf', 1, 3, 'b'))
        self.assertFalse(valid('asaaaadf', 1, 3, 'a'))
