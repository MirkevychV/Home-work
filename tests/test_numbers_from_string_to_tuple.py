import pytest

from numbers_from_string_to_tuple import numbers_from_string_to_tuple


@pytest.mark.parametrize('numbers_string,excepted_result', [
    ('1, 34, 54, 92', (1, 34, 54, 92)),
    ('2,  43, 14, 66', (2, 43, 14, 66))
])
def test_good(numbers_string, excepted_result):
    actual_result = numbers_from_string_to_tuple(numbers_string)
    assert actual_result == excepted_result
