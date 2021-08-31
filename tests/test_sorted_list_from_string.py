from sorted_list_from_string import sorted_list_from_string


def test_good():
    actual_result = sorted_list_from_string('vadim,jack,alpha,beta,vasya,yei')
    assert actual_result == ['alpha', 'beta', 'jack', 'vadim', 'vasya', 'yei']
