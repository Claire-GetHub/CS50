from bank import value

def test_test():
    assert value("hello") == 0
    assert value("howdy") == 20
    assert value("whats up") == 100
    assert value("HELLO") == 0
