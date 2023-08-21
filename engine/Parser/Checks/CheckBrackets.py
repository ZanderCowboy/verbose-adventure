from Components.Constants import LEFT_BRACKETS, RIGHT_BRACKETS
from Logging.logging_config import logger


class UnequalBracketsExcept(Exception):
	pass


def check_left_and_right_brackets(statement):
	"""
	This function checks if the number of opening and closing brackets are equal.
	:param statement: the given string statement
	:return: Returns a True if the left and right brackets are equal
	"""
	logger.info("In check_left_and_right_brackets()...")
	count = 0
	for i in range(len(statement)):
		if statement[i] in LEFT_BRACKETS:
			count += 1
		elif statement[i] in RIGHT_BRACKETS:
			count -= 1

	if count == 0:
		logger.info("Returning with True...")
		return True

	logger.error("Error in check_left_and_right_brackets()!")
	raise UnequalBracketsExcept("Input statement must have an equal number of opening and closing brackets")

# todo Add to Unit Test
# check_brackets tests
# test_check_brackets = ['(',')']
# test_check_brackets = ['(','(',')',')']
# test_check_brackets = ['(', '(',')',    '(',')',    ')']
# test_check_brackets = ['(',  '(',')',  '(','(',')','(',')',')', ')']
# test_check_brackets = ['(', '(',')', '(',   '(',')',    ')']  # False
