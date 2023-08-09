# from Computation.EvaluateStatement import *
# # from Computation.TableMatrix.Matrix import create_matrix
# from Computation.TableMatrix.DisplayMatrix import display_matrix
# from Simulator.UserInput import *
# # import Parser.Checks.IllegalCharacters as badCharacters
#
# # main()
# print("***********************************************************")
# print("In main():")
#
# # creates and initializes variables
# (number_of_variables, variables_as_array, variables_as_string,
#  provided_statement, elements_in_tree) = user_input()
#
# print("\nDisplaying returned values in main():")
# print("number of variables:\t\t" + str(number_of_variables))
# print("variables array:\t\t\t" + str(variables_as_array))
# print("variables string:\t\t\t" + variables_as_string)
# print("given statement:\t\t\t" + provided_statement)
# print("elements from statement:\t" + str(elements_in_tree))
# print("***********************************************************")
# # matrix = create_matrix(num_of_variables)
# # print(matrix)
#
#
# # badCharacters.check_for_illegal_characters("test a string")
#
#
# # print("calling EvaluateStatement.py")
# final_value_array, returned_matrix, all_variables = (
# 	evaluate_statement_as_array(number_of_variables, variables_as_array, elements_in_tree))
#
# # print("Debug: ", final_value_array, final_variable_combined, returned_matrix, all_variables)
#
# # todo Add last value to array and change display_matrix()
# display_matrix(number_of_variables, returned_matrix, all_variables)

from Simulator.SimulateMain import *

simulate_main()
