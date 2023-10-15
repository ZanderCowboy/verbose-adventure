# Test cases that is used in simulate_main.py
test_cases = [
	# "(P <-> (P <-> (P <-> (P <-> P))))",
	# "(P ^ Q)",  # valid
	"(T v (P ^ Q))",  # valid
	# "((T v P) ^ Q)",  # valid
	# "(T v (P -> Q))",  # valid
	# "(T v (P -> Q)",  # invalid
	# "((T ^ Q) v (P ^ Q))",  # valid
	# "((T ^ T) v (P ^ Q))",  # valid
	# "((T ^ T) v ((P ^ (T ^ Q)) ^ Q))",  # valid
	# "(S ^ (R ^ Q))",  # valid
	# "((R ^ (Q v (!P))) <-> (((R ^ Q) v (R ^ P)) ^ T))",  # valid
	# "((R ^ (Q v (P))) <-> (((R ^ Q) v (R ^ P)) ^ T))",  # valid

	# "R ^ (Q v !P) <-> (R ^ Q) v (R ^ P) ^ T"  # valid, but binding rules
	# should be applied.
	# "((!R) ^ P)",  # valid
	# "(P v Q)",  # valid
	# "(!P)",  # valid
	# "(!(P ^ (Q <-> !Q)))",  # valid

	# Add more test cases here
	# "(P ^ Q ^ R)",  # valid
	# "(P v Q v R)",  # valid
	# "(P ^ !Q)",  # valid
	# "(P -> (Q ^ R))",  # valid
	# "(P -> (Q v R))",  # valid
	# "((P ^ Q) v (R ^ S))",  # valid
	# "(P <-> Q)",  # valid
	# "(!(!P))",  # valid

	# ERROR checking!!!
	# "((P v Q) ^ (!R))",  # valid
	# "((P -> Q) <-> ((!Q) -> (!P)))",  # valid

	# Edge cases
	# "(P_1 ^ P_2)",
	# "(Q ^ (R_20 -> T_2))"
]
