import pytest

from robot import robot


@pytest.mark.parametrize('commands_list,excepted_result', [
    (['4 UP', '3 LEFT'], 5),
    (['1 UP', '2 RIGHT', '1 DOWN'], 2)
])
def test_good(commands_list, excepted_result):
    actual_result = robot(commands_list)
    assert actual_result == excepted_result


@pytest.mark.parametrize('commands_list', [
    (['4 UP', '3 AGAIN']),
    (['1 BACK', '2 RIGHT', '1 DOWN'])
])
def test_exception(commands_list):
    actual_result = robot(commands_list)
    assert actual_result is None
