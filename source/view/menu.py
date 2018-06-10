from controller.client_controller import ClientController
from view.password_handler import PasswordHandler


class Menu:
    @staticmethod
    def input_user():
        username = input("Enter your username: ")
        password = PasswordHandler.password_asterisk("Enter your password: ")
        return(username, password)

    @staticmethod
    def register(reg):
        username, password = Menu.input_user()
        reg.register(username, password)

    @staticmethod
    def login(reg):
        username, password = Menu.input_user()
        reg.login(username, password)

    @staticmethod
    def main_menu():
        reg = ClientController()
        print("Welcome to our bank service.\
         You are not logged in. \nPlease register or login")
        print("Enter 'help' for more information!")
        while True:
            command = input(">>> ")
            if command == 'register':
                Menu.register(reg)
            elif command == 'login':
                Menu.login(reg)
                if reg.get_user():
                    Menu.logged_user(reg)
            elif command == 'help':
                print("login - for logging in!")
                print("register - for creating new account!")
                print("exit - for closing program!")
            elif command == 'exit':
                break
            else:
                print("Invalid command, please try again!")

    @staticmethod
    def logged_user(reg):
        print("Welcome you are logged in as: " + reg.username())
        while True:
            command = input("Logged>> ")
            if command == 'info':
                print("You are: " + reg.username())
                # print("Your id is: " + reg.user.get_id())
                print("Your balance is:" + str(reg.balance()) + '$')

            elif command == 'changepass':
                password = PasswordHandler.password_asterisk()
                reg.change_password(password)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                reg.change_message(new_message)

            elif command == 'show-message':
                print(reg.message())

            elif command == "exit":
                reg.exit()
                print("You log out successfully!")
                break

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")
                print("exit - for logout")

            else:
                print("Invalid command, please try again!")

