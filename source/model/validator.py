from model.exceptions import LessThan8SymbolsError
from model.exceptions import MissingCapitalLetterError
from model.exceptions import MissingNumberError
from model.exceptions import MissingSpecialSymbolError
from model.exceptions import MissingUserError


class Validator:
    @staticmethod
    def check_password_eight_symbols(password):
        if len(password) < 8:
            raise LessThan8SymbolsError()

    @staticmethod
    def check_password_capital_letter(password):
        if not any(symbol.isupper() for symbol in password):
            raise MissingCapitalLetterError()

    @staticmethod
    def check_password_number(password):
        numbers = [str(number) for number in range(0, 10)]
        if not any(symbol in numbers for symbol in password):
            raise MissingNumberError()

    @staticmethod
    def check_password_special_symbols(password):
        special_symbols = ['"', "\\", " "]
        special_symbols += [symbol for symbol in
                            "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"]
        if not any(symbol in special_symbols for symbol in password):
            raise MissingSpecialSymbolError()

    @staticmethod
    def check_password(password):
        Validator.check_password_eight_symbols(password)
        Validator.check_password_capital_letter(password)
        Validator.check_password_number(password)
        Validator.check_password_special_symbols(password)
        return True

    @staticmethod
    def check_equal_passwords(password1, password2):
        if password1 == password2:
            raise ValueError("The new password cannot be the same as the old!")


class ClientInfoValidator:
    @staticmethod
    def check_valid_type(value, value_type):
        if type(value) is not value_type:
            raise TypeError

    @staticmethod
    def check_negative_balance(balance):
        if balance < 0:
            raise ValueError

    @staticmethod
    def check_user_in_database(info_tuple):
        if len(info_tuple) == 0:
            raise MissingUserError()
