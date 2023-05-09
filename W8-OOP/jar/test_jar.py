from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar = Jar(20)
    assert jar.capacity == 20

def test_str():
    jar = Jar()
    jar.deposit(6)
    assert str(jar)=="🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5
    try:
        jar.deposit(10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(1)
    assert jar.size == 2
    try:
        jar.withdraw(5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"