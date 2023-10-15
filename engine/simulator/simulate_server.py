"""
This can be used to simulate the calls that are made by the GRPC Server
"""
from parser.checks import check_brackets, check_for_illegal_characters
from parser.checks.check_brackets import UnequalBracketsExcept
from parser.checks.check_for_illegal_characters import IllegalCharactersException
# from input_statements import statement


# Part 1: Checks for brackets and characters
try:
    statement = []
    if (check_brackets.check_left_and_right_brackets(statement) and
            check_for_illegal_characters.check_for_illegal_characters(statement)):
        pass
except UnequalBracketsExcept as ce:
    print("Unequal Brackets Exception: ", ce)
except IllegalCharactersException as ice:
    print("Illegal Characters Exception: ", ice)
else:
    print("No exception occurred!")


# Main


# Part 2: Parses string


# Part 3: Validates parsed array
