

def create_conditionals(statement):
	"""
	Creates the conditional -> from ['-', '>'] and
	biconditional <-> from ['<', '-', '>'].

	:param statement: takes a statement with individual pieces in an array.
	:return: Returns a new array with connectives as one element.
	"""

	elements = []
	conditional_symbol = False
	biconditional_symbol = False
	for i in range(len(statement)):
		char = statement[i]
		if char == '<':
			if statement[i + 1] == '-':
				if statement[i + 2] == '>':
					elements.append("<->")
					biconditional_symbol = True
			continue
		elif char == '-' and biconditional_symbol is False:
			if statement[i + 1] == '>':
				elements.append("->")
				conditional_symbol = True
				continue
		elif char == '>' and conditional_symbol is False:
			continue
		else:
			if conditional_symbol is False and biconditional_symbol is False:
				elements.append(char)
			conditional_symbol = False
			biconditional_symbol = False

	return elements
