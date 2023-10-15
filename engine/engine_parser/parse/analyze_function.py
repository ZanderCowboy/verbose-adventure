""" Insert """
from components.create_conditionals import create_conditionals
from components.create_elements import create_array_of_elements
from components.find_variables import find_variables
from components.sanitizer import clean_whitespaces
from components.print_details import print_details
from engine_logging.logging_config import logger


def analyze_statement(statement: str):
    """
    Analyzes statement to determine the number of variables, and split into an
    array of elements

    :param statement: string
    :returns: length of array of variables as int, array of variables, string
    of variables, and array with elements
    """
    logger.info("Starting to analyze statement...")

    logger.info("The statement is sanitized from any whitespaces.")
    logger.debug("All whitespaces need to be removed, proceeding.")
    statement = clean_whitespaces(statement)
    logger.debug(
        "Finished removing any whitespaces found in statement. "
        "Proceeding with finding variables."
    )

    # find variables
    variables_arr = find_variables(statement)
    logger.debug("variables_arr=%s", variables_arr)

    # sterilize statement into elements
    logger.info(
        "The statement is converted to an array and any conditionals are sanitized."
    )
    array_of_elements: list = create_array_of_elements(statement)
    array_of_elements = create_conditionals(array_of_elements)

    logger.debug(
        "In analyze_statement(): \nlen(variables_arr)=%d, "
        "\nvariables_arr=%s, \narray_of_elements=%s",
        len(variables_arr),
        variables_arr,
        array_of_elements,
    )
    print_details(
        "ANALYSIS",
        ("Number of Variables", len(variables_arr)),
        ("Variables", variables_arr),
        ("Array of Elements", array_of_elements),
    )
    logger.info("Analyzing concluded.")
    return len(variables_arr), variables_arr, array_of_elements
