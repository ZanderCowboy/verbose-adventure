from Components.Sanitizer import clean_whitespaces, clean_commas

valid_brackets = "(){}[]"
valid_connectives = "^v!<->"
# todo Add other connectives such as &&, ||, etc.
non_variable_characters = valid_brackets + valid_connectives


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
	len_statement = len(statement)
	for i in range(len(statement)):
		duplicate = False
		char = statement[i]

		if char not in non_variable_characters:
			# print("Finding Variables \t" + char)

			# Testing for duplicates
			duplicate_int = statement.find(char, i + 1)
			var_str_find = variables_string.find(char)
			if len(variables_array) > 0 and duplicate_int > 0 and var_str_find >= 0:
				duplicate = True
			# print(duplicate)
			if duplicate_int == -1:  # no more occurrences
				if var_str_find >= 0:
					continue
			if len(variables_array) == 0 or duplicate is False:
				variables_array.append(char)
				variables_string += char
			elif duplicate:
				continue

	return variables_array, variables_string
