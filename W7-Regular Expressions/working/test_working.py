from working import convert

def test_convert_afternoon_start():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("1 PM to 5 PM") == "13:00 to 17:00"

def test_convert_morning_start():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 1:00 AM") == "00:00 to 01:00"

def test_convert_value_error():
    try:
        convert("9:00AM to 5:00PM")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for missing space"

    try:
        convert("9:00 am to 5:00 pm")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for lowercase AM/PM"

    try:
        convert("9:00 XM to 5:00 PM")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid time"

    try:
        convert("9:00 AM to 25:00 PM")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid time"

    try:
        convert("9:00 AM 10:00 PM")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for missing to"
