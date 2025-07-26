import math

class Circle:
    def __init__(self, center, coords, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        if not (isinstance(coords, tuple) and len(coords) == 2 and all(isinstance(c, (int, float)) for c in coords)):
            raise ValueError("Center must have exactly two numeric coordinates")

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
            token = tokens[i].lower()

            if token == 'center':
                try:
                    coords = (float(tokens[i+1]), float(tokens[i+2]))
                except(IndexError, ValueError):
                    raise ValueError("Invalid coordinates of center")
                center = 'Center'
                i += 3
            elif token.lower() == 'radius':
                try:
                    radius = float(tokens[i+1])
                except(IndexError, ValueError):
                    raise ValueError("Invalid radius of circle")
                i += 2
            else:
                i += 1

        if not all([center, coords, radius]):
            raise ValueError('Missing center coordinates or radius')

        return cls(center=center, coords=coords, radius=radius)