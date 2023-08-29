from unittest import TestCase
from Components.FindVariables import find_variables


class TestFindVariables(TestCase):
	def test_find_variables(self):
		self.assertNotIn(" ", "(P^P)")
		self.assertNotIn(" ", "(R^(Q->R))")

		self.assertIn(" ", "(P ^ P)")

		self.assertEqual(find_variables("(P^(P^P))"), ['P'])
		self.assertEqual(find_variables("((T^T)v((P^(T^Q))^Q))"), ['T', 'P', 'Q'])
		self.assertEqual(find_variables("(!(P^(Q<->!Q)))"), ['P', 'Q'])
		self.assertEqual(find_variables("((P^Q)v(R^S))"), ['P', 'Q', 'R', 'S'])

		self.assertEqual(find_variables("P^(R->Q)"), ['P', 'R', 'Q'])
		self.assertEqual(find_variables("Q^R^Q^T"), ['Q', 'R', 'T'])

		self.assertNotEqual(find_variables("((P^Q)v(R^S))"), ['R', 'Q', 'S', 'P'])
		self.assertNotEqual(find_variables("(P^(P^P))"), ['Q'])
