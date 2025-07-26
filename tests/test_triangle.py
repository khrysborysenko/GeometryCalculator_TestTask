import pytest
from shapes.triangle import Triangle

def test_triangle_perimeter_and_area():   #test correct calculation for a valid triangle
    tokens = ['Triangle', 'Point1', '0', '0', 'Point2', '3', '0', 'Point3', '0', '4']
    tr = Triangle.from_tokens(tokens)
    assert tr.point1 == (0, 0)
    assert tr.point2 == (3, 0)
    assert tr.point3 == (0, 4)
    assert tr.perimeter == 12
    assert tr.area == 6

def test_triangle_missing_point():   #test error when entering without third point
    tokens = ['Triangle', 'Point1', '0', '0', 'Point2', '3', '0']
    with pytest.raises(ValueError, match="Triangle must have exactly three points"):
        Triangle.from_tokens(tokens)

def test_triangle_invalid_coords():   #test error when entering invalid coordinates
    tokens1 = ['Triangle', 'Point1', '0', 'abc', 'Point2', '3', '0', 'Point3', '0', '4']
    tokens2 = ['Triangle', 'Point1', '0', 'Point2', '3', '0', 'Point3', '0', '4']
    with pytest.raises(ValueError, match="Invalid coordinates"):
        Triangle.from_tokens(tokens1)
    with pytest.raises(ValueError, match="Invalid coordinates"):
        Triangle.from_tokens(tokens2)

def test_triangle_collinear_points():   #test error when points are collinear (lie on the same line so it's impossible to form a triangle)
    tokens = ['Triangle', 'Point1', '0', '0', 'Point2', '1', '1', 'Point3', '2', '2']
    with pytest.raises(ValueError, match="Points cannot be collinear"):
        Triangle.from_tokens(tokens)

def test_triangle_duplicate_points():   #test error for duplicates
    tokens = ['Triangle', 'Point1', '0', '0', 'Point2', '1', '1', 'Point3', '0', '0']
    with pytest.raises(ValueError, match="Points must be distinct"):
        Triangle.from_tokens(tokens)

def test_triangle_additional_validation_check():   #test error of additional layer of validation in constructor
    with pytest.raises(ValueError, match="Points must have two numeric coordinates"):
        Triangle((0,), (1, 1), (5, 1))
    with pytest.raises(ValueError, match="Points must have two numeric coordinates"):
        Triangle((0,'abc'), (1, 1), (5, 1))
    with pytest.raises(ValueError, match="Points must have two numeric coordinates"):
        Triangle((0, 0, 0), (1, 1), (5, 1))