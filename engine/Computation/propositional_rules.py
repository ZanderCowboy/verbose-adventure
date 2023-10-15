""" This file is to give the rules to calculate the propositional logic. """
from math import log2
from Components.constants import TRUE, FALSE
from Logging.logging_config import logger


# todo double negation cancel out
# todo 'negation', 'for all', 'there exists' bind most tightly; then disj and
#  conj; then impl. (which is right-associative)

class UnequalArraysExcept(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
    """
    pass


def conjunction(left, right):
    """
    AND
    :param right:
    :param left:
    :return:
    """
    logger.debug("Calling conjunction(%s, %s)...", left, right)

    if len(left) != len(right):  # if they are not equal, raise and skip the rest
        logger.exception("The left '%s' and right '%s' arrays are unequal! Exiting.", left, right)
        raise UnequalArraysExcept("The left and right arrays are unequal. Please investigate.")

    num = int(log2(len(left)))
    new_row_values = []
    for i in range(0, 2 ** num):
        if left[i] == TRUE and right[i] == TRUE:
            new_row_values.append(TRUE)
        else:
            new_row_values.append(FALSE)

    logger.debug("new_row_values=%s", new_row_values)
    logger.debug("Returning with new row values.")
    return new_row_values


def disjunction(left, right):
    """
    OR
    :param right:
    :param left:
    :return:
    """
    logger.debug("Calling disjunction(%s, %s)...", left, right)

    if len(left) != len(right):  # if they are not equal, raise and skip the rest
        logger.exception("The left '%s' and right '%s' arrays are unequal! Exiting.", left, right)
        raise UnequalArraysExcept("The left and right arrays are unequal. Please investigate.")

    num = int(log2(len(left)))
    new_row_values = []
    for i in range(0, 2 ** num):
        if left[i] == FALSE and right[i] == FALSE:
            new_row_values.append(FALSE)
        else:
            new_row_values.append(TRUE)

    logger.debug("new_row_values=%s", new_row_values)
    logger.debug("Returning with new row values.")
    return new_row_values


def negation(left):
    """
    NEGATION
    :param left:
    :return:
    """
    logger.debug("Calling negation(%s)...", left)

    num = int(log2(len(left)))
    new_row_values = []
    for i in range(0, 2 ** num):
        if left[i] == TRUE:
            new_row_values.append(FALSE)
        elif left[i] == FALSE:
            new_row_values.append(TRUE)

    logger.debug("new_row_values=%s", new_row_values)
    logger.debug("Returning with new row values.")
    return new_row_values


def conditional(left, right):
    """
    IMPLICATION
    :param left:
    :param right:
    :return:
    """
    logger.debug("Calling conditional(%s, %s)...", left, right)

    if len(left) != len(right):  # if they are not equal, raise and skip the rest
        logger.exception("The left '%s' and right '%s' arrays are unequal! Exiting.", left, right)
        raise UnequalArraysExcept("The left and right arrays are unequal. Please investigate.")

    num = int(log2(len(left)))
    new_row_values = []
    for i in range(0, 2 ** num):
        if left[i] == TRUE and right[i] == FALSE:
            new_row_values.append(FALSE)
        else:
            new_row_values.append(TRUE)

    logger.debug("new_row_values=%s", new_row_values)
    logger.debug("Returning with new row values.")
    return new_row_values


def biconditional(left, right):
    """
    iff
    :param left:
    :param right:
    :return:
    """
    logger.debug("Calling biconditional(%s, %s)...", left, right)

    if len(left) != len(right):  # if they are not equal, raise and skip the rest
        logger.exception("The left '%s' and right '%s' arrays are unequal! Exiting.", left, right)
        raise UnequalArraysExcept("The left and right arrays are unequal. Please investigate.")

    num = int(log2(len(left)))
    new_row_values = []
    for i in range(0, 2 ** num):
        if left[i] == right[i]:
            new_row_values.append(TRUE)
        else:
            new_row_values.append(FALSE)

    logger.debug("new_row_values=%s", new_row_values)
    logger.debug("Returning with new row values.")
    return new_row_values
