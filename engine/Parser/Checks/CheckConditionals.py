from Logging.logging_config import logger
from Components.Constants import *


class InvalidConditionalSymbolsExcept(Exception):
	pass


def check_conditionals(array_of_elements: list, variables_arr: list) -> bool:
	# todo Add docs
	logger.debug("Calling check_conditionals(%s, %s)...", array_of_elements, variables_arr)
	exception = False

	conditional_symbol = False
	biconditional_symbol = False
	for i, char in enumerate(array_of_elements):
		if i < len(array_of_elements) - 2:
			char_two = array_of_elements[i+2]
		if i < len(array_of_elements) - 1:
			char_one = array_of_elements[i+1]
		if char in VALID_BRACKETS or char in variables_arr:
			continue
		elif char in OR_SYMBOL or char in AND_SYMBOL or char in NOT_SYMBOL:
			continue
		elif char in OPEN_ARROW:  # <
			if char_one in DASH:  # <-
				if char_two in CLOSE_ARROW:  # <->
					biconditional_symbol = True
					continue
				if char_two in LEFT_BRACKETS or char_two in RIGHT_BRACKETS or char_two in variables_arr:  # <-( or <-) or <-A
					exception = True
					break
			if char_one in LEFT_BRACKETS or char_one in RIGHT_BRACKETS or char_one in variables_arr:  # <( or <) or <A
				exception = True
				break
		elif char in DASH:  # -
			if char_one in CLOSE_ARROW:  # ->
				conditional_symbol = True
				continue
			if char_one in LEFT_BRACKETS or char_one in RIGHT_BRACKETS or char_one in variables_arr:  # -( or -) or -A
				exception = True
				break
		elif char in CLOSE_ARROW and (not biconditional_symbol and not conditional_symbol):  # < or >
			if char_one in LEFT_BRACKETS or char_one in RIGHT_BRACKETS or char_one in variables_arr:  # <( or <) or <A
				exception = True
				break
		else:
			pass
			# logger.debug("Unprocessed case. Please inspect!")

	if exception:
		logger.exception("FAIL: The conditional symbols are invalid or insufficient: ")
		raise InvalidConditionalSymbolsExcept("The symbols for conditionals are invalid or insufficient.")

	logger.info("PASS: Any conditional symbols present, are in the desired form.")
	return True
