class Square:

    def __init__(self, position, coords, side):   #initialize square
        self.position = position
        self.position = position
        self.coords = coords
        self.side = side

    @property
    def perimeter(self):   #calculate the perimeter
        return 4 * self.side

    @property
    def area(self):   #calculate the area
        return self.side ** 2

    @classmethod
    def from_tokens(cls, tokens):
        position = None
        coords = None
        side = None

        i = 0
        while i < len(tokens):   #parse tokens
            token = tokens[i]

            if token in {'TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'}:   #detect position and coordinates
                position = token
                try:
                    coords = (float(tokens[i+1]), float(tokens[i+2]))
                except (IndexError, ValueError):
                    raise ValueError("Invalid coordinates")
                i += 3
            elif token == 'Side':   #detect side length
                try:
                    side = float(tokens[i+1])
                except (IndexError, ValueError):
                    raise ValueError("Invalid side length")
                i += 2
            else:
                i += 1

        if position is None or coords is None or side is None:   #check that all required data found
            raise ValueError("Invalid data: missing position, coordinates, or side")

        if side <= 0:   #check that side length is positive
            raise ValueError("Side length must be positive")

        return cls(position=position, coords=coords, side=side)






