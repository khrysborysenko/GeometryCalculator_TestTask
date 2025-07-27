import pytest
import math
from shapes.polygon import Polygon

def test_polygon_perimeter():
    p = Polygon([(0, 0), (0, 1)])
    assert p.perimeter == 2

def test_polygon_perimeter2():
    p = Polygon([(0, 0), (0, 2)])
    assert p.perimeter == 4

def test_polygon_triangle():
    p = Polygon([(0, 0), (0, 1), (1, 2)])
    assert math.isclose(p.perimeter, 4.65, rel_tol=1e-3)