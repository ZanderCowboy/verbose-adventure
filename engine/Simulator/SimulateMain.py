from Computation.EvaluateStatement import *
from Computation.TableMatrix.DisplayMatrix import display_matrix
from Logging.logging_config import logger
from Parser.Checks.CheckBrackets import check_left_and_right_brackets
from Parser.Checks.CheckForIllegalCharacters import check_for_illegal_characters
# from Parser.Checks import CheckBrackets, CheckForIllegalCharacters
from Parser.Checks.CheckBrackets import UnequalBracketsExcept
from Parser.Checks.CheckForIllegalCharacters import IllegalCharactersException
from Simulator.UserInput import user_input
from Simulator.input_statements import *


def simulate_main():
	"""
	This simulates Main.py
	"""
	logger.debug("Calling simulate_main()...")

	for idx, statement in enumerate(test_cases, start=1):
		logger.debug("Processing statement=%s", statement)
		# print(f"\n\nTest Case {idx}: Processing statement '{statement}'...")

		# First complete all checks
		try:
			logger.info("Before proceeding, checks for unequal brackets and "
						"illegal characters are done.")
			if (check_left_and_right_brackets(statement) and
					check_for_illegal_characters(statement)):
				pass
		except UnequalBracketsExcept as ce:
			logger.error("Unequal Brackets Exception: ", ce)
			continue
		except IllegalCharactersException as ice:
			logger.error("Illegal Characters Exception: ", ice)
			continue
		else:
			# print("No exception occurred!")
			pass

		# todo Look into why statement is sent to user_input() and then
		#  returned again

		logger.warning("All checks are valid, proceeding with extracting all "
					"needed information.")
		number_of_variables, variables_as_array, provided_statement, elements_in_tree = (
			user_input(statement))
		logger.debug("In simulate_main(): \nnumber_of_variables=%d, \nvariables_as_array=%s, "
					 "\nprovided_statement=%s, \nelements_in_tree=%s",
					 number_of_variables, variables_as_array, provided_statement, elements_in_tree)

		print_details(number_of_variables, variables_as_array, provided_statement, elements_in_tree)


		# logger.warning("Starting with evaluation of array...")
		final_value_array, returned_matrix, all_variables = (
			evaluate_statement_as_array(number_of_variables, variables_as_array, elements_in_tree))
		logger.warning("Finished evaluating statement.")
		logger.debug("final_value_array=%s, returned_matrix=%s, all_variables=%s", final_value_array, returned_matrix, all_variables)

		# todo Ticket: Add and Modify Code for Console Output
		display_matrix(number_of_variables, returned_matrix, all_variables)

		logger.debug("Returning from simulate_main()...")


def print_details(number_of_variables: int, variables_as_array, provided_statement, elements_in_tree):
	logger.info("Printing details...")
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
