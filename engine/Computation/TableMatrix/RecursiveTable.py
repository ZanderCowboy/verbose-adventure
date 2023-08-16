# Creates a table of T's and F's recursively


def recursive_table(n):
	"""
	Creates a list of T's and F's recursively, given the number of variables
	# todo Finish example here.
	For example: recursive_table(1) => ['T', 'F'] and
	recursive_table(3) =>
	:param n: (int) Number of variables
	:return: Returns an array table with T/F values
	"""
	# array_table = []
	if n == 1:
		array_table = ['T', 'F']
	# array_table = []
	elif n != 1:
		array_table = recursive_table(n - 1)
		temp_table = []
		temp_table = array_table.copy()
		for j in range(0, int(2 ** n / 2)):
			if j % 2 == 0:  # even
				array_table.insert(j * 2, temp_table[j])
			elif j % 2 == 1:  # odd
				array_table.insert(j * 2, temp_table[j])

	if n > 1:
		for i in range(0, 2 ** n):
			if i % 2 == 0:  # even
				array_table[i] = str(array_table[i]) + 'T'
			elif i % 2 == 1:  # odd
				array_table[i] = str(array_table[i]) + 'F'

	# print(recursive_table(n))
	return array_table
