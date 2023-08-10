# Contains statement constants

# statement = "(P ^ Q), T v (P -> Q), R ^ (Q v !P) <-> (R ^ Q) v (R ^ P) ^ T, !R ^ P"
# statement = "(P ^ Q)"  # valid
# statement = "(T v (P ^ Q))"  # valid
# statement = "((T v P) ^ Q)"  # valid
# statement = "(T v (P -> Q))"  # valid
# statement = "(T v (P -> Q)" # invalid
# statement = "((T ^ Q) v (P ^ Q))"  # valid
# statement = "((T ^ T) v (P ^ Q))"  # valid
# statement = "((T ^ T) v ((P ^ (T ^ Q)) ^ Q))"  # valid
# statement = "(S ^ (R ^ Q))"  # valid
# statement = "((R ^ (Q v (!P))) <-> (((R ^ Q) v (R ^ P)) ^ T))"  # valid
# statement = "((R ^ (Q v (P))) <-> (((R ^ Q) v (R ^ P)) ^ T))"  # valid
# statement = "((!R) ^ P)"  # valid
# statement = "(P v Q)"  # valid
# statement = "(!P)"  # valid


# check_brackets tests
# test_check_brackets = ['(',')']
# test_check_brackets = ['(','(',')',')']
# test_check_brackets = ['(', '(',')',    '(',')',    ')']
# test_check_brackets = ['(',  '(',')',  '(','(',')','(',')',')', ')']
# test_check_brackets = ['(', '(',')', '(',   '(',')',    ')']  # False


# Additional test cases
test_cases = [
	"(P <-> (P <-> (P <-> (P <-> P))))",
	"(P ^ Q)",  # valid
	"(T v (P ^ Q))",  # valid
	"((T v P) ^ Q)",  # valid
	"(T v (P -> Q))",  # valid
	"(T v (P -> Q)",  # invalid
	"((T ^ Q) v (P ^ Q))",  # valid
	"((T ^ T) v (P ^ Q))",  # valid
	"((T ^ T) v ((P ^ (T ^ Q)) ^ Q))",  # valid
	"(S ^ (R ^ Q))",  # valid
	"((R ^ (Q v (!P))) <-> (((R ^ Q) v (R ^ P)) ^ T))",  # valid
	"((R ^ (Q v (P))) <-> (((R ^ Q) v (R ^ P)) ^ T))",  # valid
	"((!R) ^ P)",  # valid
	"(P v Q)",  # valid
	"(!P)",  # valid
	"(!(P ^ (Q <-> !Q)))",  # valid

	# Add more test cases here
	# "(P ^ Q ^ R)",  # valid
	# "(P v Q v R)",  # valid
	"(P ^ !Q)",  # valid
	"(P -> (Q ^ R))",  # valid
	"(P -> (Q v R))",  # valid
	"((P ^ Q) v (R ^ S))",  # valid
	"(P <-> Q)",  # valid
	"(!(!P))",  # valid
	"((P v Q) ^ (!R))",  # valid
	"((P -> Q) <-> ((!Q) -> (!P)))",  # valid
]

