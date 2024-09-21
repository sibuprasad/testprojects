import pytest

@pytest.mark.parametrize("num", [2,3,5,7])
def test_check(inp_value, num):
    assert num in inp_value


@pytest.mark.parametrize("i, j", [(2,10), (3,15), (4,20), (5,26)])
def test_data_find(i,j):
    assert i * 5 == j