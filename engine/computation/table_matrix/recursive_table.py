""" Insert """
from components.constants import TRUE, FALSE
from engine_logging.logging_config import logger


def recursive_table(n):
    """
    Creates a list of T's and F's recursively, given the number of variables
    For example:
    recursive_table(1) => ['T', 'F'] and
    recursive_table(3) =>
    ['TTT', 'TTF', 'TFT', 'TFF', 'FTT', 'FTF', 'FFT', 'FFF']

    :param n: (int) Number of variables
    :return: Returns an array table with T/F values
    """
    logger.debug("Creating table entries recursively...")

    logger.debug("n=%d", n)
    array_table = []
    if n == 1:
        array_table = [TRUE, FALSE]
    elif n != 1:
        array_table = recursive_table(n - 1)
        temp_table = array_table.copy()
        for j in range(0, int(2 ** n / 2)):
            if j % 2 == 0:  # even
                array_table.insert(j * 2, temp_table[j])
            elif j % 2 == 1:  # odd
                array_table.insert(j * 2, temp_table[j])

    if n > 1:
        for i in range(0, 2 ** n):
            if i % 2 == 0:  # even
                array_table[i] = str(array_table[i]) + TRUE
            elif i % 2 == 1:  # odd
                array_table[i] = str(array_table[i]) + FALSE

    logger.debug("array_table=%s", array_table)
    logger.debug("Finished creating array of table entries.")
    return array_table
