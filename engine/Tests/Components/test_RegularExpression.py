from unittest import TestCase
from Components.RegularExpression import validate_input


class TestValidateInput(TestCase):
	def test_valid_input(self):
		self.assertTrue(validate_input("A_123"))
		self.assertTrue(validate_input("^"))
		self.assertTrue(validate_input("v"))
		self.assertTrue(validate_input("!"))
		self.assertTrue(validate_input("<"))
		self.assertTrue(validate_input(">"))
		self.assertTrue(validate_input(" - "))
		self.assertTrue(validate_input("P"))
		self.assertTrue(validate_input("P_1"))
		self.assertTrue(validate_input("P_2"))
		self.assertTrue(validate_input("a"))

	def test_invalid_input(self):
		self.assertFalse(validate_input("ab!c"))
		self.assertFalse(validate_input("123"))
		self.assertFalse(validate_input("@"))
		self.assertFalse(validate_input("#"))
		self.assertFalse(validate_input("%"))
		self.assertFalse(validate_input("C_"))
		self.assertFalse(validate_input("invalid_"))
		self.assertFalse(validate_input("abc"))
		self.assertFalse(validate_input("X-Y"))
		self.assertFalse(validate_input("R-5"))
		self.assertFalse(validate_input("S^6"))
		self.assertFalse(validate_input("0"))
		self.assertFalse(validate_input("5"))
		self.assertFalse(validate_input("_xyz"))
		self.assertFalse(validate_input("def_"))
		self.assertFalse(validate_input("P@Q"))


if __name__ == '__main__':
	TestCase.main()
