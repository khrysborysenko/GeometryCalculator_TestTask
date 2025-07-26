from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.circle import Circle
from shapes.triangle import Triangle

shape_map = {
    "square": Square,
    "rectangle": Rectangle,
    "circle": Circle,
    "triangle": Triangle,
}

def define_shape(line):
    tokens = line.strip().split()

    if not tokens:
        raise ValueError("Empty input")

    shape_type = tokens[0].lower()

    shape_class = shape_map.get(shape_type)

    if shape_class is None:
        raise ValueError(f"Unknown shape type '{shape_type}'")

    try:
        return shape_class.from_tokens(tokens)
    except Exception as e:
        raise ValueError(f"In shape '{shape_type}': {e}")