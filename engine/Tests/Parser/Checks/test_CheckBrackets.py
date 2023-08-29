from unittest import TestCase
from Parser.Checks.CheckBrackets import check_left_and_right_brackets
from Parser.Checks.CheckBrackets import UnequalBracketsExcept


class TestLeftRightBrackets(TestCase):
	def test_check_left_and_right_brackets_equal(self):
		self.assertTrue(check_left_and_right_brackets("()"))
		self.assertTrue(check_left_and_right_brackets("(())"))
		self.assertTrue(check_left_and_right_brackets("(()())"))
		self.assertTrue(check_left_and_right_brackets("(()(()()))"))
		self.assertTrue(check_left_and_right_brackets("((Q)((R)(T^T)))"))
		self.assertTrue(check_left_and_right_brackets("((AvA)((A_1->T)^(!P)))"))

	def test_check_left_and_right_brackets_unequal(self):
		with self.assertRaises(UnequalBracketsExcept):
			check_left_and_right_brackets("(()(())")
		with self.assertRaises(UnequalBracketsExcept):
			check_left_and_right_brackets("(")
		with self.assertRaises(UnequalBracketsExcept):
			check_left_and_right_brackets(")))()")
