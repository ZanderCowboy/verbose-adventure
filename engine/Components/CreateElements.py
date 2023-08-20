def create_array_of_elements(statement: str) -> list:
	"""
	This takes a statement as a string and returns an array of elements
	:rtype: list
	:param statement: string
	:return: Returns an array of elements
	"""
	array_of_elements = []
	for i in range(len(statement)):
		char = statement[i]
		array_of_elements.append(char)
	return array_of_elements
