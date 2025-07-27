import math

class Polygon:
    def __init__(self, points):
        self.points = points


    @property
    def perimeter(self):
        i = 0
        side = []
        while i < len(self.points):
            if i == (len(self.points) - 1):
                side.append(math.dist(self.points[i], self.points[0]))
                break
            else:
                side.append(math.dist(self.points[i], self.points[i+1]))
                i += 1
        return sum(side)