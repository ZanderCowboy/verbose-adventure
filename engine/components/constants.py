""" Insert """
# Global Variables
LEFT_BRACKETS = "({["
RIGHT_BRACKETS = ")}]"
BINARY_CONNECTIVES = ['^', 'v', '->', '<->']
UNARY_CONNECTIVES = ['!']

# Constants used in the Computation package
TRUE = 'T'
FALSE = 'F'

# Constants used in the Components package
VALID_BRACKETS = "(){}[]"
VALID_CONNECTIVES = "^v!<->"

WHITE_SPACES = " "

# Constants used in create_conditionals.py
OPEN_ARROW = '<'
DASH = '-'
CLOSE_ARROW = '>'
COND_ELEM = "->"
BICOND_ELEM = "<->"
PRE_CHECK = ['<', '-', '>']


# What are illegal characters
# numbers
# (0 ^ 1)
# (a ^ r)
# (a_1 v a_3)

# Negation:		! ~ ¬(Alt 170)
# Conjunction:	^ & &&
# Disjunction:	v | ||
# Conditional:	-> => →(Alt 26)
# Biconditional:	<-> <=>
