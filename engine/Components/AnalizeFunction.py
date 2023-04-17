# Analize statement, extracts all the relevant information and variables

from engine.Components.ParseFunction import parse_statements


# returns
def analize_statement(statement):
    # print("***********************************************************")
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
    elements = create_conditionals(statement)

    # print("Out analyze_statement():")
    return len(variables_arr), variables_arr, variables_str, elements


# find_variables() runs through the statement to determine all the variables
# given in the user statement
# returns an array and string of variables, respectively
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
            if duplicate_int == -1:  # no more occurrences
                if var_str_find >= 0:
                    continue
            if len(variables_arr) == 0 or duplicate is False:
                variables_arr.append(char)
                variables_str += char
            elif duplicate:
                continue

    return variables_arr, variables_str


# creates the conditional -> and biconditional <->
def create_conditionals(statement):
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
        elif char == '-' and biconditional_symbol is False:
            if statement[i + 1] == '>':
                elements.append("->")
                conditional_symbol = True
                continue
        elif char == '>' and conditional_symbol is False:
            continue
        else:
            if conditional_symbol is False and biconditional_symbol is False:
                elements.append(char)
            conditional_symbol = False
            biconditional_symbol = False

    return elements
