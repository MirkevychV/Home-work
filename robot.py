from math import sqrt


def robot(commands_list):
	"""
	15. На вході функція отримує список strings із переміщеннями робота
	вигляду "1 UP", "2 LEFT", "3 DOWN", і т.д. робот може рухатись
	тільки в 4 сторони(UP,DOWN,LEFT,RIGHT). функція повинна повертати
	відстань між початковою і кінцевою точками робота.
	"""
	x = 0
	y = 0

	for command in commands_list:
		value, direction = command.split()
		if direction == "UP":
			y += int(value)
		elif direction == "DOWN":
			y -= int(value)
		elif direction == "RIGHT":
			x += int(value)
		elif direction == "LEFT":
			x -= int(value)
		else:
			print("Unknow direction '" + direction +"'")

	return sqrt(x**2 + y**2)
