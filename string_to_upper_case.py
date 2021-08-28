def string_to_upper_case(list_str):
	"""
	9. написати функцію, яка приймає список текстових рядків
	(list[str]) і виводить кожен рядок, роблячи кожну першу букву слова
	великою
	"""
	for word in list_str:
		print(word.title())
