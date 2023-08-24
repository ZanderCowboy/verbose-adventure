from Computation.EvaluateStatement import *
from Computation.TableMatrix.DisplayMatrix import display_matrix
from Logging.logging_config import logger
from Parser.Checks import CheckBrackets, CheckForIllegalCharacters
from Parser.Checks.CheckBrackets import UnequalBracketsExcept
from Parser.Checks.CheckForIllegalCharacters import IllegalCharactersException
from Simulator.UserInput import user_input
from Simulator.input_statements import *


def simulate_main():
	"""
	This simulates Main.py
	:return: No return, void function.
	"""
	logger.debug("Calling simulate_main()...")

	for idx, statement in enumerate(test_cases, start=1):
		logger.info("Processing statement=%s", statement)
		# print(f"\n\nTest Case {idx}: Processing statement '{statement}'...")

		# First complete all checks
		try:
			logger.info("Before proceeding, checks for unequal brackets and "
						"illegal characters are done: ")
			if (CheckBrackets.check_left_and_right_brackets(statement) and
					CheckForIllegalCharacters.check_for_illegal_characters(statement)):
				pass
		except UnequalBracketsExcept as ce:
			logger.error("Unequal Brackets Exception: ", ce)
			# print("Unequal Brackets Exception: ", ce)
			continue
		except IllegalCharactersException as ice:
			logger.error("Illegal Characters Exception: ", ice)
			# print("Illegal Characters Exception: ", ice)
			continue
		else:
			# print("No exception occurred!")
			pass

		# todo Look into why statement is sent to user_input() and then
		#  returned again

		logger.info("All checks are valid, proceeding with extracting all "
					"needed information from the statement %s", statement)
		number_of_variables, variables_as_array, provided_statement, elements_in_tree = (
			user_input(statement))

		print_details(number_of_variables, variables_as_array, provided_statement, elements_in_tree)


		logger.info("Evaluating array...")
		final_value_array, returned_matrix, all_variables = (
			evaluate_statement_as_array(number_of_variables, variables_as_array, elements_in_tree))

		# todo look for library for output
		display_matrix(number_of_variables, returned_matrix, all_variables)


def print_details(number_of_variables: int, variables_as_array, provided_statement, elements_in_tree):
	logger.debug("Calling print_details(%d, %s, %s, %s)...", number_of_variables, variables_as_array, provided_statement, elements_in_tree)
	logger.info("***********************************************************")
	logger.info("Displaying returned values in simulate_main():")
	logger.info("number_of_variables:\t%d", number_of_variables)
	logger.info("variables_as_array:\t%s", variables_as_array)
	logger.info("provided_statement:\t%s", provided_statement)
	logger.info("elements_in_tree:\t\t%s", elements_in_tree)
	logger.info("***********************************************************")

	# print("***********************************************************")
	# print("Displaying returned values in main():")
	# print("number of variables:\t\t" + str(number_of_variables))
	# print("variables array:\t\t\t" + str(variables_as_array))
	# print("given statement:\t\t\t" + provided_statement)
	# print("elements from statement:\t" + str(elements_in_tree))
	# print("***********************************************************")
