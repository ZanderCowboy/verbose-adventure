OPEN_ARROW = '<'
DASH = '-'
CLOSE_ARROW = '>'
COND_ELEM = "->"
BICOND_ELEM = "<->"
PRE_CHECK = ['<', '-', '>']


def create_conditionals(array_of_elements: list) -> list:
	"""
	Creates the conditional -> from ['-', '>'] and
	biconditional <-> from ['<', '-', '>'].

	:rtype: list
	:param array_of_elements: takes a statement with individual pieces in an array.
	:return: Returns a new array with connectives as one element.
	"""

	# Do a search for '-', and if found continue, o.w. return.
	end_of_line = False
	# len_of_array = len(array_of_elements)
	for i, char in enumerate(array_of_elements):
		if i == len(array_of_elements) - 1:
			end_of_line = True
		if char not in PRE_CHECK:  # no symbols present
			if end_of_line:
				return array_of_elements
			continue
		elif char in PRE_CHECK:
			break

	conditional_symbol = False
	biconditional_symbol = False
	# todo Fast failing, if '-'

	for i in range(len(array_of_elements)):
		if i == len(array_of_elements):
			break

		char = array_of_elements[i]
		# if statement[i] == '<' && statement[i+1] == '-' && statement[i+2] == '>' ...
		if char == OPEN_ARROW:  # checks to see if we have a biconditional
			if array_of_elements[i + 1] == DASH and array_of_elements[i + 2] == CLOSE_ARROW:
				# elements.append(BICOND_ELEM)
				# biconditional_symbol = True
				array_of_elements.pop(i)
				array_of_elements.pop(i)
				array_of_elements.pop(i)
				array_of_elements.insert(i, BICOND_ELEM)
			continue

		# elif char == DASH and biconditional_symbol is False:  # if we have a conditional
		elif (char == DASH and array_of_elements[i + 1] == CLOSE_ARROW and
			  biconditional_symbol is False):  # if we have a conditional
			# if array_of_elements[i + 1] == CLOSE_ARROW:
			# elements.append("->")
			# conditional_symbol = True
			array_of_elements.pop(i)
			array_of_elements.pop(i)
			array_of_elements.insert(i, COND_ELEM)
			continue
		elif char == CLOSE_ARROW and conditional_symbol is False:
			continue
		else:  # other characters
			if conditional_symbol is False and biconditional_symbol is False:
				# elements.append(char)
				pass
			conditional_symbol = False
			biconditional_symbol = False

	return array_of_elements
