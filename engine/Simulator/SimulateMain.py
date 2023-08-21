from Computation.EvaluateStatement import *
from Computation.TableMatrix.DisplayMatrix import display_matrix
from Parser.Checks import CheckBrackets, CheckForIllegalCharacters
from Parser.Checks.CheckBrackets import UnequalBracketsExcept
from Parser.Checks.CheckForIllegalCharacters import IllegalCharactersException
from Simulator.UserInput import *
from Simulator.input_statements import *
from Logging.logging_config import logger


def simulate_main():
	"""
	This simulates Main.py
	:return: No return, void function.
	"""

	logger.info("In SimulateMain.py")
	for idx, statement in enumerate(test_cases, start=1):
		print(f"\n\nTest Case {idx}: Processing statement '{statement}'...")

		# First complete all checks
		try:
			logger.info("Calling CheckBrackets.check_left_and_right_brackets() "
						"and CheckForIllegalCharacters.check_for_illegal_characters()...")
			if (CheckBrackets.check_left_and_right_brackets(statement) and
					CheckForIllegalCharacters.check_for_illegal_characters(statement)):
				pass
		except UnequalBracketsExcept as ce:
			print("Unequal Brackets Exception: ", ce)
			continue
		except IllegalCharactersException as ice:
			print("Illegal Characters Exception: ", ice)
			continue
		else:
			# print("No exception occurred!")
			pass

		# todo Look into why statement is sent to user_input() and then
		#  returned again
		number_of_variables, variables_as_array, provided_statement, elements_in_tree = (
			user_input(statement))

		print_details(number_of_variables, variables_as_array, provided_statement, elements_in_tree)

		final_value_array, returned_matrix, all_variables = (
			evaluate_statement_as_array(number_of_variables, variables_as_array, elements_in_tree))

		# todo look for library for output
		display_matrix(number_of_variables, returned_matrix, all_variables)


def print_details(number_of_variables, variables_as_array, provided_statement, elements_in_tree):
	print("***********************************************************")
	# print("In main():")
	print("Displaying returned values in main():")
	print("number of variables:\t\t" + str(number_of_variables))
	print("variables array:\t\t\t" + str(variables_as_array))
	# print("variables string:\t\t\t" + variables_as_string)
	print("given statement:\t\t\t" + provided_statement)
	print("elements from statement:\t" + str(elements_in_tree))
	print("***********************************************************")
