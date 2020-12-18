from unittest import TestCase
import unittest
from shunting_yard import do
import puzzle


class Test(TestCase):
    def test_given_p2(self):
        self.assertEqual(231, do('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual(51, do('1 + (2 * 3) + (4 * (5 + 6))'))
        self.assertEqual(46, do('2 * 3 + (4 * 5)'))
        self.assertEqual(1445, do('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
        self.assertEqual(669060, do('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
        self.assertEqual(23340, do('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))


if __name__ == '__main__':
    unittest.main()
