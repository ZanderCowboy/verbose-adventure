from Components.Constants import *
from Components.Sanitizer import add_brackets_around_unary_connectives
from Components.Sanitizer import remove_brackets_around_variables
from Logging.logging_config import logger
from Parser.Checks.CheckBrackets import check_left_and_right_brackets


def parse_array(elements: list, variables: list) -> list:
    """

    :param elements:
    :param variables:
    :return:
    """
    logger.debug("Calling parse_array(%s, %s)...", elements, variables)

    # this removes any brackets around single variables e.g., (P), (R), etc.
    elements_second = remove_brackets_around_variables(elements, variables)
    elements_second = add_brackets_around_unary_connectives(elements_second, variables)

    # first checks if brackets are equal
    is_parsable = check_left_and_right_brackets(elements_second)
    if is_parsable:
        return parse(elements_second)


def parse(arr):
    """

    :param arr: takes a new analyzed statement as an array
    :return:  of the parsed statement with individual blocks
    """
    logger.debug("Calling parse(%s)...", arr)

    # remove brackets
    arr = remove_outer_brackets(arr)

    # parse the binary/unary into left, middle, and right
    temp_arr = []
    if arr[0] in UNARY_CONNECTIVES:
        temp_arr.append(arr[0])
        temp_arr.append(arr[1])
        logger.info("Parsed list for unary connectives; temp_arr=%s, returning.", temp_arr)
        return temp_arr

    middle, position_middle = find_connective(arr)

    # left
    left = []
    arr_left = arr[:position_middle]
    if len(arr_left) > 1:
        if arr_left[0] in LEFT_BRACKETS:
            left = parse(arr_left)
    elif len(arr_left) == 1:
        left.append(arr_left[0])

    # right
    right = []
    arr_right = arr[position_middle + 1:]
    if len(arr_right) > 1:
        if arr_right[0] in LEFT_BRACKETS:
            right = parse(arr_right)
    elif len(arr_right) == 1:
        right.append(arr_right[0])

    temp_arr.append(left)
    temp_arr.append(middle)
    temp_arr.append(right)

    logger.info("Parsed list for binary connectives; temp_arr=%s, returning.", temp_arr)
    return temp_arr


def remove_outer_brackets(array):
    """
    removes the outer brackets and returns new array
    :param array:
    :return: returns a new array with the outer brackets removed
    """
    logger.debug("Calling remove_outer_brackets(%s)...", array)

    len_of_array = len(array)
    array.pop(0)
    array.pop(len_of_array - 2)

    logger.info("Removed outer brackets: array=%s, returning", array)
    return array


def find_connective(arr):
    """
    given an array without outer brackets, find the connective between
    left section and right section
    (left) conn (right)
    :param arr:
    :return: returns a string with the connective and position in array
    """
    logger.debug("Calling find_connectives(%s)...", arr)

    temp_string = ''
    count = 0
    in_bracket = False

    for i in range(len(arr)):
        # j = 0
        elem = arr[i]
        if elem in LEFT_BRACKETS:
            in_bracket = True
            count += 1
        if elem in RIGHT_BRACKETS and in_bracket:
            if count == 1:
                in_bracket = False
            count -= 1
        if elem in BINARY_CONNECTIVES and not in_bracket and count == 0:
            return elem, i

    logger.info("Found all connectives: temp_string=%s, returning.", temp_string)
    return temp_string
