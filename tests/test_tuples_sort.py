from tuples_sort import tuples_sort


def test_good():
    actual_result = tuples_sort([
        ('Vadim', 17, 99),
        ('Jack', 25, 75),
        ('Vadim', 17, 100),
        ('Vadim', 18, 99)
    ])

    excepted_result = [
        ('Jack', 25, 75),
        ('Vadim', 17, 100),
        ('Vadim', 17, 99),
        ('Vadim', 18, 99)
    ]

    assert actual_result == excepted_result
