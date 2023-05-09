from datetime import date
from seasons import convert_number_to_words, find_minutes

def test_convert_number_to_words():

    assert convert_number_to_words(1440) == "one thousand, four hundred forty"
    assert convert_number_to_words(525600) == "five hundred twenty-five thousand, six hundred"
    assert convert_number_to_words(15778080) == "fifteen million, seven hundred seventy-eight thousand eighty"
