import pytest
from text_analysis import get_alphabet, get_char_frequencies, get_bigrams, get_trigrams, filter_text

def test_get_alphabet():
    assert get_alphabet("hello") == ['e', 'h', 'l', 'o']
    assert get_alphabet("1234") == ['1', '2', '3', '4']
    assert get_alphabet("aabbcc") == ['a', 'b', 'c']

def test_get_char_frequencies():
    assert get_char_frequencies("aabb") == {'a': 2, 'b': 2}
    assert get_char_frequencies("") == {}
    assert get_char_frequencies("abc") == {'a': 1, 'b': 1, 'c': 1}

def test_get_bigrams():
    assert get_bigrams("hello") == {'he': 1, 'el': 1, 'll': 1, 'lo': 1}
    assert get_bigrams("aaa") == {'aa': 2}
    assert get_bigrams("") == {}

def test_get_trigrams():
    assert get_trigrams("hello") == {'hel': 1, 'ell': 1, 'llo': 1}
    assert get_trigrams("aaaa") == {'aaa': 2}
    assert get_trigrams("") == {}

def test_filter_text():
    assert filter_text("hello world!") == "hello_world!"
    assert filter_text("Привіт!") == "!"
    assert filter_text("123 ABC") == "123_ABC"
