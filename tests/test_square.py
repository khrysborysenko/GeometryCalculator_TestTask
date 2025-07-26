import pytest
from shapes.square import  Square

def test_square_perimeter_and_area():   #test correct calculation for a valid square
    square = Square(position='TopLeft', coords=(0, 0), side=5)
    assert square.perimeter == 20
    assert square.area == 25

def test_square_from_tokens_method():   #test of parsing tokens and constructing square
    tokens = ['Square', 'TopLeft', '0', '0', 'Side', '6']
    square = Square.from_tokens(tokens)
    assert square.position == 'TopLeft'
    assert square.coords == (0, 0)
    assert square.side == 6
    assert square.perimeter == 24
    assert square.area == 36

def test_square_missing_data():   #test error when entering incomplete data
    tokens = ['Square', 'TopLeft', '0', '0']
    with pytest.raises(ValueError, match="Invalid data: missing position, coordinates, or side"):
        Square.from_tokens(tokens)

def test_square_invalid_side():   #test errors when entering invalid side
    tokens_zero = ['Square', 'TopLeft', '0', '0', 'Side', '0']
    tokens_negative = ['Square', 'TopLeft', '0', '0', 'Side', '-5']
    tokens_not_number = ['Square', 'TopLeft', '0', '0', 'Side', 'abc']
    with pytest.raises(ValueError, match="Side length must be positive"):
        Square.from_tokens(tokens_zero)

    with pytest.raises(ValueError, match="Side length must be positive"):
        Square.from_tokens(tokens_negative)

    with pytest.raises(ValueError, match="Invalid side length"):
        Square.from_tokens(tokens_not_number)

def test_square_invalid_coords():   #test error when entering invalid coordinates
    tokens = ['Square', 'TopLeft', 'abc', 'def', 'Side', '6']
    with pytest.raises(ValueError, match="Invalid coordinates"):
        Square.from_tokens(tokens)