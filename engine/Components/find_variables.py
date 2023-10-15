""" Insert """
from Components.constants import VALID_BRACKETS, VALID_CONNECTIVES
from Logging.logging_config import logger


def find_variables(statement: str) -> list:
    """
    Runs through the statement to determine all the variables given in the
    statement.

    :rtype: list
    :param statement: given user statement
    :return: Returns an array variables
    """
    logger.info("Finding variables in statement...")

    # todo Check if all whitespaces are removed. If so, continue o.w. call clean_whitespaces()

    logger.debug("statement=%s", statement)
    variables_array = []
    variables_string = ""
    non_variable_characters = VALID_BRACKETS + VALID_CONNECTIVES
    for i, char in enumerate(statement):
        duplicate = False

        if char not in non_variable_characters:  # if char is not a bracket or a connective
            # Testing for duplicates
            duplicate_int = statement.find(char, i + 1)
            var_str_find = variables_string.find(char)
            if len(variables_array) > 0 and duplicate_int > 0 and var_str_find >= 0:
                duplicate = True
            if duplicate_int == -1:  # no initial or more occurrences
                if var_str_find >= 0:
                    continue
            if len(variables_array) == 0 or duplicate is False:
                variables_array.append(char)
                variables_string += char
            elif duplicate:
                continue

    logger.debug("variables_array=%s", variables_array)
    logger.info("Found all variables in statement.")
    logger.info("*** Variables:\t%s ***", variables_array)
    return variables_array
