def tuples_sort(tuples_list):
	"""
	14. написати функцію, яка буде сортувати tuple із 3х значень. tuple
	вигляду (імя, вік, та рейтийнг). Пріорітет сортування - по імені,
	потім по віку, потім по рейтингу.
	"""
	sorted_list = sorted(tuples_list, key=lambda tup: (tup[0], tup[1], -tup[2]))
	return sorted_list
