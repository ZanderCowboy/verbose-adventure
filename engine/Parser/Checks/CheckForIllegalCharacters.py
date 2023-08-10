from Components.RegularExpression import validate_input
from Components.Constants import *


class IllegalCharactersException(Exception):
	pass


def check_for_illegal_characters(string):
	for i in range(len(string)):
		char = string[i]
		if char in LEFT_BRACKETS or char in RIGHT_BRACKETS or char in WHITE_SPACES:
			continue
		if validate_input(char):
			continue
		else:
			raise IllegalCharactersException("String contains illegal characters, please check and try again")
