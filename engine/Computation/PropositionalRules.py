# This file is to give the rules to calculate the propositional logic.
from math import log2
from Components.Constants import TRUE, FALSE

# todo double negation cancel out
# todo 'negation', 'for all', 'there exists' bind most tightly; then disj and
#  conj; then impl. (which is right-associative)
# todo Add global variables T and F


def conjunction(left, right):
	"""
	AND
	:param right:
	:param left:
	:return:
	"""

	# todo Add Exception
	if len(left) != len(right):  # if they are not equal, raise and skip the rest
		raise Exception

	num = int(log2(len(left)))
	new_row_values = []
	for i in range(0, 2 ** num):
		if left[i] == TRUE and right[i] == TRUE:
			new_row_values.append(TRUE)
		else:
			new_row_values.append(FALSE)

	return new_row_values


def disjunction(left, right):
	"""
	OR
	:param right:
	:param left:
	:return:
	"""

	# todo Add Exception
	if len(left) != len(right):  # if they are not equal, raise and skip the rest
		raise Exception

	num = int(log2(len(left)))
	new_row_values = []
	for i in range(0, 2 ** num):
		if left[i] == FALSE and right[i] == FALSE:
			new_row_values.append(FALSE)
		else:
			new_row_values.append(TRUE)

	return new_row_values


def negation(left):
	"""
	NEGATION
	:param left:
	:return:
	"""

	num = int(log2(len(left)))
	new_row_value = []
	# print("Negation")
	for i in range(0, 2 ** num):
		if left[i] == TRUE:
			new_row_value.append(FALSE)
		elif left[i] == FALSE:
			new_row_value.append(TRUE)

	return new_row_value


def conditional(left, right):
	"""
	IMPLICATION
	:param left:
	:param right:
	:return:
	"""

	# todo Add Exception
	if len(left) != len(right):  # if they are not equal, raise and skip the rest
		raise Exception

	num = int(log2(len(left)))
	new_row_value = []
	# print("Conditional")
	for i in range(0, 2 ** num):
		if left[i] == TRUE and right[i] == FALSE:
			new_row_value.append(FALSE)
		else:
			new_row_value.append(TRUE)

	return new_row_value


def biconditional(left, right):
	"""
	iff
	:param left:
	:param right:
	:return:
	"""

	# todo Add Exception
	if len(left) != len(right):  # if they are not equal, raise and skip the rest
		raise Exception

	num = int(log2(len(left)))
	new_row_value = []
	# print("Biconditional")
	for i in range(0, 2 ** num):
		if left[i] == right[i]:
			new_row_value.append(TRUE)
		else:
			new_row_value.append(FALSE)

	return new_row_value
