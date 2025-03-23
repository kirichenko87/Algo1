import pytest
from count_ones import count_ones


@pytest.mark.parametrize('value, expected_result', [
    (0, 0),
    (5, 2),
    (15, 4)
])

def test_count_ones_positive(value, expected_result):
    assert count_ones(value) == expected_result

@pytest.mark.parametrize('value, expected_result', [
    (-1, ValueError),
    ("123", TypeError)
])


def test_count_ones_negative(value, expected_result):
    with pytest.raises(expected_result):
        count_ones(value)

@pytest.mark.parametrize('value, expected_result', [
    (0, 0),
    (1234123, 11)
])

def test_count_ones_limit(value, expected_result):
    assert count_ones(value) == expected_result