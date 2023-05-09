from numb3rs import validate

def test_wrong_ostet_number():
    assert validate("35.54.250") == False
    assert validate("5.154.32.234.125") == False


def test_max_255():
    assert validate("35.54.2.255") == True
    assert validate("0.35.54.50") == True
    assert validate("45.35.54.290") == False
    assert validate("45.35.542.20") == False
    assert validate("45.355.54.250") == False
    assert validate("452.35.54.250") == False


def test_non_int():
    assert validate("35.df.22.250") == False
    assert validate("35.54.1.2/0") == False
    assert validate("35.54.1.&*") == False

