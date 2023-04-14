# Comment
# todo Check brackets left and right should align
# todo number of variables, in order
# todo T&F values of variables in table, Evaluate sequences little by little (Reassign string with new variables pi_1, pi_2, etc.
# todo Get final array of values


# def create_matrix(num_of_var):
# 	table_entries = recursive_table(num_of_var)
#
# 	matrix = [[0] * num_of_var] * (2 ** num_of_var)
# 	new_matrix = []
#
# 	row_entries = [0] * num_of_var
# 	for i, row in enumerate(matrix):
# 		# print(row)
# 		get_row_values = str(table_entries[i])
# 		# print(get_row_values)
# 		for j in range(0, num_of_var):
# 			row_entries[j] = get_row_values[j]
# 		# print(row_entries)
# 		new_row = row_entries.copy()
# 		new_matrix.append(new_row)
#
# 	return new_matrix


# def user_input():
#     print("In user_input():")
#     # statement = input("Please enter the statement(s): ")
#     print("Please enter the statement(s): P ^ Q, R v (P -> Q), R ^ (Q v P) <-> (R ^ Q) v (R ^ P)")
#     statement = "P ^ Q, R v (P -> Q), R ^ (Q v P) <-> (R ^ Q) v (R ^ P) ^ T"
#     # statement = "P ^ Q"
#     # statement = "P v Q"
#
#     # evaluate statement to determine the number of variables
#     number_of_variables, variables_arr, variables_str, elements = analize_statement(statement)
#
#     print("Out user_input():")
#     return number_of_variables, variables_arr, variables_str, statement, elements


def check_brackets(eva_str):
    # todo Finish check_brackets
    outcome = False

    return outcome
