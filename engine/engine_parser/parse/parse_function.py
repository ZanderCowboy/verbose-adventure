""" Insert """
from engine_parser.checks.check_brackets import check_left_and_right_brackets
from components.constants import (
    LEFT_BRACKETS,
    RIGHT_BRACKETS,
    UNARY_CONNECTIVES,
    BINARY_CONNECTIVES,
)
from components.sanitizer import add_brackets_around_unary_connectives
from components.sanitizer import remove_brackets_around_variables
from components.print_details import print_details
from engine_logging.logging_config import logger


def parse_array(elements: list, variables: list):
    """
    This takes an array of elements and variables, completes some sanitizing and
    checks and then calls an internal parse function to complete the parsing.

    :param elements: Array of elements in no particular structure
    :param variables: Variables as found in statement
    :return: Returns an array in a tree-like structure
    """
    logger.info("Starting to parse array...")

    # this removes any brackets around single variables e.g., (P), (R), etc.
    elements_second = remove_brackets_around_variables(elements, variables)
    logger.debug("In parse_array(): elements_second=%s", elements_second)
    elements_second = add_brackets_around_unary_connectives(elements_second, variables)
    logger.debug("In parse_array(): elements_second=%s", elements_second)

    # first checks if brackets are equal
    logger.info("Final checks are ran before parsing concludes.")
    is_parsable = check_left_and_right_brackets(elements_second)
    if is_parsable:
        tree_structured_array = parse(elements_second)
        logger.debug("tree_structured_array=%s", tree_structured_array)
        print_details("PARSE", ("Parsed Array", tree_structured_array))
        logger.info("Finished parsing array.")
        return tree_structured_array

    logger.debug("**** ERROR! **** \n This should not be reached. "
                 "Inspect parse_array in parse_function.py")
    return None


def parse(arr):  # Private Method
    """
    This acts as an internal parse function, taking an array and recursively
    building a tree-like array structure.

    :param arr: Takes a new analyzed statement as an array
    :return: Returns building blocks of elements recursively, forming a tree
    structure
    """
    logger.debug("Calling parse(%s)...", arr)

    # remove outer brackets
    arr = remove_outer_brackets(arr)
    logger.debug("In parse(): arr=%s", arr)

    # parse the binary/unary into left, middle, and right
    temp_arr = []
    if arr[0] in UNARY_CONNECTIVES:
        temp_arr.append(arr[0])
        temp_arr.append(arr[1])
        logger.debug("temp_arr=%s", temp_arr)
        logger.debug("Returning with parsed list of unary connectives.")
        return temp_arr

    middle, position_middle = find_connective(arr)

    # ******************* LEFT ************************
    left = []
    arr_left = arr[:position_middle]
    if len(arr_left) > 1:
        if arr_left[0] in LEFT_BRACKETS:
            left = parse(arr_left)
    elif len(arr_left) == 1:
        left.append(arr_left[0])

    # ******************* RIGHT ***********************
    right = []
    arr_right = arr[position_middle + 1 :]
    if len(arr_right) > 1:
        if arr_right[0] in LEFT_BRACKETS:
            right = parse(arr_right)
    elif len(arr_right) == 1:
        right.append(arr_right[0])

    temp_arr.append(left)
    temp_arr.append(middle)
    temp_arr.append(right)

    logger.debug("temp_array=%s", temp_arr)
    logger.debug("Returning with parsed list for binary connectives.")
    return temp_arr


def remove_outer_brackets(array):  # Private Method
    """
    This removes the outer brackets around an array.
    :param array: An array with redundant outer brackets
    :return: Returns a new array with the outer brackets removed
    """
    logger.debug("Calling remove_outer_brackets(%s)...", array)

    len_of_array = len(array)
    array.pop(0)
    array.pop(len_of_array - 2)

    logger.debug("array=%s", array)
    logger.debug("Finished removing outer brackets.")
    return array


def find_connective(arr):  # Private Method
    """
    Given an array with no outer brackets, this find the connective between
    the left section and the right section. Acts as an internal function.
    For example: (left) conn (right)

    :param arr: Passed array to find connective
    :return: Returns a string with the connective and position in the array
    """
    logger.debug("Calling find_connectives(%s)...", arr)

    count = 0
    in_bracket = False

    for i, elem in enumerate(arr):
        if elem in LEFT_BRACKETS:
            in_bracket = True
            count += 1
        if elem in RIGHT_BRACKETS and in_bracket:
            if count == 1:
                in_bracket = False
            count -= 1
        if elem in BINARY_CONNECTIVES and not in_bracket and count == 0:
            logger.debug("In find_connective(): elem=%s, i=%d", elem, i)
            logger.debug("Found connective.")
            return elem, i

    logger.debug("**** ERROR! **** \n This should not be reached. "
                 "Inspect find_connective in parse_function.py")
    return None
