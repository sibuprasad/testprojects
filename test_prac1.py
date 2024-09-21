import pytest

@pytest.mark.xfail(reason = "This test is expected to fail due to division by zero")
def test_myprac():
    result = 1 / 0
    assert result == 0


@pytest.mark.xfail(reason = "Known issue with addition")
def test_myprac2():
    result = 2 + 2
    assert result == 5


@pytest.mark.xskip(reason="Test requires external service")
def test_integration_with_service():
    # Test code that requires an external service which is not available
    assert True


@pytest.mark.xskip
def test_slow_functionality():
    if not pytest.config.getoption('--runslow'):
        pytest.skip("Need --runslow option to run")
    assert True