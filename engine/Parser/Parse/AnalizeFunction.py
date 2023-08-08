# Analize statement, extracts all the relevant information and variables
from Components.FindVariables import find_variables
from Components.Sanitizer import clean_whitespaces
from Components.Sanitizer import clean_commas
from Components.CreateConditionals import create_conditionals


# returns
def analize_statement(statement):
    """
    Analyzes statement to determine the number of variables, and split into an array of elements
    :param statement:
    :return: length of array of variables as int, array of variables, string of variables, and array with elements
    """

    # print("***********************************************************")
    # print("In analize_statement():")
    # print("given statement=" + statement)

    statement = clean_whitespaces(statement)
    statement = clean_commas(statement)

    # find variables
    variables_arr, variables_str = find_variables(statement)
    # print("variables=" + str(variables_arr))
    # print("variables_str=" + variables_str)

    # sterilize statement into elements
    elements = create_conditionals(statement)

    # print("Out analyze_statement():")
    return len(variables_arr), variables_arr, variables_str, elements

