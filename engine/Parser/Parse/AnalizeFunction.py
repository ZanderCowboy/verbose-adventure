# Analize statement, extracts all the relevant information and variables
from Components.FindVariables import find_variables
from Components.Sanitizer import clean_whitespaces
from Components.Sanitizer import clean_commas
from Components.CreateConditionals import create_conditionals


# returns
def analize_statement(statement):
    """
    Analyzes statement to determine the number of variables, and split into an
    array of elements
    :param statement:
    :return: length of array of variables as int, array of variables,
    string of variables, and array with elements
    """

    statement = clean_whitespaces(statement)
    statement = clean_commas(statement)

    # find variables
    variables_arr, variables_str = find_variables(statement)

    # sterilize statement into elements
    elements = create_conditionals(statement)

    return len(variables_arr), variables_arr, variables_str, elements

