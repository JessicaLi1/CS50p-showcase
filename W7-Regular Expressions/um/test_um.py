from um import count

def test_count():
    assert count("hello, um, world") == 1
    assert count("um, so, um well") == 2
    assert count("like a small cat but not mine") == 0
    assert count("um") == 1
    assert count("UM well awsome") == 1
    assert count("") == 0
    assert count("hum") == 0