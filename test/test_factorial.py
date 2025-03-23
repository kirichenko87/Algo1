import pytest
from factorial import factorial

@pytest.mark.parametrize('value, expected_result', [
    (2, 2),
    (5, 120),
    (10, 3628800),
    (15, 1307674368000),
    (19, 121645100408832000)
])

def test_factorial_positive(value, expected_result):
    assert factorial(value) == expected_result


@pytest.mark.parametrize('value, expected_result',[
    ([1,2,3,4,5,6], TypeError),
    ('123345', TypeError),
    (-123, ValueError),
    (-1, ValueError),
    (21, ValueError)
])

def test_factorial_negative(value, expected_result):
    with pytest.raises(expected_result):
        factorial(value)

@pytest.mark.parametrize('value, expected_result',[
    (0, 1),
    (20, 2432902008176640000)
])

def test_factorial_limit(value, expected_result):
    assert factorial(value) == expected_result