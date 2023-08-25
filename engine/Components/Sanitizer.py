# todo Changes statement to something that we can use
# todo Change to something that the system can use
# todo Add brackets
# todo Change connectives to one common set
# todo Change lower case letters to upper case

from Components.Constants import *
from Logging.logging_config import logger


# for example: change & to ^, | to v


# todo Refactor to sanitize statement
def add_brackets(statement):
	"""
	Adds outer brackets to any statement
	:param statement:
	:return:
	"""
	pass
	new_string = ""

	return new_string


# def clean_commas(statement: str) -> str:
# 	"""
# 	Removes commas if more than one statement is given.
#
# 	:param statement: given statement
# 	:return: returns a statement with commas removed
# 	"""
# 	logger.debug("Calling clean_commas(%s)...", statement)
#
# 	logger.debug("Returning without commas: statement=%s", statement.replace(",", ""))
# 	return statement.replace(",", "")


def clean_whitespaces(statement: str) -> str:
	"""
	This clears a statement of all whitespaces that are present.
	:param statement: given statement
	:return: returns a statement with whitespaces removed
	"""
	logger.debug("Calling clean_whitespaces(%s)...", statement)

	logger.debug("Returning without whitespaces: statement=%s", statement.replace(" ", ""))
	return statement.replace(" ", "")


def remove_brackets_around_variables(arr: list, variables: list) -> list:
	"""
	This removes brackets around single variables in an array, e.g., (P) => P
	:param arr:
	:param variables: Array of variables from statement.
	:return: Returns an array without brackets around variables.
	"""
	logger.info("Removing brackets around standalone variables...")

	for i in range(0, len(arr) - 2):
		if arr[i] in variables:
			left_of_variable = arr[i - 1]
			right_of_variable = arr[i + 1]
			if left_of_variable in LEFT_BRACKETS and right_of_variable in RIGHT_BRACKETS:
				arr.pop(i - 1)
				arr.pop(i)
	# todo Add another loop to make sure that no 'single brackets' are found

	logger.debug("arr=%s", arr)
	logger.info("Removed all brackets around variables.")
	return arr


def add_brackets_around_unary_connectives(arr: list, variables: list) -> list:
	"""
	This adds brackets around unary connectives.
	:param arr:
	:param variables: Array of variables from statement.
	:return: Returns an array with brackets around unary connectives.
	"""
	logger.info("Adding brackets around unary connectives...")

	for i in range(len(arr)):
		if arr[i] in UNARY_CONNECTIVES:  # we have a unary connective
			if arr[i+1] in variables:  # unary connective is next to a variable
				if arr[i-1] in LEFT_BRACKETS and arr[i+2] in RIGHT_BRACKETS:  # there is brackets around it
					# good case
					continue
				elif arr[i-1] in BINARY_CONNECTIVES or arr[i+2] in BINARY_CONNECTIVES:  # there is no brackets around it
					arr.insert(i, '(')
					arr.insert(i+3, ')')
	# todo Add a final check to makes sure that no unary connectives was missed.

	logger.debug("arr=%s", arr)
	logger.info("Finished adding brackets around all unary connectives.")
	return arr
