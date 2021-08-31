import pytest

from validation import validation


@pytest.mark.parametrize('password,excepted_result', [
    ('qwerty', False),
    ('123456qwerty', False),
    ('Gnj183##ac', True),
    ('kk23014KK$', True),
    ('short', False),
    ('looooooooooooooong', False)
])
def test_good(password, excepted_result):
    assert validation(password) == excepted_result
