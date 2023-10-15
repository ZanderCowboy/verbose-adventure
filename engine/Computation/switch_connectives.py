from Computation.propositional_rules import *
from Logging.logging_config import logger


def switch_case(case, temp_left, temp_right):
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
    logger.debug("In conj. case...")
    return conjunction(left, right)


def disj(left, right):
    logger.debug("In disj. case...")
    return disjunction(left, right)


# todo Refactor neg() to remove 'right' parameter
def neg(left, right):
    logger.debug("In neg. case...")
    return negation(left)


def cond(left, right):
    logger.debug("In cond. case...")
    return conditional(left, right)


def bicond(left, right):
    logger.debug("In bicond. case...")
    return biconditional(left, right)


def default_case():
    logger.debug("In default case...")
    return "Default case executed."
