from Components.Constants import VALID_BRACKETS, VALID_CONNECTIVES
# from Components.Sanitizer import clean_whitespaces, clean_commas
from Components.Sanitizer import clean_whitespaces
from Logging.logging_config import logger


def find_variables(statement: str) -> list:
	"""
	Runs through the statement to determine all the variables given in the
	statement.

	:rtype: list
	:param statement: given user statement
	:return: Returns an array variables
	"""
	logger.info("Finding variables in statement...")

	# logger.info("All whitespaces and commas need to be removed, proceeding.")
	logger.info("All whitespaces need to be removed, proceeding.")
	statement = clean_whitespaces(statement)
	# statement = clean_commas(statement)
	# logger.warning("Removed any whitespaces or commas found in statement. "
	# 			   "Proceeding with finding variables.")
	logger.warning("Removed any whitespaces found in statement. "
				   "Proceeding with finding variables.")

	logger.debug("statement=%s", statement)
	variables_array = []
	variables_string = ""
	non_variable_characters = VALID_BRACKETS + VALID_CONNECTIVES
	for i in range(len(statement)):
		duplicate = False
		char = statement[i]

		if char not in non_variable_characters:  # if char is not a bracket or a connective
			# Testing for duplicates
			duplicate_int = statement.find(char, i + 1)
			var_str_find = variables_string.find(char)
			if len(variables_array) > 0 and duplicate_int > 0 and var_str_find >= 0:
				duplicate = True
			if duplicate_int == -1:  # no initial or more occurrences
				if var_str_find >= 0:
					continue
			if len(variables_array) == 0 or duplicate is False:
				variables_array.append(char)
				variables_string += char
			elif duplicate:
				continue

	logger.debug("variables_array=%s", variables_array)
	logger.info("Found all variables in statement. ")
	return variables_array
