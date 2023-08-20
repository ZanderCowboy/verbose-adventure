from Computation.PropositionalRules import *


def switch_case(case, temp_left, temp_right):
	switch_dict = {
		'^': conj,
		'v': disj,
		'!': neg,
		'->': cond,
		'<->': bicond
	}
	return switch_dict.get(case, default_case)(temp_left, temp_right)


def conj(left, right):
	# print("in conjunction")
	return conjunction(left, right)


def disj(left, right):
	# print("in disjunction")
	return disjunction(left, right)


# todo Refactor neg() to remove 'right' parameter
def neg(left, right):
	# print("in negation")
	return negation(left)


def cond(left, right):
	# print("in conditional")
	return conditional(left, right)


def bicond(left, right):
	# print("in biconditional")
	return biconditional(left, right)


def default_case():
	return "Default case executed."

