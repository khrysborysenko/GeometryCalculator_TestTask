import math

class Circle:
    def __init__(self, center, coords, radius):
        self.center = center
        self.coords = coords
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def from_tokens(cls, tokens):
        center = None
        coords = None
        radius = None
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.lower() == 'center':
                center = token
                coords = (float(tokens[i+1]), float(tokens[i+2]))
                i += 3
            elif token.lower() == 'radius':
                radius = float(tokens[i+1])
                i += 2
            else:
                i += 1

        if not all([center, coords, radius]):
            raise ValueError('Invalid data')

        return cls(center=center, coords=coords, radius=radius)