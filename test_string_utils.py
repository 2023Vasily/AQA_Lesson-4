import pytest
from string_utils import StringUtils

string =  StringUtils()

def test_firstLetter_positive():
    string = StringUtils()
    res = string.capitilize("dima")
    assert res == "Dima"

def test_whitespace_positive():
    string = StringUtils()
    res = string.trim("   Fire")
    assert res == "Fire"

def test_whitespace_negative():
    string = StringUtils()
    res = string.trim("")
    assert res == "Fire"

def test_list_positive():
    string = StringUtils()
    res = string.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]

def test_string_is_empty_negative():
    string = StringUtils()
    res = string.is_empty("")
    assert res == ["a", "b", "c", "d"]

def test_list_is_empty_negative():
    string = StringUtils()
    res = string.to_list("[]")
    assert res == []

def test_contains_positive():
    string = StringUtils()
    assert string.contains("Fire", "F") is True

def test_contains_negative_1():
    string = StringUtils()
    assert string.contains("Fire", "M") is False

def test_contains_negative_2():
    string = StringUtils()
    assert string.contains("", "") is False

@pytest.mark.parametrize(
        "input_string, input_symbol, result",
        [
            ("MyPain", "P", "Myain"),
            ("MyPain", "Pain", "My"),
            ("MyPain", "e", "MyPain"),
            ("", "", "MyPain"),
            ("", "a", ""),
            ("MyPain", "x", ""),
            ("123456", "5", "12346"),
            ("18 декабря 2024", "бря", "18 дека 2024"),
            ]
            )
def test_delete_symbol(input_string, input_symbol, result):
    string = StringUtils()
    res = string.delete_symbol(input_string, input_symbol)
    assert res == result

@pytest.mark.parametrize(
        "input_string, input_symbol, result",
        [
            ("SkyPro", "S", True),
            ("SkyPro", "M", False),
            ("SkyPro", "M", True),
            (" SkyPro", "S", True),
        ]
        )
def test_startswith(input_string, input_symbol, result):
    string = StringUtils()
    res = string.starts_with(input_string, input_symbol)
    assert res == result

@pytest.mark.parametrize(
        "input_string, input_symbol, result",
        [
            ("Song", "g", True),
            ("Song", "z", False),
            ("Song", "a", True),
            ("", "g", False),
        ]
        )
def test_endswith(input_string, input_symbol, result):
    string = StringUtils()
    res = string.end_with(input_string, input_symbol)
    assert res == result

def test_is_empty_positive_1():
    string = StringUtils()
    assert string.is_empty("") is True

def test_is_empty_positive_2():
    string = StringUtils()
    assert string.is_empty(" ") is True

def test_is_empty_positive_3():
    string = StringUtils()
    assert string.is_empty("Дима") is False

def test_list_to_string_1():
    string = StringUtils()
    assert string.list_to_string([1,2,3,4,5]) == "1, 2, 3, 4, 5"

def test_list_to_string_2():
    string = StringUtils()
    assert string.list_to_string(["Sky", "Pro"]) == "Sky, Pro"

def test_list_to_string_3():
    string = StringUtils()
    assert string.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

def test_list_to_string_4():
    string = StringUtils()
    assert string.list_to_string([]) == ""
    
    
