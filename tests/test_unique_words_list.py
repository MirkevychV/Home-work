from unique_words_list import unique_words_list


def test_good():
    actual_result = unique_words_list('jack jack  python   vadim vadim vadim')
    assert any(True for el in ['jack', 'python', 'vadim'] if el in actual_result)
