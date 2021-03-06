from unittest import TestCase
import unittest
from day import part1, part2
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(32287787075651, part1(puzzle.input))

    def test_test_part1(self):
        self.assertEqual(20899048083289, part1(puzzle.test_input))

    @unittest.skip("Unfinished algorithm")
    def test_part2(self):
        self.assertEqual(2, part2(puzzle.input))

    @unittest.skip("Unfinished algorithm")
    def test_test_part2(self):
        self.assertEqual(273, part2(puzzle.test_input))


if __name__ == '__main__':
    unittest.main()
