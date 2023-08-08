# todo changes statement to something that we can use
# todo change to something that the system can use
# todo add brackets
# todo Change connectives to one common set
# todo Change lower case letters to upper case


# for example: change & to ^, | to v

def add_brackets(statement):
	"""

	:param statement:
	:return:
	"""
	pass
	new_string = ""

	return new_string


def sanitize_statements(statement):
	"""

	:param statement:
	:return:
	"""
	final_string = ""

	new_string = add_brackets(statement)

	return final_string


def clean_commas(statement):
	"""
	Removes commas if more than one statement is given.

	:param statement: given statement
	:return: returns a statement with commas removed
	"""
	return statement.replace(",", "")


def clean_whitespaces(statement):
	"""

	:param statement: given statement
	:return: returns a statement with whitespaces removed
	"""
	return statement.replace(" ", "")

