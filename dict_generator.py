def dict_generator(n):
	"""
	5. написати функцію, яка при заданому n буде генерувати dict
	вигляду {i: i^2, ...}, де і від 1 до n.
	"""
	result = {}

	for i in range(1, n+1):
		result[i] = i ** 2

	return result
