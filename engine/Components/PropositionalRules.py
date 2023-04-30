# This file is to give the rules to calculate the propositional logic.

#todo double negation cancel out
#todo negation, for all, there exists bind most tightly; then disj and conj; then impl. (which is right-associative)

# matr = LogicCalculator.create_matrix(LogicCalculator.num_of_variables)


# AND
def conjugation(num, matr):
	new_row_value = []
	left = ""
	right = ""
	temp_val = ''

	print("Conjunction")
	for i in range(0, 2 ** num):
		temp_row = matr[i]

		for j in range(num):
			temp = temp_row[j]
			# right = temp_row[j+1]
			# if left == 'F' or right == 'F':
			if temp == 'F':
				temp_val = 'F'
			else:
				temp_val = 'T'

		new_row_value.append(temp_val)
	return new_row_value

# OR
def disjunction(num, matr):
	new_row_value = []
	left = ""
	right = ""
	temp_val = ''

	print("Disjunction")
	for i in range(0, 2 ** num):
		temp_row = matr[i]
		left = temp_row[0]
		right = temp_row[1]

		if left == 'T' or right == 'T':
			temp_val = 'T'
		else:
			temp_val = 'F'
		new_row_value.append(temp_val)
	return new_row_value

# NEGATION
def negation(num, matr):
	new_row_value = []
	temp_val = ''

	print("Negation")
	for i in range(0, 2 ** num):
		temp_row = matr[i]
		temp = temp_row[0]

		if temp == 'T':
			temp_val = 'F'
		else:
			temp_val = 'T'

		new_row_value.append(temp_val)
	return new_row_value

# IMPLICATION
def conditional(num, matr):
	new_row_value = []
	left = ""
	right = ""
	temp_val = ''

	print("Conditional")
	for i in range(0, 2 ** num):
		temp_row = matr[i]
		left = temp_row[0]
		right = temp_row[1]

		if left == 'T':
			if right == 'F':
				temp_val = 'F'
			else:
				temp_val = 'T'
		else:
			temp_val = 'T'
		new_row_value.append(temp_val)
	return new_row_value

# iff
def biconditional(num, matr):
	new_row_value = []
	left = ""
	right = ""
	temp_val = ''

	print("Biconditional")
	for i in range(0, 2 ** num):
		temp_row = matr[i]
		left = temp_row[0]
		right = temp_row[1]

		if (left == 'T' and right == 'T') or (left == 'F' and right == 'F'):
			temp_val = 'T'
		else:
			temp_val = 'F'
		new_row_value.append(temp_val)
	return new_row_value
