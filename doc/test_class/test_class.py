import pytest

class calculadora:
    def soma(self, x):
        return sum(x)

    def divide(self, x: float, y: float) -> float:
        try:
            return (x / y)
        except:
            raise SystemExit(1)


class TestClass:
    def test_soma(self):
        x = [1, 2, 3, 4]
        res = calculadora().soma(x)
        assert res == 10

    def test_divide(self):
        x, y = 10, 1
        res = calculadora().divide(x, y)
        assert res == 10


class TestClassException:
    def test_mytest(self):
        with pytest.raises(SystemExit):
            calculadora().divide(10, 0)