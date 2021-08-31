import re


def unique_words_list(words_string):
	"""
	10. написати функцію, яка приймає string зі словами, розділеними
	пробілами (одним чи більше) і повертає список із унікальними
	словами
	"""
	result_set = set()

	match_template = re.findall(r'\w+', words_string)
	for word in match_template:
		result_set.add(word)

	return list(result_set)
