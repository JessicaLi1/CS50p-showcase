from bank import value

def test_value_hello():
    assert value("hello world") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hELLO") == 0
    assert value(" hello ") == 0

def test_value_h():
    assert value("hi there") == 20
    assert value("help me") == 20
    assert value("Holland") == 20
    assert value("H") == 20
    assert value(" h ") == 20

def test_value_other():
    assert value("good morning") == 100
    assert value(" morning ") == 100
    assert value("536") == 100
    assert value(",./") == 100