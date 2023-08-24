from Components.RegularExpression import validate_input
from Components.Constants import *
from Logging.logging_config import logger


class IllegalCharactersException(Exception):
	pass


def check_for_illegal_characters(statement):
	"""
	Checks for illegal characters in the given statement
	:param statement: (string)
	:return: returns true in case statement is clear of illegal characters and
	raises an exception if not.
	"""
	logger.debug("Calling CheckForIllegalCharacters.check_for_illegal_characters(%s)", statement)

	for i in range(len(statement)):
		char = statement[i]
		if char in LEFT_BRACKETS or char in RIGHT_BRACKETS or char in WHITE_SPACES:
			continue
		if validate_input(char):
			continue
		else:
			logger.error("String contains illegal characters, please check and try again")
			raise IllegalCharactersException("String contains illegal characters, please check and try again")

	logger.info("There were no illegal characters found, returning.")
	return True  # returns True in case no fowl characters are found
