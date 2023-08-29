from unittest import TestCase
from Parser.Checks.CheckConditionals import check_conditionals
from Parser.Checks.CheckConditionals import InvalidConditionalSymbolsExcept


class TestCheckConditionals(TestCase):
	def test_check_conditionals_pass(self):
		self.assertTrue(check_conditionals(['(', 'T', 'v', '(', 'P', '-', '>', 'Q', ')', ')'], ['T', 'P', 'Q']))
		self.assertTrue(check_conditionals(['(', '(', 'T', '^', 'Q', ')', 'v', '(', 'P', '^', 'Q', ')', ')'], ['T', 'Q', 'P']))
		self.assertTrue(check_conditionals(['(', 'S', '^', '(', 'R', '^', 'Q', ')', ')'], ['S', 'R', 'Q']))
		self.assertTrue(check_conditionals(['(', 'P', 'v', 'Q', ')'], ['P', 'Q']))
		self.assertTrue(check_conditionals(['(', 'P', '-', '>', '(', 'Q', '^', 'R', ')', ')'], ['P', 'Q', 'R']))
		self.assertTrue(check_conditionals(['(', '(', 'P', '-', '>', 'Q', ')', '<', '-', '>', '(', '(', '!', 'Q', ')', '-', '>', '(', '!', 'P', ')', ')', ')'], ['P', 'Q']))

	def test_check_conditionals_fail(self):
		with self.assertRaises(InvalidConditionalSymbolsExcept):
			check_conditionals(['(', 'T', 'v', '(', 'P', '<', 'Q', ')', ')'], ['T', 'P', 'Q'])
		with self.assertRaises(InvalidConditionalSymbolsExcept):
			check_conditionals(['(', 'T', 'v', '(', 'P', '-', 'Q', ')', ')'], ['T', 'P', 'Q'])
		with self.assertRaises(InvalidConditionalSymbolsExcept):
			check_conditionals(['(', 'T', 'v', '(', 'P', '>', 'Q', ')', ')'], ['T', 'P', 'Q'])
		with self.assertRaises(InvalidConditionalSymbolsExcept):
			check_conditionals(['(', 'T', 'v', '(', 'P', '<', '-', 'Q', ')', ')'], ['T', 'P', 'Q'])
		with self.assertRaises(InvalidConditionalSymbolsExcept):
			check_conditionals(['(', 'T', 'v', '(', 'P', '<', '-', '>', '-', 'Q', ')', ')'], ['T', 'P', 'Q'])
		with self.assertRaises(InvalidConditionalSymbolsExcept):
			check_conditionals(['(', 'T', 'v', '(', 'P', '>', '-', '<', 'Q', ')', ')'], ['T', 'P', 'Q'])
		with self.assertRaises(InvalidConditionalSymbolsExcept):
			check_conditionals(['(', 'T', 'v', '(', 'P', '>', '<', 'Q', ')', ')'], ['T', 'P', 'Q'])
		with self.assertRaises(InvalidConditionalSymbolsExcept):
			check_conditionals(['(', 'T', 'v', '(', 'P', '-', '-', 'Q', ')', ')'], ['T', 'P', 'Q'])
