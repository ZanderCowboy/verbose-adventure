from Components.constants import OPEN_ARROW, DASH, CLOSE_ARROW, COND_ELEM, BICOND_ELEM, PRE_CHECK
from Logging.logging_config import logger


def create_conditionals(array_of_elements: list) -> list:
	"""
	Creates the conditional -> from ['-', '>'] and
	biconditional <-> from ['<', '-', '>'].

	:rtype: list
	:param array_of_elements: takes a statement with individual pieces in an array.
	:return: Returns a new array with connectives as one element.
	"""
	logger.debug("Creating one-piece conditionals from single elements.")

	# Do a search for '-', and if found continue, o.w. return.
	logger.debug("Searching for a '-' in array_of_elements=%s", array_of_elements)
	end_of_line = False
	for i, char in enumerate(array_of_elements):
		if i == len(array_of_elements) - 1:
			end_of_line = True
		if char not in PRE_CHECK:  # no symbols present
			if end_of_line:
				logger.debug("Search for conditionals finished and none were found, returning.")
				return array_of_elements
			continue
		elif char in PRE_CHECK:
			break

	logger.debug("Conditional symbols were found in %s", array_of_elements)
	conditional_symbol = False
	biconditional_symbol = False
	for i in range(len(array_of_elements)):
		if i == len(array_of_elements):
			break

		char = array_of_elements[i]
		if char == OPEN_ARROW:  # checks to see if we have a biconditional
			if array_of_elements[i + 1] == DASH and array_of_elements[i + 2] == CLOSE_ARROW:
				array_of_elements.pop(i)
				array_of_elements.pop(i)
				array_of_elements.pop(i)
				array_of_elements.insert(i, BICOND_ELEM)
			continue

		# if we have a conditional
		elif (char == DASH and array_of_elements[i + 1] == CLOSE_ARROW and
			  biconditional_symbol is False):  # if we have a conditional
			array_of_elements.pop(i)
			array_of_elements.pop(i)
			array_of_elements.insert(i, COND_ELEM)
			continue
		elif char == CLOSE_ARROW and conditional_symbol is False:
			continue
		else:  # other characters
			if conditional_symbol is False and biconditional_symbol is False:
				pass
			conditional_symbol = False
			biconditional_symbol = False

	logger.debug("array_of_elements=%s", array_of_elements)
	logger.debug("Finished creating conditionals.")
	return array_of_elements
