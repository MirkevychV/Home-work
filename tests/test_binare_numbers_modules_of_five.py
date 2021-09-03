import pytest

from binare_numbers_modules_of_five import binare_numbers_modules_of_five


@pytest.mark.parametrize('nums_string,excepted_result', [
    ('00101,01101,11101', ['00101']),
    ('1111,01010,011101', ['1111', '01010'])
])
def test_good(nums_string, excepted_result):
    actual_result = binare_numbers_modules_of_five(nums_string)
    assert actual_result == excepted_result
