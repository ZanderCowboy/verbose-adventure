"""_summary_
"""
from engine_logging.logging_config import logger


def print_details(name: str, *args):
    """
    This is a generalized print function for logs. It takes a section name
    followed by (name,value) tuples. For example,

    print_details("TEST", ("some_name", some_value)) where 'some_value' can be
    passed.

    :param name: Required: A name for the details section, CAPITALIZED.
    :param args: Optional: Any number of parameters as tuples that can be
    printed
    :return:
    """
    logger.debug("Printing details...")

    max_length = 60
    len_name = len(name)
    amount_stars = max_length - len_name
    star_line = "*" * int(amount_stars/2) + " " + name.upper() + " " + "*" * int(amount_stars/2)

    logger.info(star_line)
    for arg_name, arg_value in args:
        logger.info("-> %s: \t%s", arg_name, arg_value)
    logger.info(star_line)
