import queries
import hashlib
from create_database import conn, cursor
import uuid


class ClientDB:
    @staticmethod
    def hash_password(password):
        salt = uuid.uuid4().hex
        return (hashlib.sha256(salt.encode() +
                password.encode()).hexdigest() + ':' + salt)

    @staticmethod
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        # print("password=", password)
        # print("salt=", salt)
        return (password == hashlib.sha256(salt.encode() +
                user_password.encode()).hexdigest())

    @staticmethod
    def add_user(username, password):
        hash_password = ClientDB.hash_password(password)
        cursor.execute(queries.ADD_NEW_USER, (username, str(hash_password)))
        conn.commit()

    @staticmethod
    def change_password(id, new_password):
        new_hash_password = ClientDB.hash_password(new_password)
        cursor.execute(queries.UPDATE_PASSWORD, (str(new_hash_password), id))
        conn.commit()

    @staticmethod
    def find_id(username, password):
        hash_password = ClientDB.find_password(username)
        result = cursor.execute(queries.FIND_ID_BY_USERNAME_AND_PASSWORD,
                                (username, hash_password))
        row = cursor.fetchone()
        return row[0]

    @staticmethod
    def show_info_about_user(username, password):
        hashed_password = ClientDB.find_password(username)
        if hashed_password:
            # print(len(username))
            # print("hashed_password = ", hashed_password)
            if ClientDB.check_password(hashed_password, password):
                cursor.execute(queries.SHOW_INFORMATION,
                               (username, hashed_password))
                row = cursor.fetchone()
                return row
        return ()

    @staticmethod
    def update_message(user_id, new_message):
        cursor.execute(queries.UPDATE_MESSAGE, (new_message, user_id))
        conn.commit()

    @staticmethod
    def find_password(username):
        cursor.execute(queries.FIND_PASSWORD_BY_USERNAME, (username,))
        r = cursor.fetchone()
        if r:
            return r[0]
        else:
            return None
