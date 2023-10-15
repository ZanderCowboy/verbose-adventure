""" Insert """
from parser.parse.analyze_function import analyze_statement
from parser.parse.parse_function import parse_array
from engine_logging.logging_config import logger


def user_input(statement: str):
    """
    Takes a given statement, analyzes it and returns the elements and variables.
    :returns: (int) number of variables,
                (list) array of variables,
                (str) given statement,
                (list) array of elements from statement
    """
    # todo Add console output with table of connectives in formal logic
    logger.info("Processing statement...")
    logger.debug("statement=%s", statement)

    # todo Edge case, P_1, P_2, P_3, etc.
    #  For this, would it be wise to use brackets around variables? Create ISSUE.
    # todo Create a possible REGEX function?

    number_of_variables, variables_as_array, elements_as_array = analyze_statement(
        statement
    )

    # Combine variables and connectives
    new_elements = parse_array(elements_as_array, variables_as_array)

    logger.debug(
        "In user_input(): \nnumber_of_variables=%d, \nvariables_as_array=%s, \nstatement=%s, "
        "\nnew_elements=%s.",
        number_of_variables,
        variables_as_array,
        statement,
        new_elements,
    )
    logger.info("Gathered all information needed including variables and parsed array.")
    return number_of_variables, variables_as_array, statement, new_elements
