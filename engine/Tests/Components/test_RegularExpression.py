from unittest import TestCase
from RegularExpression import validate_input


class TestValidateInput(TestCase):
	def test_valid_input(self):
		self.assertFalse(validate_input("abc"))
		self.assertTrue(validate_input("A_123"))
		self.assertTrue(validate_input("^"))
		self.assertTrue(validate_input("v"))
		self.assertTrue(validate_input("!"))

	def test_invalid_input(self):
		self.assertFalse(validate_input("ab!c"))
		self.assertFalse(validate_input("123"))
		self.assertTrue(validate_input("<"))
		self.assertTrue(validate_input(">"))
		self.assertTrue(validate_input(" - "))
		self.assertFalse(validate_input("invalid_"))


if __name__ == '__main__':
	TestCase.main()
