import re
from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("AB1234") == True
    assert is_valid("B1234") == False
    assert is_valid("A1B234") == False
    assert is_valid("1AB234") == False

def test_max_six_characters():
    assert is_valid("ABCDEF") == True
    assert is_valid("AB1234") == True
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCD1234") == False

def test_numbers_at_end_only():
    assert is_valid("AAA222") == True
    assert is_valid("AB123") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AB0123") == False

def test_no_punctuation():
    assert is_valid("ABCD12") == True
    assert is_valid("ABCD.") == False
    assert is_valid("ABCD 12") == False
    assert is_valid("ABCD_12") == False