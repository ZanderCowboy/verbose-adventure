""" Insert """
from computation.table_matrix.recursive_table import recursive_table
from engine_logging.logging_config import logger


def create_matrix(num_of_var: int) -> list:
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
    logger.debug("Creating initial matrix...")

    # Getting the array with the values that will be converted into a matrix
    table_entries = recursive_table(num_of_var)

    new_matrix = []

    row_entries = [""] * num_of_var
    for i in range(2**num_of_var):
        get_row_values = str(table_entries[i])
        for j in range(0, num_of_var):
            row_entries[j] = get_row_values[j]
        new_row = row_entries.copy()
        new_matrix.append(new_row)

    logger.debug("In create_matrix(): new_matrix=%s", new_matrix)
    logger.info("Finished creating the initial 'truth' matrix.")
    logger.info("*** Initial Matrix:\t%s ***", new_matrix)
    return new_matrix
