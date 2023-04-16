# Analize statement, extracts all the relevant information and variables

from engine.Components.BuildFunction import build_statements


def analize_statement(statement):
    print("***********************************************************")
    # print("In analize_statement():")
    # print("given statement=" + statement)

    # remove blanks and commas
    statement = statement.replace(" ", "")
    statement = statement.replace(",", "")

    # find variables
    variables_arr, variables_str = find_variables(statement)
    # print("variables=" + str(variables_arr))
    # print("variables_str=" + variables_str)

    # sterilize statement into elements
    elements = sterilize_statement(statement)
    # print("elements=" + str(elements))

    # Combine variables and connectives
    print("\nCalling build_statements():")
    new_elements = build_statements(statement, elements, variables_arr)

    print("Out analize_statement():")
    return len(variables_arr), variables_arr, variables_str, new_elements


# find_variables() runs through the statement to determine all the variables
# given in the user statement
def find_variables(statement):
    variables_arr = []
    variables_str = ""
    len_statement = len(statement)
    for i in range(len(statement)):
        duplicate = False
        char = statement[i]
        if char not in "^v!<->(){}[]":
            # print("Finding Variables \t" + char)
            # Testing for duplicates
            duplicate_int = statement.find(char, i + 1)
            var_str_find = variables_str.find(char)
            if len(variables_arr) > 0 and duplicate_int > 0 and var_str_find >= 0:
                duplicate = True
            # print(duplicate)
            if duplicate_int == -1:  # no more occurences
                if var_str_find >= 0:
                    continue
            if len(variables_arr) == 0 or duplicate == False:
                variables_arr.append(char)
                variables_str += char
            elif duplicate == True:
                continue

    return variables_arr, variables_str


# creates the conditional -> and biconditional <->
def sterilize_statement(statement):
    elements = []
    conditional_symbol = False
    biconditional_symbol = False
    for i in range(len(statement)):
        char = statement[i]
        if char == '<':
            if statement[i + 1] == '-':
                if statement[i + 2] == '>':
                    elements.append("<->")
                    biconditional_symbol = True
            continue
        elif char == '-' and biconditional_symbol == False:
            if statement[i + 1] == '>':
                elements.append("->")
                conditional_symbol = True
                continue
        elif char == '>' and conditional_symbol == False:
            continue
        else:
            if conditional_symbol == False and biconditional_symbol == False:
                elements.append(char)
            conditional_symbol = False
            biconditional_symbol = False

    return elements
