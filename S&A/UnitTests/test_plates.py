from plates import is_valid

def test_test():
    assert is_valid("H3110") == False #beginning alphabetical
    assert is_valid("HELLOOOOOOOOO") == False #length
    assert is_valid("HE11O") == False #number placement
    assert is_valid("HELL0") == False #zero placement
    assert is_valid("HELLO!") == False #alphanumeric characters


