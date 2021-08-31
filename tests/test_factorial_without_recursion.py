import pytest

from factorial_without_recursion import factorial_without_recursion


@pytest.mark.parametrize('n,excepted_result', [
    (4, 24),
    (5, 120),
    (7, 5040)
])
def test_good(n, excepted_result):
    actual_result = factorial_without_recursion(n)
    assert actual_result == excepted_result
