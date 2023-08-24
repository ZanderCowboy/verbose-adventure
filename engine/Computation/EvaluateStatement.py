from math import log2

from Computation.SwitchConnectives import switch_case
from Computation.TableMatrix.CreateTableMatrix import create_matrix
from Logging.logging_config import logger


# todo restructure to have initial call in one function and another. Function in function
def evaluate_statement_as_array(number_of_variables, variables_as_array, elements_in_tree):
	"""

	:param number_of_variables:
	:param variables_as_array:
	:param elements_in_tree:
	:return:
	"""

	logger.debug("Calling evaluate_statement_as_array(%d, %s, %s)...", number_of_variables, variables_as_array, elements_in_tree)
	counter = 0
	# todo Add a new column entry for each row, |.
	matrix = create_matrix(number_of_variables)

	returned_array, final_variable_combined, returned_matrix, all_variables = (
		evaluate_array(elements_in_tree, counter, matrix, variables_as_array))

	all_variables.append(final_variable_combined[0])

	logger.info("Finised evaluating statement into an array: \nreturned_array=%s, "
				"\nreturned_matrix=%s, \nall_variables=%s; \nreturning.", returned_array, returned_matrix, all_variables)
	return returned_array, returned_matrix, all_variables


def evaluate_array(array: list, counter: int, matrix: list, variables: list):
	"""
	acts as inner recursive function
	:param matrix: matrix
	:param counter: counter
	:param variables: array
	:param array: elements_in_tree
	:return: returned_array, final_variable_combined, returned_matrix, all_variables
	"""
	logger.debug("Calling evaluate_array(%s, %d, %s, %s)...", array, counter, matrix, variables)

	# todo Fix bug for ((!Q) -> (!P))
	# if negation is encounter, add placeholder value in front
	if len(array) == 2:
		blank = '_'
		array = [blank, array[0], array[1]]

	left_array = array[0]
	connective = array[1]
	right_array = array[2]

	# induction case
	# ******************* LEFT ************************
	if len(left_array) != 1:
		temp_left_array = left_array

		counter += 1
		array_evaluated, left_array, placeholder, placeholder = evaluate_array(temp_left_array, counter, matrix, variables)
		counter -= 1
		variables = add_array_to_matrix(matrix, array_evaluated, variables, left_array)

	# ******************* RIGHT ************************
	if len(right_array) != 1:
		temp_right_array = right_array

		counter += 1
		array_evaluated, right_array, placeholder, placeholder = evaluate_array(temp_right_array, counter, matrix, variables)
		counter -= 1
		variables = add_array_to_matrix(matrix, array_evaluated, variables, right_array)

	# ******************** BASE CASE ************************
	final_variable_combined = []

	if len(left_array) == 1 and len(right_array) == 1:
		# find variables for left and right
		left_variable = left_array[0]
		right_variable = right_array[0]

		left_variable_position = -1
		right_variable_position = -1

		# get position for variable in list of variables as a string
		for i, item in enumerate(variables):
			if left_variable == item:
				left_variable_position = i
				break
		for i, item in enumerate(variables):
			if right_variable == item:
				right_variable_position = i
				break

		# call matrix for each variable, and assign to temp
		temp_left = []
		temp_right = []
		for i in range(0, 2 ** int(log2(len(matrix)))):
			row_in_matrix = matrix[i]
			temp_left.append(row_in_matrix[left_variable_position])
			temp_right.append(row_in_matrix[right_variable_position])
		returned_array = switch_case(connective, temp_left, temp_right)

		# get array item for combined variable
		if len(left_array) == 1 and len(right_array) == 1:
			temp_array = [left_array, connective, right_array]
			final_variable_combined = set_new_array(temp_array)

		if len(final_variable_combined) == 1 and counter == 0:
			# append returned_array to matrix
			for i in range(len(returned_array)):
				entry_in_return_array = returned_array[i]
				matrix[i].append(entry_in_return_array)

		logger.info("Evaluation of statement is done: \nreturned_array=%s, "
					"\nfinal_variable_combined=%s, \nmatrix=%s, \nvariables=%s;"
					"returning.", returned_array, final_variable_combined, matrix, variables)
		return returned_array, final_variable_combined, matrix, variables


def set_new_array(temp_array):
	# todo Finish documentation
	"""

	:param temp_array:
	:return:
	"""
	logger.debug("Calling set_new_array(%s)...", temp_array)

	left_part = temp_array[0]
	connective = temp_array[1]
	right_part = temp_array[2]

	new_string = ""

	# look at left part
	if left_part[0] == '_':
		pass
	elif len(left_part[0]) == 1:
		new_string += left_part[0]
	elif len(left_part[0]) > 1:
		temp_part = "(" + left_part[0] + ")"
		new_string += temp_part

	# middle part
	new_string += connective

	# look at right part
	if len(right_part[0]) == 1:
		new_string += right_part[0]
	elif len(right_part[0]) > 1:
		temp_part = "(" + right_part[0] + ")"
		new_string += temp_part
	new_array = [new_string]

	logger.info("Finished setting new array. \nnew_array=%s, returning.", new_array)
	return new_array


def add_array_to_matrix(matrix, array_evaluated, variables, variable_entry):
	# todo Finish documentation
	"""
	this should be a function that adds a new entry in each column of the rows
	:param matrix:
	:param array_evaluated:
	:param variables:
	:param variable_entry:
	:return:
	"""
	logger.debug("Calling add_array_to_matrix(%s, %s, %s, %s)...", matrix, array_evaluated, variables, variable_entry)

	for i in range(len(matrix)):
		row_entry = matrix[i]
		entry_to_add = array_evaluated[i]
		row_entry.append(entry_to_add)
	variables.append(variable_entry[0])  # append new 'variable' to array of variables

	logger.info("Added array to matrix, %s, returning.", variables)
	return variables
