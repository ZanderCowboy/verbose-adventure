""" Insert """
from computation.propositional_rules import *
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
    switch_dict = {
        '^': conj,
        'v': disj,
        '!': neg,
        '->': cond,
        '<->': bicond
    }
    return switch_dict.get(case, default_case)(temp_left, temp_right)


def conj(left, right):
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In conj. case...")
    return conjunction(left, right)


def disj(left, right):
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In disj. case...")
    return disjunction(left, right)


# todo Refactor neg() to remove 'right' parameter
def neg(left, _):
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In neg. case...")
    return negation(left)


def cond(left, right):
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In cond. case...")
    return conditional(left, right)


def bicond(left, right):
    """_summary_

    Args:
        left (_type_): _description_
        right (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("In bicond. case...")
    return biconditional(left, right)


def default_case():
    """_summary_

    Returns:
        _type_: _description_
    """
    logger.debug("In default case...")
    return "Default case executed."
