from unittest import TestCase
import unittest
from day import part1, part2, evaluate, parse
import puzzle


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(75592527415659, part1(puzzle.input))

    def test_part2(self):
        self.assertEqual(2, part2(puzzle.input))

    def test_eval(self):
        self.assertEqual(71, evaluate(parse('1 + 2 * 3 + 4 * 5 + 6')))

    def test_given(self):
        self.assertEqual(26, evaluate(parse('2 * 3 + (4 * 5)')))
        self.assertEqual(437, evaluate(parse('5 + (8 * 3 + 9 + 3 * 4 * 3)')))
        self.assertEqual(12240, evaluate(parse('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')))
        self.assertEqual(13632, evaluate(parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')))

    def test_eval_paren(self):
        self.assertEqual(26, evaluate(parse('2 * 3 + (4 * 5)')))
        self.assertEqual(7, evaluate(parse('(1 + (2 * 3))')))

    def test_eval_paren(self):
        # self.assertEqual(26, evaluate(parse('2 * 3 + (4 * 5)')))
        self.assertEqual(7, evaluate([1, '+', [2, '*', 3]]))

    def test_eval_parse_left(self):
        self.assertEqual(3, evaluate(parse('((1 * 2) + 1)')))

    def test_eval_parse_2(self):
        self.assertEqual(7, evaluate(parse('(3)*(2)+1')))

    def test_eval_parse_4(self):
        self.assertEqual(7, evaluate(parse('(3)* (2) + 1')))

    def test_eval_parse_3(self):
        self.assertEqual(3, evaluate(parse('(2) + 1')))

    def test_eval_only_large(self):
        self.assertEqual(54 * 126, evaluate([[2, '+', 4, '*', 9], '*', [6, '+', 9, '*', 8, '+', 6]]))
        # self.assertEqual(54 * 126 + 6, evaluate(parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6)')))
        # self.assertEqual(13632, evaluate(parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')))

    def test_eval_large(self):
        self.assertEqual(54 * ((6+9)*8 + 6), evaluate(parse('(2 + 4 * 9) * (6 + 9 * 8 + 6)')))
        self.assertEqual(54 * 126 + 6, evaluate(parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6)')))
        self.assertEqual(13632, evaluate(parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')))

    def test_parse(self):
        self.assertEqual([1, '+', 2, '*', 3, '+', 4, '*', 5, '+', 6], parse('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual([[1, ' +', [2, '*', 3]]], parse('(1 + (2 * 3))'))

    def test_parse(self):
        self.assertEqual([1, '+', 2, '*', 3, '+', 4, '*', 5, '+', 6], parse('1 + 2 * 3 + 4 * 5 + 6'))

    def test_parse_large12(self):
        self.assertEqual(2, parse('(2 + 4 * 9) * (6 + 9 * 8 + 6)'))

    def test_parse_paren_left(self):
        self.assertEqual(2, parse('((1 + 2) * 3)'))


if __name__ == '__main__':
    unittest.main()
