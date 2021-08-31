import re


def validation(password):
	"""
	13. написати функцію, яка перевіряє пароль на відповідність
	правилам:
	"""
	rules = {
		"At least 1 letter between [a-z]": "-",
		"At least 1 number between [0-9]": "-",
		"At least 1 letter between [A-Z]": "-",
		"At least 1 character from [$#@]": "-",
		"Minimum length of transaction password: 6": "-",
		"Maximum length of transaction password: 12": "-"
	}

	if re.findall(r'[a-z]+', password):
		rules["At least 1 letter between [a-z]"] = "+"
	if re.findall(r'[0-9]+', password):	
		rules["At least 1 number between [0-9]"] = "+"
	if re.findall(r'[A-Z]+', password):	
		rules["At least 1 letter between [A-Z]"] = "+"
	if re.findall(r'[$#@]+', password):	
		rules["At least 1 character from [$#@]"] = "+"
	if len(password) >= 6:	
		rules["Minimum length of transaction password: 6"] = "+"
	if len(password) <= 12:	
		rules["Maximum length of transaction password: 12"] = "+"

	print("Password '" + password + "':")
	for rule, result in rules.items():
		print(rule + ": " + result)
