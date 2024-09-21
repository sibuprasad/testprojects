from Projects.testprojects import shape
import pytest

class TestCircle:

    def setup_method(self, method):
        print(f"setting up {method}")
        self.circles = shape.circle(10)

    def teardown_method(self, method):
        print(f"setting up {method}")
        del self.circles

    def test_area(self):
        assert self.circles.area() == (22/7) * self.circles.r ** 2

    def test_perimeter(self):
        result = self.circles.perimeter()
        expected = 2 * (22/7) * self.circles.r
        assert result == expected