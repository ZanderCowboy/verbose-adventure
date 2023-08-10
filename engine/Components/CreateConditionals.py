def create_conditionals(array_of_elements: list) -> list:
	"""
	Creates the conditional -> from ['-', '>'] and
	biconditional <-> from ['<', '-', '>'].

	:rtype: list
	:param array_of_elements: takes a statement with individual pieces in an array.
	:return: Returns a new array with connectives as one element.
	"""

	# elements = []
	conditional_symbol = False
	biconditional_symbol = False
	for i in range(len(array_of_elements)):
		if i == len(array_of_elements):
			break
		char = array_of_elements[i]
		if char == '<':  # checks to see if we have a biconditional
			if array_of_elements[i + 1] == '-':
				if array_of_elements[i + 2] == '>':
					# elements.append("<->")
					# biconditional_symbol = True
					array_of_elements.pop(i)
					array_of_elements.pop(i)
					array_of_elements.pop(i)
					array_of_elements.insert(i, "<->")
			continue

		elif char == '-' and biconditional_symbol is False:  # if we have a conditional
			if array_of_elements[i + 1] == '>':
				# elements.append("->")
				# conditional_symbol = True
				array_of_elements.pop(i)
				array_of_elements.pop(i)
				array_of_elements.insert(i, "->")
				continue
		elif char == '>' and conditional_symbol is False:
			continue
		else:  # other characters
			if conditional_symbol is False and biconditional_symbol is False:
				# elements.append(char)
				pass
			conditional_symbol = False
			biconditional_symbol = False

	return array_of_elements
