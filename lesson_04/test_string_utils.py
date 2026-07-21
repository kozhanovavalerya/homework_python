import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("Python", "Python"),
    ("SKYPRO", "Skypro"),
    ("hello-world", "Hello-world"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("12345", "12345"),
    ("!!!", "!!!"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("    Skypro", "Skypro"),
    ("Python   ", "Python   "),
    ("    ", ""),
    ("skypro", "skypro"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_negative():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", True),
    ("Skypro", "S", True),
    ("Python123", "1", True),
    ("SKYPRO", "M", False),
    ("hello@gmail.com", "@", True),
    ("SKYPRO", " ", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
def test_contains_negative():
    with pytest.raises(TypeError):
        string_utils.contains("Python123", 1)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", "kypro"),
    ("SSSkypro", "S", "kypro"),
    ("hello world", " ", "helloworld"),
    ("SKYPRO", "PRO", "SKY"),
    ("hello@gmail.com", "@", "hellogmail.com"),
    ("", "a", ""),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_negative():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "s")
