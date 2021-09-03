import pytest

from solve_a import solve_a


@pytest.mark.parametrize('a,excepted_result', [
    (1, 1234),
    (2, 2468),
    (3, 3702)
])
def test_good(a, excepted_result):
    actual_result = solve_a(a)
    assert actual_result == excepted_result
