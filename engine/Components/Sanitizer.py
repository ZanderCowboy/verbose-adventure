# todo changes statement to something that we can use
# todo change to something that the system can use
# todo add brackets
# todo Change connectives to one common set
# todo Change lower case letters to upper case

from Components.Constants import *

# for example: change & to ^, | to v


def add_brackets(statement):
	"""
	Adds outer brackets to any statement
	:param statement:
	:return:
	"""
	pass
	new_string = ""

	return new_string


def sanitize_statements(statement):
	"""
	dummy function
	:param statement:
	:return:
	"""
	final_string = ""

	new_string = add_brackets(statement)

	return final_string


def clean_commas(statement):
	"""
	Removes commas if more than one statement is given.

	:param statement: given statement
	:return: returns a statement with commas removed
	"""
	return statement.replace(",", "")


def clean_whitespaces(statement):
	"""

	:param statement: given statement
	:return: returns a statement with whitespaces removed
	"""
	return statement.replace(" ", "")


# takes a new analyzed statement as array and
# returns an array of the parsed statement with individual blocks
def remove_brackets_around_variables(arr, variables):
	"""
	Removes brackets around single variables, e.g., (P)
	:param arr:
	:param variables:
	:return:
	"""
	for i in range(0, len(arr) - 2):
		if arr[i] in variables:
			left_of_variable = arr[i - 1]
			# variable_itself = arr[i]
			right_of_variable = arr[i + 1]
			if left_of_variable in LEFT_BRACKETS and right_of_variable in RIGHT_BRACKETS:
				arr.pop(i - 1)
				arr.pop(i)
	return arr


def add_brackets_around_unary_connectives(arr, variables):
	"""
	Adds brackets around unary connectives.
	:param arr:
	:param variables:
	:return:
	"""
	# print("Debug: ", arr, variables, sep='\n')
	for i in range(len(arr)):
		if arr[i] in UNARY_CONNECTIVES:  # we have a unary connective
			if arr[i+1] in variables:  # unary connective is next to a variable
				if arr[i-1] in LEFT_BRACKETS and arr[i+2] in RIGHT_BRACKETS:  # there is brackets around it
					# good case
					continue
				elif arr[i-1] in BINARY_CONNECTIVES or arr[i+2] in BINARY_CONNECTIVES:  # there is no brackets around it
					arr.insert(i, '(')
					arr.insert(i+3, ')')
	return arr
