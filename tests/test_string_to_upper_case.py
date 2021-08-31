from string_to_upper_case import string_to_upper_case


def test_good():
    actual_result = string_to_upper_case(['vadim the best',
                                          'i want to the cinema',
                                          'i like it'])
    assert actual_result == 'Vadim The Best\n' \
                            'I Want To The Cinema\n' \
                            'I Like It\n'
