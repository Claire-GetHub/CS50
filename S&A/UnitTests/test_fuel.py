from fuel import convert, gauge
import pytest

def test_test():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(5) == "5%"
    assert convert("1/2") == 50

# print(gauge(99))
# print(gauge(1))
# print(gauge(5))
# print(convert("1/2"))





