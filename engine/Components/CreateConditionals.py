OPEN_ARROW = '<'
DASH = '-'
CLOSE_ARROW = '>'
COND_ELEM = "->"
BICOND_ELEM = "<->"
PRE_CHECK = ['<', '-', '>']


def create_conditionals(statement):
	"""
	Creates the conditional -> from ['-', '>'] and
	biconditional <-> from ['<', '-', '>'].

	:param statement: takes a statement with individual pieces in an array.
	:return: Returns a new array with connectives as one element.
	"""

	# Do a search for '-', and if found continue, o.w. return.
	end_of_line = False
	len_of_statement = len(statement)
	for i, char in enumerate(statement):
		if i == len(statement) - 1:
			end_of_line = True
		if char not in PRE_CHECK:  # no symbols present
			if end_of_line:
				return statement
			continue
		elif char in PRE_CHECK:
			break


	elements = []
	conditional_symbol = False
	biconditional_symbol = False
	# todo Fast failing, if '-'
	for i in range(len(statement)):

		char = statement[i]
		# if statement[i] == '<' && statement[i+1] == '-' && statement[i+2] == '>' ...
		if char == OPEN_ARROW:
			if statement[i+1] == DASH and statement[i+2] == CLOSE_ARROW:
				elements.append(BICOND_ELEM)
				biconditional_symbol = True
			continue
		elif char == DASH and biconditional_symbol is False:
			if statement[i + 1] == CLOSE_ARROW:
				elements.append(COND_ELEM)
				conditional_symbol = True
				continue
		elif char == CLOSE_ARROW and conditional_symbol is False:
			continue
		else:
			if conditional_symbol is False and biconditional_symbol is False:
				elements.append(char)
			conditional_symbol = False
			biconditional_symbol = False

	return elements
