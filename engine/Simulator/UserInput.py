from Parser.Parse.ParseFunction import parse_statements
from Simulator.input_statements import statement
from Parser.Parse.AnalizeFunction import analize_statement
from Components.Sanitizer import sanitize_statements


# returns an integer of the number of variables,
# an array and string of the variables respectively,
# a statement that is provided and an array with the individual elements
def user_input():
    """
    Takes a given statement, analyzes it and returns the elements and variables.
    :return: returns an integer of the number of variables, an array and string
    of the variables respectively, a statement that is provided and an array
    with the individual elements
    """
    # todo add console output with table of connectives in formal logic

    # print("In user_input():")
    # statement = input("Please enter the statement(s): ")
    print("Please enter the statement(s): " + statement)

    # analyze statement to determine the number of variables,
    # and split into an array of elements
    number_of_variables, variables_arr, variables_str, elements = analize_statement(statement)

    # add section to sanitize user input
    sanitized_statement = ""
    sanitized_statement = sanitize_statements(statement)


    # add section to verify statement returned from Sanitizer.py



    # add section to handles errors if the Verifier fails




    # Combine variables and connectives
    # print("\nCalling parse_statements():")
    new_elements = parse_statements(statement, elements, variables_arr)

    # print("Out user_input():")
    return number_of_variables, variables_arr, variables_str, statement, new_elements
