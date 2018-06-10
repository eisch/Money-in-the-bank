from getch import getch
import sys


class PasswordHandler:
    @staticmethod
    def password_asterisk(prompt='Password: '):
        password = ""
        sys.stdout.write(prompt)
        sys.stdout.flush()
        while True:
            key = ord(getch())
            if key == 13:  # Return Key
                sys.stdout.write('\n')
                return password
            elif key == 127:  # Backspace key
                if len(password) > 0:
                    # Erases previous character.
                    sys.stdout.write('\b' + ' ' + '\b')
                    sys.stdout.flush()
                    password = password[:-1]
            else:
                # Masks user input.
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()
                password += char
