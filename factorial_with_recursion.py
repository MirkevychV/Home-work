import sys


sys.setrecursionlimit(1007)  # default 1000, so we cant find 1005!


def factorial_with_recursion(n):
	"""
	3. написати функцію, яка буде знаходити факторіал числа.
	"""
	if n == 1:
		return 1  # 1! = 1
	else:
		return n * factorial_with_recursion(n-1)
