import unittest
from pyrus import str_manager as sm


class StringNormaliserTestCase(unittest.TestCase):
    def test_lowercase_conversion(self):
        # Test lowercase conversion
        input_string = "HELLO World"
        expected_output = "hello world"
        self.assertEqual(sm.string_normaliser(input_string), expected_output)

    def test_whitespace_removal(self):
        # Test leading/trailing whitespace removal
        input_string = "  leading and trailing spaces  "
        expected_output = "leading and trailing spaces"
        self.assertEqual(sm.string_normaliser(input_string), expected_output)

    def test_double_space_removal(self):
        # Test double space removal
        input_string = "this  has  double  spaces"
        expected_output = "this has double spaces"
        self.assertEqual(sm.string_normaliser(input_string), expected_output)

    def test_accented_character_replacement(self):
        # Test accented character replacement
        input_string = "Café"
        expected_output = "cafe"
        self.assertEqual(sm.string_normaliser(input_string), expected_output)

    def test_special_character_replacement(self):
        # Test special character replacement
        input_string = "hello!@#$%^&*()"
        expected_output = "hello"
        self.assertEqual(sm.string_normaliser(input_string), expected_output)

    def test_combined_operations(self):
        # Test multiple operations combined
        input_string = "  Café  has  spaces!  "
        expected_output = "cafe has spaces"
        self.assertEqual(sm.string_normaliser(input_string), expected_output)

if __name__ == '__main__':
    unittest.main()
