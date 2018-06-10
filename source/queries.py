PLACEHOLDER = '%s'


UPDATE_MESSAGE = """
    UPDATE clients SET message = %s WHERE id = %s;
"""

UPDATE_PASSWORD = """
    UPDATE clients SET password = %s WHERE id = %s;
"""

ADD_NEW_USER = """
    INSERT INTO clients (username, password) VALUES (%s, %s);
"""

SHOW_INFORMATION = """
    SELECT id, username, balance, message
    FROM clients
    WHERE username = %s AND password = %s
    LIMIT 1;
"""

FIND_ID_BY_USERNAME_AND_PASSWORD = """
    SELECT id
    FROM clients
    WHERE username = %s AND password = %s;
"""

FIND_PASSWORD_BY_USERNAME = """
    SELECT password
    FROM clients
    WHERE username = %s;
"""

ALL = """
    SELECT *
    FROM clients
"""

