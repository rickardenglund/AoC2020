from unittest import TestCase
from ship import dir_to_letter, Ship, NORTH, WEST, EAST, SOUTH


class Test(TestCase):
    def test_dir_to_letter(self):
        ship = Ship()
        self.assertEqual(EAST, ship.face)

        ship.action('R', 90)
        self.assertEqual(SOUTH, ship.face)
