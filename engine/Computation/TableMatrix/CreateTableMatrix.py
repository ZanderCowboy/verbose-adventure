# Creates the truth table matrix with initial values.

from Computation.TableMatrix.RecursiveTable import recursive_table


def create_matrix(num_of_var):
    """
    This takes the number of variables and produces an initial corresponding
    input matrix (also known as a truth table) with 2*exp(num_of_var) row
    entries with T and F values.
    # todo Add example.
    For example: create_matrix(2) will output
    [['T', 'T'], ['T', 'F'], ['F', 'T'], ['F', 'F']] or equivalently
    [   ['T', 'T'],
        ['T', 'F'],
        ['F', 'T'],
        ['F', 'F']
    ].

    :param num_of_var: (int) Number of variables used in statement.
    :return: Returns a matrix, with alternating T/F values for the number of
    variables as columns and 2*exp(num_of_var) rows.
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
