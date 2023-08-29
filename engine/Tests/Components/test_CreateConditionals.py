from unittest import TestCase
from Components.CreateConditionals import create_conditionals


class TestCreateConditionals(TestCase):
	def test_containing_no_conditionals(self):
		self.assertEqual(create_conditionals(['(', 'T', 'v', '(', 'P', '^', 'Q', ')', ')']),
						 ['(', 'T', 'v', '(', 'P', '^', 'Q', ')', ')'])
		self.assertEqual(create_conditionals(['(', '(', 'T', '^', 'Q', ')', 'v', '(', 'P', '^', 'Q', ')', ')']),
						 ['(', '(', 'T', '^', 'Q', ')', 'v', '(', 'P', '^', 'Q', ')', ')'])
		self.assertEqual(create_conditionals(['(', 'P', 'v', 'Q', ')']),
						 ['(', 'P', 'v', 'Q', ')'])
		self.assertEqual(create_conditionals(['P', '^', 'Q']), ['P', '^', 'Q'])

	def test_create_conditionals(self):
		self.assertEqual(create_conditionals(['(', 'T', 'v', '(', 'P', '-', '>', 'Q', ')', ')']),
						 ['(', 'T', 'v', '(', 'P', '->', 'Q', ')', ')'])
		self.assertEqual(create_conditionals(['(', 'P', '-', '>', '(', 'Q', '^', 'R', ')', ')']),
						 ['(', 'P', '->', '(', 'Q', '^', 'R', ')', ')'])
		self.assertEqual(create_conditionals(['(', '(', 'P', '-', '>', 'Q', ')', '<', '-', '>', '(', '(', '!', 'Q', ')', '-', '>', '(', '!', 'P', ')', ')', ')']),
						 ['(', '(', 'P', '->', 'Q', ')', '<->', '(', '(', '!', 'Q', ')', '->', '(', '!', 'P', ')', ')', ')'])
		self.assertEqual(create_conditionals(['P', '<', '-', '>', 'Q']), ['P', '<->', 'Q'])

	# def test_unsuccessful_create_conditionals(self):
	# 	self.assertEqual(create_conditionals(['P', '<', '-', 'Q']), ['P', '<->', 'Q'])
	# 	self.assertEqual(create_conditionals(['P', '-', 'Q']), ['P', '<->', 'Q'])

