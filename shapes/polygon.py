import math

class Polygon:
    def __init__(self, points):
        self.points = points


    @property
    def perimeter(self):
        if len(self.points) == 2:
            side_a = math.dist(self.points[0], self.points[1])
            side_b = math.dist(self.points[1], self.points[0])
            return side_a + side_b
        elif len(self.points) == 3:
            side_a = math.dist(self.points[0], self.points[1])
            side_b = math.dist(self.points[1], self.points[2])
            side_c = math.dist(self.points[2], self.points[0])
            return side_a + side_b + side_c
