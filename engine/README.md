# verbose-adventure Engine

This is a Python gRPC server that will calculate the final truth column that 
will be sent back

## Propositional Logic Calculator

Random Repository

Propositional Logic Calculator.

## Description
Use LogicCalculator to do all the relevant checks and calculations


# GRPCServer Package
To follow
This package is responsible for communicating with the GRPC client on the backend
side but also calling the necessary packages.

### Calling sequence for the packages with a perfect flow.


# SIMULATOR Package
This is responsible for simulating the input that is sent from the Backend. This
includes the User Input and input statements.


# PARSER Package
## Check Errors
- Checking for invalid characters such as @, etc.
- Checking for unequal number of opening and closing brackets.

This takes a string and runs through it to determine if there are any illegal
characters and also checks that the number of opening and closing brackets
are equal. 

- If the string is successful, it is sent to the next section that will do the 
parsing, turning it from a string into an array.
- If not, an appropriate error message is send back to the GRPC Server to handle.

## Parse String
### String to Simple Array

### Processing Connectives in Array

### Restructuring Array into Tree Structured Array


## Validation
### Processing Connectives

### Processing Brackets


# VALIDATOR Package
## Logic Rules

## Connectives


# COMPUTATION Package
## Propositional Rules

##

# Flow
Start with the GRPCServer

- First checks as pre-flight
- GRPCServer Checks => checks
- If good, proceed:
- GRPCServer Parser => checks, parse, validate
- If good, proceed:
- GRPCServer Compute => compute