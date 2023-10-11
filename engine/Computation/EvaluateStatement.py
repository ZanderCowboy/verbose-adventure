from math import log2

from Computation.SwitchConnectives import switch_case
from Computation.TableMatrix.CreateTableMatrix import create_matrix
from Logging.logging_config import logger


def evaluate_array_as_tree(number_of_variables, variables_as_array, elements_in_tree):
	"""
	This is used to take an array of elements in a tree-like structure, and
	evaluates the elements from the bottom up, using a recursive internal
	function.

	:param number_of_variables: Number of variables in statement
	:param variables_as_array: Variables as array
	:param elements_in_tree: Statement with elements in tree-like structure
	:returns: Returns an array with the last evaluation, a matrix containing
	all evaluations and an array with all variables, including auxiliary ones.
	"""
	logger.info("Starting evaluation of array of elements...")

	counter = 0
	matrix = create_matrix(number_of_variables)

	logger.debug("In evaluate_array_as_tree(): \nelements_in_tree=%s, \ncounter=%d, \nmatrix=%s, "
				 "\nvariables_as_array=%s", elements_in_tree, counter, matrix, variables_as_array)
	returned_array, final_variable_combined, returned_matrix, all_variables = (
		evaluate_array(elements_in_tree, counter, matrix, variables_as_array))

	all_variables.append(final_variable_combined[0])

	logger.debug("returned_array=%s, returned_matrix=%s, all_variables=%s", returned_array, returned_matrix, all_variables)
	logger.debug("Finished evaluating array.")
	return returned_array, returned_matrix, all_variables


def evaluate_array(array: list, counter: int, matrix: list, variables: list):
	"""
	This acts as inner recursive function to evaluate an array.

	:param array: Array with elements in a tree structure
	:param counter: Counter to keep track of recursive calls
	:param matrix: Matrix used by evaluation
	:param variables: List of variables in statement
	:return: returned_array, final_variable_combined, returned_matrix, all_variables
	"""
	logger.debug("Calling evaluate_array(%s, %d, %s, %s)...", array, counter, matrix, variables)

	# todo Fix bug for ((!Q) -> (!P))
	# if negation is encountered, add placeholder value in front
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
			final_variable_combined = set_new_array_elem(temp_array)

		if len(final_variable_combined) == 1 and counter == 0:
			# append returned_array to matrix
			for i in range(len(returned_array)):
				entry_in_return_array = returned_array[i]
				matrix[i].append(entry_in_return_array)

		logger.debug("In evaluate_array(): \nreturned_array=%s, \nfinal_variable_combined=%s, \nmatrix=%s, \nvariables=%s",
					 returned_array, final_variable_combined, matrix, variables)
		logger.debug("Evaluation of array in evaluate_array() is done.")
		return returned_array, final_variable_combined, matrix, variables


def set_new_array_elem(temp_array):
	"""
	This is used to set a new array-element from a temporary array of elements
	after calculations were done.
	For example:
	[['T'], 'v', ['P^Q']] => ['Tv(P^Q)']

	:param temp_array: An array that contains 3 parts
	:return: Returns an array with a single combined entry
	"""
	logger.debug("Calling set_new_array_elem(%s)...", temp_array)

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

	logger.debug("new_array=%s", new_array)
	logger.debug("Finished setting new array element.")
	return new_array


def add_array_to_matrix(matrix, array_evaluated, variables, variable_entry):
	"""
	This iterates over a matrix row-by-row and appends the new values in an
	evaluated array to the end of it.

	:param matrix: Matrix where the values should be added
	:param array_evaluated: Evaluated array to append to matrix
	:param variables: Variables in statement
	:param variable_entry: Auxiliary entry to add to array of variables
	:return: Returns an updated array of variables
	"""
	logger.debug("Calling add_array_to_matrix(%s, %s, %s, %s)...", matrix, array_evaluated, variables, variable_entry)

	for i in range(len(matrix)):
		row_entry = matrix[i]
		entry_to_add = array_evaluated[i]
		row_entry.append(entry_to_add)
	variables.append(variable_entry[0])  # append new 'variable' to array of variables

	logger.debug("variables=%s", variables)
	logger.debug("Added array to matrix.")
	return variables
