from components.print_details import print_details
from Computation.evaluate_statement import *
from Computation.TableMatrix.DisplayMatrix import display_matrix
from engine_logging.logging_config import logger
from Parser.Checks.CheckBrackets import check_left_and_right_brackets
from Parser.Checks.CheckForIllegalCharacters import check_for_illegal_characters
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
		logger.info("Statement:\t%s", statement)

		# First complete all checks
		try:
			logger.info("Before proceeding, doing checks for unequal brackets and "
						"illegal characters.")
			if (check_left_and_right_brackets(statement) and
					check_for_illegal_characters(statement)):
				pass
		except UnequalBracketsExcept as ce:
			logger.exception("Unequal Brackets Exception: ", ce)
			continue
		except IllegalCharactersException as ice:
			logger.exception("Illegal Characters Exception: ", ice)
			continue
		else:
			pass

		# todo Look into why statement is sent to user_input() and then
		#  returned again

		logger.info("All checks are valid, proceeding with extracting "
					"information from statement.")
		number_of_variables, variables_as_array, provided_statement, elements_in_tree = (
			user_input(statement))
		logger.debug("In simulate_main(): \nnumber_of_variables=%d, \nvariables_as_array=%s, "
					 "\nprovided_statement=%s, \nelements_in_tree=%s",
					 number_of_variables, variables_as_array, provided_statement, elements_in_tree)

		print_details("SUMMARY",
					  ("number_of_variables", number_of_variables),
					  ("variables_as_array", variables_as_array),
					  ("provided_statement", provided_statement),
					  ("elements_in_tree", elements_in_tree))

		final_value_array, returned_matrix, all_variables = (
			evaluate_array_as_tree(number_of_variables, variables_as_array, elements_in_tree))
		logger.debug("In simulate_main(): \nfinal_value_array=%s, \nreturned_matrix=%s, \nall_variables=%s",
					 final_value_array, returned_matrix, all_variables)

		print_details("EVALUATE", ("Statement", statement),
					  ("Final Calculated Array", final_value_array),
					  ("All Variables", all_variables),
					  ("Final Matrix", returned_matrix))
		logger.info("Finished evaluating statement.")

		# todo Ticket: Add and Modify Code for Console Output
		display_matrix(number_of_variables, returned_matrix, all_variables)

		logger.debug("Returning from simulate_main()...")
