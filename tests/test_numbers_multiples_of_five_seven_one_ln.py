import pytest

from numbers_multiples_of_seven_one_line import numbers_multiples_of_seven_one_line


@pytest.mark.parametrize('start,stop,excepted_result', [
    (1, 30, '7,14,21,28'),
    (100, 140, '112,119,126,133')
])
def test_good(start, stop, excepted_result):
    actual_result = numbers_multiples_of_seven_one_line(start, stop)
    assert actual_result == excepted_result
