def sorted_list_from_string(words_string):
	"""
	8. написати функцію, яка приймає string зі словами через кому, а
	повертає список із словами відсортованими в алфавітному порядку
	"""
	words_list = words_string.split(',')
	words_list.sort()
	return words_list
