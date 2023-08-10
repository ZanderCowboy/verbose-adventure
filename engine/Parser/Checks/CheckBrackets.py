from Components.Constants import LEFT_BRACKETS, RIGHT_BRACKETS


class UnequalBracketsExcept(Exception):
	pass


def check_left_and_right_brackets(statement):
	"""
	This function checks if the number of opening and closing brackets are equal.
	:param statement: the given string statement
	:return: Returns a True if the left and right brackets are equal
	"""
	count = 0
	for i in range(len(statement)):
		if statement[i] in LEFT_BRACKETS:
			count += 1
		elif statement[i] in RIGHT_BRACKETS:
			count -= 1

	if count == 0:
		return True
	raise UnequalBracketsExcept("Input statement must have an equal number of opening and closing brackets")
