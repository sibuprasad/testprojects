from Projects.testprojects import shape
import pytest

class TestRectangle:

    def setup_method(self, data):
        print(f"setting up {data}")
        self.recarea = shape.rectangle(5,10)

    def teardown_method(self, data):
        print(f"setting up {data}")
        # del self.recarea

    def test_rec_area(self):
        result = self.recarea.area()
        expected = self.recarea.l * self.recarea.b
        assert result == expected

    def test_rec_peri(self):
        result = self.recarea.perimeter()
        expected = 2*(self.recarea.l + self.recarea.b)
        assert result == expected