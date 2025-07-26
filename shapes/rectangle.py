class Rectangle:

    def __init__(self, corner1, corner2):
        self.x1, self.y1 = corner1
        self.x2, self.y2 = corner2

        if self.x1 == self.x2 or self.y1 == self.y2:
            raise ValueError("Corners must be opposite, only axis-aligned rectangles are supported")

        self.width = abs(self.x2 - self.x1)
        self.height = abs(self.y2 - self.y1)

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
                    raise ValueError("Invalid coordinates")

                if corner1 is None:
                    corner1 = coords
                elif corner2 is None:
                    corner2 = coords
                else:
                    raise ValueError("Too many corners provided for Rectangle")
                i +=3
            else:
                i +=1
        if not all([corner1, corner2]):
            raise ValueError("Rectangle requires exactly 2 corners")

        return cls(corner1, corner2)

