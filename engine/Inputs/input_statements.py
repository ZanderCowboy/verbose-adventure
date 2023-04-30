# Contains statement constants

# statement = "(P ^ Q), T v (P -> Q), R ^ (Q v !P) <-> (R ^ Q) v (R ^ P) ^ T, !R ^ P"
# statement = "(P ^ Q)"
statement = "(T v (P -> Q))"
# statement = "(T v (P -> Q)"
# statement = "((R ^ (Q v (!P))) <-> (((R ^ Q) v (R ^ P)) ^ T))"
# statement = "((!R) ^ P)"
# statement = "(P ^ Q)"
# statement = "P v Q"

# check_brackets tests
# test_check_brackets = ['(',')']
# test_check_brackets = ['(','(',')',')']
# test_check_brackets = ['(', '(',')',    '(',')',    ')']
# test_check_brackets = ['(',  '(',')',  '(','(',')','(',')',')', ')']
# test_check_brackets = ['(', '(',')', '(',   '(',')',    ')']  # False