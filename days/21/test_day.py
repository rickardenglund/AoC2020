from unittest import TestCase
import unittest
from day import part1, part2
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(2280, part1(puzzle.input))

    def test_test_part1(self):
        self.assertEqual(5, part1(puzzle.test_input))

    def test_part2(self):
        self.assertEqual('vfvvnm,bvgm,rdksxt,xknb,hxntcz,bktzrz,srzqtccv,gbtmdb', part2(puzzle.input))

    def test_test_part2(self):
        self.assertEqual('mxmxvkd,sqjhc,fvjkl', part2(puzzle.test_input))


if __name__ == '__main__':
    unittest.main()
