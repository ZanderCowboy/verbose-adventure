from Parser.Parse.AnalizeFunction import analize_statement
from Parser.Parse.ParseFunction import parse_array


def user_input(statement):
    """
    Takes a given statement, analyzes it and returns the elements and variables.
    :return: returns an integer of the number of variables, an array and string
    of the variables respectively, a statement that is provided and an array
    with the individual elements
    """
    # todo add console output with table of connectives in formal logic

    # statement = input("Please enter the statement(s): ")

    print("Please enter the statement(s): " + statement)

    number_of_variables, variables_arr, elements = analize_statement(statement)

    # todo add section to handles errors if the Verifier fails

    # Combine variables and connectives
    new_elements = parse_array(elements, variables_arr)

    return number_of_variables, variables_arr, statement, new_elements
