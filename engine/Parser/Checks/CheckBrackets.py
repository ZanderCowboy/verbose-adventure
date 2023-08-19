from Components.Constants import LEFT_BRACKETS, RIGHT_BRACKETS
import re


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

	# pattern = "^(?:(?:[^[\]]*\[[^[\]]*])*(?:[^[\]]*])*?)$"
	# pattern = "^(?:(?:[^()]*\([^()]*\))*(?:[^()]*))*$"
	# pattern = "^(?:(?:[^()]*\([^()]*\))*(?:[^()]*))*$"
	# brackets = get_brackets_from_statement_or_array(statement)
	# return_obj = re.fullmatch(pattern, brackets) is not None
	# return return_obj

	if count == 0:
		return True
	raise UnequalBracketsExcept("Input statement must have an equal number of opening and closing brackets")

# todo Add to Unit Test
# check_brackets tests
# test_check_brackets = ['(',')']
# test_check_brackets = ['(','(',')',')']
# test_check_brackets = ['(', '(',')',    '(',')',    ')']
# test_check_brackets = ['(',  '(',')',  '(','(',')','(',')',')', ')']
# test_check_brackets = ['(', '(',')', '(',   '(',')',    ')']  # False


# def get_brackets_from_statement_or_array(statement):
# 	string_of_brackets = ""
#
# 	for i, char in enumerate(statement):
# 		if char in LEFT_BRACKETS or char in RIGHT_BRACKETS:
# 			string_of_brackets += char
#
# 	return string_of_brackets
