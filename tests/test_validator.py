import unittest
import sys
sys.path.append('/home/elitsa/projects/week10/friday/source/model')
sys.path.append('/home/elitsa/projects/week10/friday/source')
sys.path.append('/home/elitsa/projects/week10/friday')
from validator import Validator
from model.exceptions import *


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.correct_password = "@bC7eF6h"
        self.other_correct_password = "abC@72ca"

    def test_error_less_than_eight_symbols(self):
        wrong_password = "bC7eF6h"
        with self.assertRaises(LessThan8SymbolsError):
            Validator.check_password_eight_symbols(wrong_password)

    def test_error_missing_capital_letter(self):
        wrong_password = "@bc7ef6h"
        with self.assertRaises(MissingCapitalLetterError):
            Validator.check_password_capital_letter(wrong_password)

    def test_error_missing_number(self):
        wrong_password = "@Bcdefgh"
        with self.assertRaises(MissingNumberError):
            Validator.check_password_number(wrong_password)

    def test_error_missing_special_symbol(self):
        wrong_password = "1Bcdefgh"
        with self.assertRaises(MissingSpecialSymbolError):
            Validator.check_password_special_symbols(wrong_password)

    def test_error_equal_passwords(self):
        test_password = "@bC7eF6h"
        with self.assertRaises(ValueError):
            Validator.check_equal_passwords(self.correct_password,
                                            test_password)

    def test_correct_password(self):
        self.assertTrue(Validator.check_password(self.correct_password))


if __name__ == "__main__":
    unittest.main()
