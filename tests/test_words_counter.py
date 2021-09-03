from words_counter import words_counter


def test_good():
    excepted_result = 'a 1\naa 2\naaa 2\nbb 3\nc 4\njj 1'
    actual_result = words_counter('jj aa aa. aaa bb c bb a bb. c c-c aaa ')
    assert actual_result == excepted_result
