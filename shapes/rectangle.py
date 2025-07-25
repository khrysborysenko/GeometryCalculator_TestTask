class Rectangle:

    def __init__(self, corner1, corner2):
        self.x1, self.y1 = corner1
        self.x2, self.y2 = corner2

    @property
    def width(self):
        return abs(self.x2 - self.x1)

    @property
    def height(self):
        return abs(self.y2 - self.y1)

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def area(self):
        return self.width * self.height

    @classmethod
    def from_tokens(cls, tokens):
        corner1 = None
        corner2 = None

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token in {'TopRight','TopLeft','BottomLeft','BottomRight'}:
                try:
                    coords = (float(tokens[i+1]), float(tokens[i+2]))
                except (IndexError, ValueError):
                    raise ValueError(f"Invalid coordinates {token}")

                if not corner1:
                    corner1 = coords
                else:
                    corner2 = coords
                i +=3
            else:
                i +=1
        if not all([corner1, corner2]):
            raise ValueError(f"Invalid coordinates {tokens}")

        return cls(corner1, corner2)

