from model.client import Client
from model.exceptions import LessThan8SymbolsError
from model.exceptions import MissingCapitalLetterError
from model.exceptions import MissingNumberError
from model.exceptions import MissingSpecialSymbolError
from model.exceptions import MissingUserError


class ClientController:
    def __init__(self):
        self.user = None

    def get_user(self):
        return self.user

    def register(self, user_name, password):
        try:
            self.user = Client.add_client(user_name, password)
            print("Successful registration.\
                Now you can login with your username and password")
            return True
        except LessThan8SymbolsError:
            print("Your password must be at least 8 letters!")
            return False
        except MissingCapitalLetterError:
            print("Missing capital letter, at least one is required!")
        except MissingSpecialSymbolError:
            print("Missing special symbol, at least one is required!")
        except MissingNumberError:
            print("Missing number, at least one is required!")

    # TODO: needs refactoring
    def login(self, user_name, password):
        try:
            self.user = Client.show_info(user_name, password)
            print("You logged in successfully!")
            self.user.set_id(password)
            return True
        except MissingUserError:
            print("Invalid password or username, please try again!")
            return False

    # TODO: needs refactoring too
    def change_password(self, new_password):
        try:
            self.user.change_password(new_password)
        except LessThan8SymbolsError:
            print("Your password must be at least 8 letters!")
        except MissingCapitalLetterError:
            print("Missing capital letter, at least one is required!")
        except MissingSpecialSymbolError:
            print("Missing special symbol, at least one is required!")
        except MissingNumberError:
            print("Missing number, at least one is required!")

    def change_message(self, new_message):
        try:
            self.user.change_message(new_message)
            print("You change your message successfully!")
        except ValueError:
            print('Unsuccessful')

    def username(self):
        return self.user.get_username()

    def balance(self):
        return self.user.get_balance()

    def message(self):
        return self.user.get_message()

    def exit(self):
        self.user = None
