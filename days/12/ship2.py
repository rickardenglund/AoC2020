import math


class Ship2():
    def __init__(self, waypoint_x=10, waypoint_y=1):
        self.waypoint_y = waypoint_y
        self.waypoint_x = waypoint_x

    x = 0
    y = 0

    def action(self, action, value):
        if action == 'W':
            self.waypoint_x -= value
        elif action == 'N':
            self.waypoint_y += value
        elif action == 'E':
            self.waypoint_x += value
        elif action == 'S':
            self.waypoint_y -= value
        elif action == 'L':
            dist, angle_rad = cart2pol(self.waypoint_x, -self.waypoint_y)
            angle_rad -= math.radians(value)
            x, y = pol2cart(dist, angle_rad)
            self.waypoint_x = x
            self.waypoint_y = -y
        elif action == 'R':
            dist, angle_rad = cart2pol(self.waypoint_x, -self.waypoint_y)
            angle_rad += math.radians(value)
            x, y = pol2cart(dist, angle_rad)
            self.waypoint_x = x
            self.waypoint_y = -y
        elif action == 'F':
            dist, angle_rad = cart2pol(self.waypoint_x, self.waypoint_y)
            dist *= value
            dx, dy = pol2cart(dist, angle_rad)
            self.x += dx
            self.y += dy

        # print((action, value), (self.x, self.y), (self.waypoint_x, self.waypoint_y))

    def distance(self) -> int:
        return abs(self.x) + abs(self.y)


def cart2pol(x, y):
    rho = math.sqrt(x ** 2 + y ** 2)
    phi = math.atan2(y, x)
    return (rho, phi)


def pol2cart(rho, phi):
    x = rho * math.cos(phi)
    y = rho * math.sin(phi)
    return (x, y)
