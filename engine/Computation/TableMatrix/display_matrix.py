from Logging.logging_config import logger


def display_matrix(number_of_variables: int, returned_matrix: list, all_variables: list) -> None:
    logger.debug("Displaying matrix to console...")

    auxiliary_variables = []  # Holds all the placeholder variables
    for i in range(number_of_variables, len(all_variables) - 1):
        auxiliary_variables.append(all_variables[i])
    number_of_aux_variables = len(auxiliary_variables)

    # prints part for variables
    print("| ", end='')
    for j in range(number_of_variables):
        if j != number_of_variables-1:
            print(all_variables[j] + " | ", end='')
        else:
            print(all_variables[j] + " || ", end='')

    # prints auxiliary variables
    index_between_auxiliary_variables_and_last = number_of_variables + len(auxiliary_variables)
    for j in range(number_of_variables, index_between_auxiliary_variables_and_last):
        if j != index_between_auxiliary_variables_and_last - 1:
            print(all_variables[j] + " | ", end='')
        else:
            print(all_variables[j] + " || ", end='')

    # prints last column
    print(all_variables[-1] + " || ", end='')

    print('\n', end='')

    count_characters = get_number_of_spaces(number_of_variables, number_of_aux_variables, all_variables)
    print("=" * count_characters)

    # prints the T/F values for each row in matrix
    for i in range(len(returned_matrix)):
        row = returned_matrix[i]

        print("| ", end='')

        # prints part for variables
        for j in range(number_of_variables):
            if j != number_of_variables-1:
                print(row[j] + " | ", end='')
            else:
                print(row[j] + " || ", end='')

        # prints auxiliary variables
        index_between_auxiliary_variables_and_last = number_of_variables + len(auxiliary_variables)
        for j in range(number_of_variables, index_between_auxiliary_variables_and_last):
            if j != index_between_auxiliary_variables_and_last - 1:
                print(row[j] + " | ", end='')
            else:
                temp_length = len(all_variables[j])
                add_len = 0
                if temp_length % 2 == 1:  # odd
                    add_len = temp_length/2 + 1
                add_space = ''
                for k in range(int(add_len)):
                    add_space += ' '
                print(row[j] + add_space + " || ", end='')

        # prints last column
        temp_length = len(all_variables[-1])
        add_len = 0
        if temp_length % 2 == 1:  # odd
            add_len = temp_length/2 + 1
        elif temp_length % 2 == 0:  # even
            add_len = temp_length/2
        add_space = ''
        for k in range(int(add_len)):
            add_space += ' '
        print(row[-1] + add_space + " || ", end='')
        print('\n', end='')

    print("=" * count_characters)


# todo Finish Function
def get_number_of_spaces(number_of_variables: int, nr_auxiliary_variables: int, all_variables: list) -> int:
    logger.debug("Calling get_number_of_spaces(%d, %d, %s)...", number_of_variables, nr_auxiliary_variables, all_variables)

    space = 3
    total_space = 0

    initial_space = 1
    total_space += initial_space
    spaces_for_variables = space * number_of_variables
    total_space += spaces_for_variables
    spaces_for_single_sep = number_of_variables - 1
    total_space += spaces_for_single_sep

    length_of_aux_strings = 0
    for i in range(number_of_variables, len(all_variables) - 1):
        temp_length = len(all_variables[i])
        length_of_aux_strings += temp_length
    length_of_aux_strings += nr_auxiliary_variables * 2
    spaces_for_aux_variables = length_of_aux_strings
    total_space += spaces_for_aux_variables
    spaces_for_single_sep = nr_auxiliary_variables - 1
    total_space += spaces_for_single_sep

    space_for_last_variable = len(all_variables[-1])
    total_space += space_for_last_variable
    spaces_for_double_sep = 6
    total_space += spaces_for_double_sep

    logger.debug("total_space=%d", total_space)
    logger.debug("Finished calculating the total space.")
    return total_space
