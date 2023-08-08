# Creates the truth table matrix with initial values.

from Computation.TableMatrix.RecursiveFunction import recursive_table


def create_matrix(num_of_var):
    """
    This takes a number of variables and produces a corresponding matrix
    with num_of_var entries and T and F values
    :param num_of_var: Number of variables used in statement
    :return: Returns a matrix with alternating T/F values for the number of
    variables.
    """
    table_entries = recursive_table(num_of_var)

    matrix = [[0] * num_of_var] * (2 ** num_of_var)
    new_matrix = []

    row_entries = [0] * num_of_var
    for i, row in enumerate(matrix):
        # print(row)
        get_row_values = str(table_entries[i])
        # print(get_row_values)
        for j in range(0, num_of_var):
            row_entries[j] = get_row_values[j]
        # print(row_entries)
        new_row = row_entries.copy()
        new_matrix.append(new_row)

    return new_matrix
