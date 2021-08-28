import re


def numbers_from_string_to_tuple(numbers_string):
	"""
	7. написати функцію, яка отримує аргумент типу string з числами
	через кому (можливі пробіли(space)), а на виході видає tuple цих
	чисел
	"""
	numbers_list = []

	match_template = re.findall(r'\d+', numbers_string)
	for number in match_template:
		numbers_list.append(int(number))
	return tuple(numbers_list)
