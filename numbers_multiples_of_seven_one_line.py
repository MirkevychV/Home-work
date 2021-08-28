# 2. написати те ж що в №1, але в 1 рядок( без використання eval )
def numbers_multiples_of_seven_one_line(): return ','.join([str(num) for num in range(1000, 3100) if num % 7 == 0 and num % 5 != 0])

print(numbers_multiples_of_seven_one_line())
