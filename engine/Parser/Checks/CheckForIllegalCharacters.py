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
	logger.debug("Calling check_for_illegal_characters(%s)", statement)
	logger.debug("******************** starting input validation *******************")
	for i in range(len(statement)):
		char = statement[i]
		if char in LEFT_BRACKETS or char in RIGHT_BRACKETS or char in WHITE_SPACES:
			continue
		if validate_input(char):
			continue
		else:
			logger.exception("FAIL: String contains illegal characters, please check and try again: char=%s", char)
			raise IllegalCharactersException("String contains illegal characters, please check and try again")
	logger.debug("******************** finished input validation *******************")

	logger.info("PASS: There were no illegal characters found.")
	return True  # returns True in case no fowl characters are found
