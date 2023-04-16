from engine.Inputs.UserInput import *

# main()
print("***********************************************************")
print("In main():")
# User Input, Calls user_input() function in LogicCalculator.py
# todo Move user_input() to new file.
# creates and initializes variables
num_of_variables, variables_arr, variables_str, statement, elements = user_input()

print("\nDisplaying returned values in main():")
print("number of variables:\t\t" + str(num_of_variables))
print("variables string:\t\t\t" + variables_str)
print("given statement:\t\t\t" + statement)
print("elements from statement:\t" + str(elements))

print("***********************************************************")
# matrix = create_matrix(num_of_variables)
# print(matrix)


# print(conjugation(num_of_variables, matrix))
# print()
# print(disjunction(num_of_variables, matrix))
# print()
# print(negation(num_of_variables, matrix))
# print()
# print(conditional(num_of_variables, matrix))
# print()
# print(biconditional(num_of_variables, matrix))
# print()

