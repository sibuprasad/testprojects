import pytest
import time

def test_one():
    time.sleep(1)
    assert 1 == 1

def test_two():
    time.sleep(1)
    assert 2 == 2

def test_three():
    time.sleep(1)
    assert 3 == 3

def test_four():
    time.sleep(1)
    assert 4 == 4