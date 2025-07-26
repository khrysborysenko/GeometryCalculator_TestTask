import math

class Triangle:
    def __init__(self, point1, point2, point3):
        for idx, pt in enumerate([point1, point2, point3], start=1):
            if not (isinstance(pt, tuple) and len(pt) == 2 and all(isinstance(c, (int, float)) for c in pt)):
                raise ValueError("Points must have two numeric coordinates")

        if point1 == point2 or point2 == point3 or point3 == point1:
            raise ValueError("Points must be distinct")

        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3
        triangle_area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
        if triangle_area == 0:
            raise ValueError("Points cannot be collinear")

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
                    raise ValueError("Invalid coordinates")

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
            raise ValueError("Triangle must have exactly three points")

        return cls(point1, point2, point3)

