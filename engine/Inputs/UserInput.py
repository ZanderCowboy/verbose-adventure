import Inputs.input_statements as instate
from Components.AnalizeFunction import analize_statement


def user_input():
    statement = instate.statement

    print("In user_input():")
    # statement = input("Please enter the statement(s): ")
    print("Please enter the statement(s): P ^ Q, R v (P -> Q), R ^ (Q v P) <-> (R ^ Q) v (R ^ P)")
    # statement = "P ^ Q, R v (P -> Q), R ^ (Q v P) <-> (R ^ Q) v (R ^ P) ^ T"


    # analize statement to determine the number of variables
    # todo move analize_statement() to separate file
    number_of_variables, variables_arr, variables_str, elements = analize_statement(statement)

    print("Out user_input():")
    return number_of_variables, variables_arr, variables_str, statement, elements