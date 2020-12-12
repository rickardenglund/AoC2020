from unittest import TestCase
from ship2 import Ship2


class TestShip2(TestCase):
    def test_action(self):
        ship = Ship2()
        ship.action('R', 180)
        self.assertAlmostEqual(-10, ship.waypoint_x)
        self.assertAlmostEqual(-1, ship.waypoint_y)

        ship.action('L', 180)
        self.assertAlmostEqual(10, ship.waypoint_x)
        self.assertAlmostEqual(1, ship.waypoint_y)

    def test_action_r90(self):
        ship = Ship2(10, 1)
        ship.action('R', 90)
        self.assertAlmostEqual(1, ship.waypoint_x)
        self.assertAlmostEqual(-10, ship.waypoint_y)
