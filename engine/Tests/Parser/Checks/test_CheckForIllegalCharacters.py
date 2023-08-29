from unittest import TestCase
from unittest.mock import patch
from Parser.Checks.CheckForIllegalCharacters import check_for_illegal_characters
from Parser.Checks.CheckForIllegalCharacters import IllegalCharactersException
from Components.RegularExpression import validate_input
from Components.Constants import *


class TestIllegalCharacters(TestCase):
	@patch('Components.RegularExpression.validate_input')
	def test_check_for_legal_characters(self, mock_validate_input):
		# left brackets
		self.assertIn("(", LEFT_BRACKETS)
		self.assertIn("{", LEFT_BRACKETS)
		self.assertIn("[", LEFT_BRACKETS)
		# right brackets
		self.assertIn(")", RIGHT_BRACKETS)
		self.assertIn("}", RIGHT_BRACKETS)
		self.assertIn("]", RIGHT_BRACKETS)
		# white spaces
		self.assertIn(" ", WHITE_SPACES)

		# mock validate input
		mock_validate_input.return_value = True
		result = check_for_illegal_characters("((!P) -> (R v ((Q_2) ^ (Q_4))))")
		mock_validate_input.assert_called_once_with("((!P) -> (R v ((Q_2) ^ (Q_4))))")
		self.assertEqual(result, True)

	@patch('Components.RegularExpression.validate_input')
	def test_check_for_illegal_characters(self, mock_validate_input):
		with self.assertRaises(IllegalCharactersException):
			mock_validate_input.return_value = False
			result = check_for_illegal_characters("@#$%")
			mock_validate_input.assert_called_once_with("@#$%")
			self.assertEqual(result, False)
