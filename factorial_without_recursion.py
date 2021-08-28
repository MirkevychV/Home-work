def factorial_without_recursion(n):
	"""
	4. те ж саме, але без рекурсії ( з рекурсією, якщо зробили без
	рекурсії )
	"""
	factorial = 1

	if n == 1:
		return 1  # 1! = 1
	else:
		for i in range(1, n+1):
			factorial = factorial * i
		return factorial
