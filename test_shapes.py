from Projects.testprojects import shape
import pytest

""" Without using @pytest.fixture """
def test_rec_area():
    rectangle = shape.rectangle(2,4)        # without fixture i write the same data twice
    assert rectangle.area() == 8

def test_rec_peri():
    rect = shape.rectangle(2,4)             # without fixture i write the same data twice
    assert rect.perimeter() == 2*(rect.l + rect.b)


""" With using @pytest.fixture """
@pytest.fixture()
def mycircle():
    return shape.circle(7)                      # with fixture it became dynamic & i use it every where

def test_cir_area(mycircle):
    assert mycircle.area() == ((22/7) * (mycircle.r**2))
    print(mycircle.area())

def test_cir_peri(mycircle):
    assert mycircle.perimeter() == 2 * (22/7) * mycircle.r
    print(mycircle.perimeter())