NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Ship():
    x = 0
    y = 0
    face = EAST

    def action(self, action, value):
        if action == 'W':
            self.x -= value
        elif action == 'N':
            self.y += value
        elif action == 'E':
            self.x += value
        elif action == 'S':
            self.y -= value
        elif action == 'L':
            self.face = (self.face + 3*value/90) % 4
        elif action == 'R':
            self.face = (self.face + 1*value/90) % 4
        elif action == 'F':
            self.action(dir_to_letter(self.face), value)

    def distance(self) -> int:
        return abs(self.x) + abs(self.y)


def dir_to_letter(face: int) -> str:
    translation = {EAST: 'E', NORTH: 'N', WEST: 'W', SOUTH: 'S'}
    return translation[face]
