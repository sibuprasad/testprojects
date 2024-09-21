import pytest

@pytest.mark.great
def test_graeter():
    num = 100
    assert num > 100

@pytest.mark.great
def test_graeter_equal():
    num = 100
    assert num >= 100

@pytest.mark.other
def test_less():
    num = 100
    assert num < 200