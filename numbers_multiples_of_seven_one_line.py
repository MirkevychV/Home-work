# 2. написати те ж що в №1, але в 1 рядок( без використання eval )
def numbers_multiples_of_seven_one_line(start, stop): return ','.join(
    [str(num) for num in range(start, stop) if num % 7 == 0 and num % 5 != 0])
