from shapes.square import Square

shape_map = {
    "square": Square,
}

def define_shape(line):
    tokens = line.strip().split()

    if not tokens:
        return None

    shape_type = tokens[0].lower()

    shape_class = shape_map.get(shape_type)

    if shape_class is None:
        print("Unknown shape type {shape_type}")
        return None

    try:
        return shape_class.from_tokens(tokens)
    except Exception as e:
        print(f"Error in shape definition: {e}")
        return None