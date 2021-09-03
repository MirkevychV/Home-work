def numbers_multiples_of_seven(start=1000, stop=3100):
	"""
	1. написати програму, яка буде знаходити всі числа кратні 7 але не
	кратні 5, не менше 1000 і не більше 3100. Результат вивести через
	кому в один рядок.
	"""
	result_list = []

	for num in range(start, stop):
		if (num % 7 == 0) and (num % 5 != 0):
			result_list.append(str(num))

	result = ','.join(result_list)
	return result
