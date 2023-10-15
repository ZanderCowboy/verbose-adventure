""" Insert """
from computation.propositional_rules import (
    conjunction,
    disjunction,
    negation,
    conditional,
    biconditional,
)
from engine_logging.logging_config import logger


def switch_case(case, temp_left, temp_right):
    """_summary_

    Args:
        case (_type_): _description_
        temp_left (_type_): _description_
        temp_right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("Entering switch_case(%s, %s, %s)...", case, temp_left, temp_right)
    switch_dict = {"^": conj, "v": disj, "!": neg, "->": cond, "<->": bicond}
    return switch_dict.get(case, default_case)(temp_left, temp_right)


def conj(left, right):  # Private Method
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In conj. case...")
    return conjunction(left, right)


def disj(left, right):  # Private Method
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In disj. case...")
    return disjunction(left, right)


def neg(left, _):  # Private Method
    """_summary_

    Args:
        left (_type_): _description_
        _ (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In neg. case...")
    return negation(left)


def cond(left, right):  # Private Method
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In cond. case...")
    return conditional(left, right)


def bicond(left, right):  # Private Method
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In bicond. case...")
    return biconditional(left, right)


def default_case():  # Private Method
    """_summary_

    Returns:
        _type_: _description_
    """
    logger.debug("In default case...")
    return "Default case executed."
