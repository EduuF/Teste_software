import pytest

def divide(x: float, y: float) -> float:
    try:
        return (x/y)
    except:
        raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        divide(10, 0)