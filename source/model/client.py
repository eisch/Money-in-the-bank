from model.client_database import ClientDB
from model.validator import Validator, ClientInfoValidator


class Client():
    def __init__(self, username, balance=0, message=""):
        ClientInfoValidator.check_valid_type(username, str)
        ClientInfoValidator.check_valid_type(balance, float)
        self.__username = username
        self.__balance = balance
        self.__message = message

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_message(self):
        if self.__message:
            return self.__message
        else:
            return "Missing message!"

    def set_message(self, new_message):
        self.__message = new_message

    def set_id(self, password):
        self.__id = self.find_id(self.__username, password)
        return self.__id

    def get_id(self):
        return self.__id

    @classmethod
    def add_client(cls, username, password):
        ClientInfoValidator.check_valid_type(username, str)
        Validator.check_password(password)
        ClientDB.add_user(username, password)
        return cls(username)

    def change_password(self, new_password):
        if Validator.check_password(new_password):
            ClientDB.change_password(self.__id, new_password)

    @classmethod
    def show_info(cls, username, password):
        info = ClientDB.show_info_about_user(username, password)
        ClientInfoValidator.check_user_in_database(info)
        logged_username = info[1]
        logged_balance = info[2]
        logged_message = info[3]
        return cls(logged_username, logged_balance, logged_message)

    def change_message(self, new_message):
        ClientDB.update_message(self.__id, new_message)
        self.__message = new_message

    def __eq__(self, other):
        return self.get_username() == other.get_username()\
            and self.get_balance() == other.get_balance()\
            and self.get_message() == other.get_message()

    def find_id(self, username, password):
        user_id = ClientDB.find_id(username, password)
        return user_id
