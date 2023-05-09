from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("hfsd") == "hfsd"
    assert shorten("gsqgh") == "gsqgh"

def test_shorten_all_vowels():
    assert shorten("JAEIOUaeiou") == "J"
    assert shorten("jouiaeIOUEa") == "j"

def test_shorten_some_vowels():
    assert shorten("hello") == "hll"
    assert shorten("QUICK") == "QCK"

def test_shorten_with_numbers():
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("QU1CK") == "Q1CK"

def test_shorten_no_punctuation():
    assert shorten("Hello, world.") == "Hll, wrld."
    assert shorten("Let's code!") == "Lt's cd!"