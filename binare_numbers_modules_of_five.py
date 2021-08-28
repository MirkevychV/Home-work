def binare_numbers_modules_of_five(nums_string):
	"""
	11. написати програму, яка приймає string із бінарними числами,
	розділеними комою, і повертає тільки ті, які діляться на 5 
	"""
	nums_list = nums_string.split(',')
	result_list = []

	for num in nums_list:
		if int(num, 2) % 5 == 0:
			result_list.append(num) 
	
	return result_list
