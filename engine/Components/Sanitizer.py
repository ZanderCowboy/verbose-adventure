"""_summary_

Returns:
    _type_: _description_
"""
# todo Change connectives to one common set
# todo Change lower case letters to upper case

from engine_logging import logger
from components import LEFT_BRACKETS, RIGHT_BRACKETS, UNARY_CONNECTIVES, BINARY_CONNECTIVES


# for example: change & to ^, | to v


# todo Refactor to sanitize statement
def add_brackets():
    """
    Adds outer brackets to any statement
    :param:
    :return:
    """
    new_string = ""

    return new_string


def clean_whitespaces(statement: str) -> str:
    """
    This clears a statement of all whitespaces that are present.
    :param statement: given statement
    :return: returns a statement with whitespaces removed
    """
    logger.debug("Calling clean_whitespaces(%s)...", statement)

    logger.debug("Finished removing whitespaces: statement=%s", statement.replace(" ", ""))
    return statement.replace(" ", "")


def remove_brackets_around_variables(arr: list, variables: list) -> list:
    """
    This removes brackets around single variables in an array, e.g., (P) => P
    :param arr:
    :param variables: Array of variables from statement.
    :return: Returns an array without brackets around variables.
    """
    logger.debug("Removing brackets around standalone variables...")

    for i in range(0, len(arr) - 2):
        if arr[i] in variables:
            left_of_variable = arr[i - 1]
            right_of_variable = arr[i + 1]
            if left_of_variable in LEFT_BRACKETS and right_of_variable in RIGHT_BRACKETS:
                arr.pop(i - 1)
                arr.pop(i)
    # todo Add another loop to make sure that no 'single brackets' are found

    logger.debug("arr=%s", arr)
    logger.debug("Finished removing all brackets around variables.")
    return arr


def add_brackets_around_unary_connectives(arr: list, variables: list) -> list:
    """
    This adds brackets around unary connectives.
    :param arr:
    :param variables: Array of variables from statement.
    :return: Returns an array with brackets around unary connectives.
    """
    logger.debug("Adding brackets around unary connectives...")
    for i, _ in enumerate(arr):
        # we have a unary connective and unary connective is next to a variable
        if arr[i] in UNARY_CONNECTIVES and arr[i+1] in variables:
            # there is brackets around it
            if arr[i-1] in LEFT_BRACKETS and arr[i+2] in RIGHT_BRACKETS:
                # good case
                continue

            # there is no brackets around it
            if arr[i-1] in BINARY_CONNECTIVES or arr[i+2] in BINARY_CONNECTIVES:
                arr.insert(i, '(')
                arr.insert(i+3, ')')
    # todo Add a final check to makes sure that no unary connectives was missed.

    logger.debug("arr=%s", arr)
    logger.debug("Finished adding brackets around all unary connectives.")
    return arr
