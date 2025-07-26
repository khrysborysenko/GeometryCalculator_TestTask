import pytest
from shapes.rectangle import Rectangle

def test_rectangle_perimeter_and_area():   #test correct calculation for a valid rectangle
    rect = Rectangle.from_tokens(['Rectangle', 'TopLeft', '-4', '-1', 'BottomRight', '-1', '-3'])
    assert rect.width == 3
    assert rect.height == 2
    assert rect.perimeter == 10
    assert rect.area == 6

def test_rectangle_missing_corner():   #test error when entering data without second corner
    with pytest.raises(ValueError, match="Rectangle requires exactly 2 corners"):
        Rectangle.from_tokens(['Rectangle', 'TopLeft', '0', '0'])

def test_rectangle_too_many_corners():   #test error when entering three corners
    with pytest.raises(ValueError, match="Too many corners provided for Rectangle"):
        Rectangle.from_tokens(['Rectangle', 'TopLeft', '0', '2', 'TopRight', '3', '2', 'BottomLeft', '0', '0'])

def test_rectangle_invalid_coords():   #test error when entering invalid coordinates
    tokens1 = ['Rectangle', 'TopLeft', '0', 'BottomRight', '1', '1']
    tokens2 = ['Rectangle', 'TopLeft', 'abc', '0', 'BottomRight', '0', '4']
    with pytest.raises(ValueError, match="Invalid coordinates"):
        Rectangle.from_tokens(tokens1)
    with pytest.raises(ValueError, match="Invalid coordinates"):
        Rectangle.from_tokens(tokens2)

def test_rectangle_adjacent_corners():   #test error when entering adjacent corners (impossible to form rectangle)
    with pytest.raises(ValueError, match="Corners must be opposite, only axis-aligned rectangles are supported"):
        Rectangle.from_tokens(['Rectangle', 'TopLeft', '0', '0', 'TopRight', '0', '2'])

    with pytest.raises(ValueError, match="Corners must be opposite, only axis-aligned rectangles are supported"):
        Rectangle.from_tokens(['Rectangle', 'TopLeft', '0', '0', 'TopRight', '2', '0'])

