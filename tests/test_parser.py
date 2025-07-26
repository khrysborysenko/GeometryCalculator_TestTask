import pytest
from parser import define_shape
from utils import format_number

def test_parser_valid_input():
    inputs = [
        "Square TopLeft 5 5 Side 3",
        "Rectangle TopRight 11 6 BottomLeft 1 1",
        "Circle Center 7 7 Radius 5",
        "Triangle Point1 1 0 Point2 6 0 Point3 4 3",
    ]
    expected_outputs = [
        "Square Perimeter 12 Area 9",
        "Rectangle Perimeter 30 Area 50",
        "Circle Perimeter 31.42 Area 78.54",
        "Triangle Perimeter 12.85 Area 7.50"
    ]
    for i, line in enumerate(inputs):
        shape = define_shape(line)
        result = f"{shape.__class__.__name__} Perimeter {format_number(shape.perimeter)} Area {format_number(shape.area)}"
        assert result == expected_outputs[i]

def test_parser_invalid_input():
    inputs = [
        "",
        "Parallelogram TopRight 6 5",
        "Square TopLeft 1 1",
        "Rectangle TopRight 3 4",
        "Circle Center 1 1",
        "Triangle Point1 1 0 Point2 6 0"
    ]
    for line in inputs:
        with pytest.raises(ValueError):
            define_shape(line)
