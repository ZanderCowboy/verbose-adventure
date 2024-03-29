""" Insert """
from engine_logging.logging_config import logger


def create_array_of_elements(statement: str) -> list:
    """
    This takes a statement as a string and returns an array of elements
    For example:
    "(P^Q)" => ['(', 'P', '^', 'Q', ')']

    :rtype: list
    :param statement: string
    :return: Returns an array of elements
    """
    logger.debug("Creating an array from a string...")
    logger.debug("Calling create_array_of_elements(%s)", statement)

    array_of_elements = []
    for _, char in enumerate(statement):
        array_of_elements.append(char)

    logger.debug("array_of_elements=%s", array_of_elements)
    logger.debug("Finished creating array.")
    return array_of_elements
