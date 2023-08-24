from Computation.TableMatrix.RecursiveTable import recursive_table
from Logging.logging_config import logger


def create_matrix(num_of_var):
    """
    This takes the number of variables and produces an initial corresponding
    input matrix (also known as a truth table) with 2*exp(num_of_var) row
    entries with T and F values.

    For example:
    create_matrix(2) => [['T', 'T'], ['T', 'F'], ['F', 'T'], ['F', 'F']]
    or equivalently
    [   ['T', 'T'],
        ['T', 'F'],
        ['F', 'T'],
        ['F', 'F']
    ].

    :param num_of_var: (int) Number of variables used in statement.
    :return: Returns a matrix, with alternating T/F values for the number of
    variables as columns and 2*exp(num_of_var) rows.
    """
    logger.debug("Calling create_matrix(%d)", num_of_var)

    # Getting the array with the values that will be converted into a matrix
    table_entries = recursive_table(num_of_var)

    # todo Refactor the code; unused matrix found
    matrix = [[0] * num_of_var] * (2 ** num_of_var)
    new_matrix = []

    row_entries = [0] * num_of_var
    for i, row in enumerate(matrix):
        get_row_values = str(table_entries[i])
        for j in range(0, num_of_var):
            row_entries[j] = get_row_values[j]
        new_row = row_entries.copy()
        new_matrix.append(new_row)

    logger.info("Created the matrix with alternating T/F values from the given "
                "number of variables. \n new_matrix=%s \n Returning.", new_matrix)
    return new_matrix
