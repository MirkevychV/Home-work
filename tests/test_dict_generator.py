import pytest

from dict_generator import dict_generator


@pytest.mark.parametrize('n,excepted_result', [
    (2, {1: 1, 2: 4}),
    (3, {1: 1, 2: 4, 3: 9})
])
def test_good(n, excepted_result):
    actual_result = dict_generator(n)
    assert actual_result == excepted_result
    