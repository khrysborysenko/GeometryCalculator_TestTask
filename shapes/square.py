class Square:

    def __init__(self, position, coords, side):
        self.position = position
        self.coords = coords
        self.side = side

    @property
    def perimeter(self):
        return 4 * self.side

    @property
    def area(self):
        return self.side ** 2

    @classmethod
    def from_tokens(cls, tokens):
        position = None
        coords = None
        side = None

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token in {'TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'}:
                position = token
                coords = (float(tokens[i+1]), float(tokens[i+2]))
                i += 3
            elif token == 'Side':
                side = float(tokens[i+1])
                i += 2
            else:
                i += 1

        if not all([position, coords, side]):
            raise ValueError("Invalid data")

        return cls(position=position, coords=coords, side=side)






