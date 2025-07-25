import math

class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    @property
    def side_a(self):
        return math.dist(self.point1, self.point2)

    @property
    def side_b(self):
        return math.dist(self.point2, self.point3)

    @property
    def side_c(self):
        return math.dist(self.point3, self.point1)

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        a, b, c = self.side_a, self.side_b, self.side_c
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @classmethod
    def from_tokens(cls, tokens):
        point1 = None
        point2 = None
        point3 = None
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in {'Point1', 'Point2', 'Point3'}:
                try:
                    coords = (float(tokens[i+1]), float(tokens[i+2]))
                except (IndexError, ValueError):
                    raise ValueError('Invalid coordinates')

                if token == 'Point1':
                    point1 = coords
                elif token == 'Point2':
                    point2 = coords
                elif token == 'Point3':
                    point3 = coords

                i += 3
            else:
                i += 1

        if not all([point1, point2, point3]):
            raise ValueError('Invalid data')

        return cls(point1, point2, point3)

