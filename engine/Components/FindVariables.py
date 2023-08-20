from Components.Constants import VALID_BRACKETS, VALID_CONNECTIVES
from Components.Sanitizer import clean_whitespaces, clean_commas


def find_variables(statement):
	"""
	Runs through the statement to determine all the variables given in the user
	statement.

	:param statement: given user statement
	:returns: Returns an array and string of variables, respectively
	"""

	statement = clean_whitespaces(statement)
	statement = clean_commas(statement)

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

	return variables_array, variables_string
