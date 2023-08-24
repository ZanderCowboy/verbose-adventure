from Logging.logging_config import logger


def create_array_of_elements(statement: str) -> list:
	"""
	This takes a statement as a string and returns an array of elements
	:rtype: list
	:param statement: string
	:return: Returns an array of elements
	"""
	logger.debug("Calling create_array_of_elements(%s)", statement)

	array_of_elements = []
	for i in range(len(statement)):
		char = statement[i]
		array_of_elements.append(char)

	logger.info("Converted the statement into an array from a string. "
				"array_of_elements=%s", array_of_elements)
	return array_of_elements
