import unittest
from pyrus import str_manager as sm

class StringNormaliserTests(unittest.TestCase):

    def subtester(self, test_values):
        
        for value, expected_result in test_values:
            with self.subTest(value=value):
                result = sm.string_normaliser(value)
                self.assertEqual(result, expected_result)
    
    def test_case_normalisation(self):
        test_values = [
            ("Hello World!", "hello world!"),
            ("ThIs Is A MiXeD CaSe StRiNg", "this is a mixed case string"),
            ("Áccéntéd Cháráctérs", "áccéntéd cháráctérs"),
            ("ALL UPPERCASE", "all uppercase"),
            ("", ""),  # Empty string should remain the same
        ]
    
        self.subtester(test_values)

    def test_whitespace_normalisation(self):
        test_values = [
            ("   Remove  extra  spaces   ", "Remove extra spaces"),
            ("  Leading and trailing spaces  ", "Leading and trailing spaces"),
            ("    ", ""),  # All whitespace, expect empty string
            ("", "")
        ]
        
        self.subtester(test_values)

    def test_double_space_normalisation(self):
        test_values = [
            ("This  has  double  spaces", "This has double spaces"),
            ("No  double  spaces", "No double spaces"),
            ("Single spaces", "Single spaces"),
            ("", ""),  # Empty string should remain the same
        ]
        
        self.subtester(test_values)

    def test_encoding_normalisation(self):
        test_values = [
            ("Thís Štríng Hás Áccénted Characters", "Thís Štríng Hás Áccénted Characters"),
            ("Ünicöde Äscii Êncoding", "Ünicöde Äscii Êncoding"),
            ("Keep 1234567890 digits", "Keep 1234567890 digits"),
            ("", ""),  # Empty string should remain the same
        ]
        
        self.subtester(test_values)

    def test_special_char_normalisation(self):
        test_values = [
            ("Hello@# World!", "Hello@# World"),
            ("Remove !@#$ special %^&* characters", "Remove special characters"),
            ("Keep digits 1234567890", "Keep digits 1234567890"),
            ("", ""),  # Empty string should remain the same
        ]
        
        self.subtester(test_values)

    def test_combined_normaisation(self):
        test_values = [
            # Normal test values
            ("Hello World!", "hello world"),
            ("   Remove  extra  spaces   ", "remove extra spaces"),
            ("Thís Štríng Hás Áccénted Characters", "thís Štríng hás áccénted characters"),
            ("Ünicöde Äscii Êncoding", "ünicöde äscii êncoding"),
            ("Hello@# World!", "hello world"),
            ("Remove !@#$ special %^&* characters", "remove special characters"),
            ("Keep digits 1234567890", "keep digits 1234567890"),

            # Extreme test values
            ("    ", ""),  # All whitespace, expect empty string
            ("!@#$%^&*()_+", ""),  # All special characters, expect empty string
            ("ÁČÇÈÑTÉÐ ßÞÉÇÏÀL ÇHÁRÁÇTÉRS", "áčçèñtéd ßþéçïàl çháráçtérs"),
            ("ÛÑÎÇØÐÊ ÄŠÇÏÏ ÊÑÇØÐÏÑG", "ûñîçøðê äšçïï êñçøðïñg"),
            ("     ÛÑÎÇØÐÊ   ", "ûñîçøðê"),  # Leading/trailing whitespace with accented characters
            ("\n    ÛÑÎÇØÐÊ     ÄŠÇÏÏ     ÊÑÇØÐÏÑG    ", "ûñîçøðê äšçïï êñçøðïñg"),  # Multiple operations with accented characters and whitespace
        ]
        
        self.subtester(test_values)


if __name__ == '__main__':
    unittest.main()
