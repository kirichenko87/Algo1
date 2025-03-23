from pickle import FALSE

import pytest
from is_palindrome import is_palindrome

@pytest.mark.parametrize('value, expected_result',[
    (121, True),
    (-121, False),
    (10, False),
    (0, True)
])

def test_is_polindrome_positive(value, expected_result):
    assert is_palindrome(value) == expected_result

@pytest.mark.parametrize('value, expected_result', [
    ('121', TypeError),
    ('0', TypeError)

])

def test_is_polindrome_negative(value, expected_result):
    with pytest.raises(expected_result):
        is_palindrome(value)

@pytest.mark.parametrize('value, expected_result', [
    (0, True),
    (1222222222222221, True),
    (124124234151343, False)
])

def test_ispolindrome_limit(value, expected_result):
    assert is_palindrome(value) == expected_result