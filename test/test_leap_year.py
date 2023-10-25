from src.year_leap.leap_year import isLeapYear

def test_leap_year_divided_by_4_but_not_by_100():
    assert isLeapYear(2016) == True
    assert isLeapYear(2020) == True

def test_leap_year_divided_by_400():
    assert isLeapYear(2000) == True
    assert isLeapYear(2400) == True

def test_non_leap_year_not_divided_by_4():
    assert isLeapYear(2021) == False
    assert isLeapYear(2100) == False

def test_non_leap_year_divided_by_100_but_not_by_400():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2100) == False
