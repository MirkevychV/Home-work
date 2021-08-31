def solve_a(a):
	"""
	12. написати функцію, яка обчислює a+aa+aaa+aaaa при заданому а.
	приклад, а=1 -- 1+11+111+1111
	"""
	result = 0
	template = "{0} {0}{0} {0}{0}{0} {0}{0}{0}{0}".format(a)
	numbers_list = template.split()

	for num in numbers_list:
		result += int(num)
	return result
