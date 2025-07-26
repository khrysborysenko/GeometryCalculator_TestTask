import math
import pytest
from shapes.circle import Circle

def test_circle_perimeter_and_area():
    c = Circle(center='Center', coords=(1, 2), radius=3)
    assert c.center == 'Center'
    assert c.coords == (1, 2)
    assert c.radius == 3
    assert math.isclose(c.perimeter, 2 * math.pi * 3, rel_tol=1e-3)
    assert math.isclose(c.area, math.pi * 3**2, rel_tol=1e-3)

def test_circle_missing_data():
    tokens_missing_center = ['Circle', 'Radius', '3']
    tokens_missing_radius = ['Circle', 'Center', '1', '1']
    with pytest.raises(ValueError, match="Missing center coordinates or radius"):
        Circle.from_tokens(tokens_missing_center)
    with pytest.raises(ValueError, match="Missing center coordinates or radius"):
        Circle.from_tokens(tokens_missing_radius)

def test_circle_invalid_coords():
    tokens1 = ['Circle', 'Center', '1', 'Radius', '3']
    tokens2 = ['Circle', 'Center', '1', 'abc', 'Radius', '3']
    with pytest.raises(ValueError, match="Invalid coordinates of center"):
        Circle.from_tokens(tokens1)
    with pytest.raises(ValueError, match="Invalid coordinates of center"):
        Circle.from_tokens(tokens2)

def test_circle_invalid_radius():
    tokens_not_number = ['Circle', 'Center', '1', '1', 'Radius', 'abc']
    tokens_negative = ['Circle', 'Center', '1', '1', 'Radius', '-4']
    with pytest.raises(ValueError, match="Invalid radius of circle"):
        Circle.from_tokens(tokens_not_number)
    with pytest.raises(ValueError, match="Radius must be positive"):
        Circle.from_tokens(tokens_negative)

def test_circle_additional_validation_check():
    with pytest.raises(ValueError, match="Radius must be positive"):
        Circle(center='Center', coords=(1, 1), radius=0)
    with pytest.raises(ValueError, match="Center must have exactly two numeric coordinates"):
        Circle(center='Center', coords=(1, 1, 1), radius=3)
    with pytest.raises(ValueError, match="Center must have exactly two numeric coordinates"):
        Circle(center='Center', coords=(1, 'abc'), radius=3)
