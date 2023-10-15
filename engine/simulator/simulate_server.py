"""
This can be used to simulate the calls that are made by the GRPC Server
"""
from engine_parser.checks.check_brackets import (
    check_left_and_right_brackets,
    UnequalBracketsExcept,
)
from engine_parser.checks.check_illegal_characters import (
    check_for_illegal_characters,
    IllegalCharactersException,
)


# Part 1: Checks for brackets and characters
try:
    statement = []
    if check_left_and_right_brackets(statement) and check_for_illegal_characters(
        statement
    ):
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
