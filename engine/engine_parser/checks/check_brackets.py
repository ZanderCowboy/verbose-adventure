""" Insert """
from components.constants import LEFT_BRACKETS, RIGHT_BRACKETS
from engine_logging.logging_config import logger


class UnequalBracketsExcept(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
    """


def check_left_and_right_brackets(statement):
    """
    This function checks if the number of opening and closing brackets are equal.
    :param statement: the given string statement
    :return: Returns a True if the left and right brackets are equal
    """
    logger.debug("Calling check_left_and_right_brackets(%s)...", statement)

    count = 0
    for _, char in enumerate(statement):
        if char in LEFT_BRACKETS:
            count += 1
        elif char in RIGHT_BRACKETS:
            count -= 1

    if count == 0:
        logger.info("PASS: The number of left and right brackets are equal.")
        return True

    logger.exception(
        "FAIL: Unequal number of left and right brackets. Please check: count=%d",
        count,
    )
    raise UnequalBracketsExcept(
        "Input statement must have an equal number of opening and closing brackets"
    )
