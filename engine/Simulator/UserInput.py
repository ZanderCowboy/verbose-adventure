from Logging.logging_config import logger
from Parser.Parse.AnalizeFunction import analize_statement
from Parser.Parse.ParseFunction import parse_array


def user_input(statement):
    """
    Takes a given statement, analyzes it and returns the elements and variables.
    :returns: (int) number of variables,
                (list) array of variables,
                (str) given statement,
                (list) array of elements from statement
    """
    # todo add console output with table of connectives in formal logic

    logger.debug("Calling user_input(%s)...", statement)
    logger.info("Processing statement: %s", statement)
    # print("Processing Statement: " + statement)

    # todo Edge case, P_1, P_2, P_3, etc
    # todo Create a possible REGEX function?

    number_of_variables, variables_as_array, elements_as_array = analize_statement(statement)

    # todo add section to handles errors if the Verifier fails

    # Combine variables and connectives
    new_elements = parse_array(elements_as_array, variables_as_array)

    logger.info("Gathered all information needed from UserInput: \n number_of_variables=%d, "
                "\n variables_as_array=%s, \n statement=%s, \n new_elements=%s. \n Returning.",
                number_of_variables, variables_as_array, statement, new_elements)
    return number_of_variables, variables_as_array, statement, new_elements
