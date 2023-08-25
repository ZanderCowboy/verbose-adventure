from Components.CreateConditionals import create_conditionals
from Components.CreateElements import create_array_of_elements
from Components.FindVariables import find_variables
# from Components.Sanitizer import clean_commas
from Components.Sanitizer import clean_whitespaces
from Logging.logging_config import logger


def analize_statement(statement: str) -> [int, list, list]:
    """
    Analyzes statement to determine the number of variables, and split into an array of elements
    :param statement: string
    :returns: length of array of variables as int, array of variables, string of variables, and array with elements
    """
    logger.info("Starting to analize statement...")

    statement = clean_whitespaces(statement)
    # statement = clean_commas(statement)

    # find variables
    variables_arr = find_variables(statement)
    logger.debug("variables_arr=%s", variables_arr)

    # sterilize statement into elements
    array_of_elements: list = create_array_of_elements(statement)
    array_of_elements = create_conditionals(array_of_elements)

    logger.debug("len(variables_arr)=%d, variables_arr=%s, array_of_elements=%s", len(variables_arr), variables_arr, array_of_elements)
    logger.info("Analyzing concluded.")
    return len(variables_arr), variables_arr, array_of_elements
