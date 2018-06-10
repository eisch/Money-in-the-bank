class LessThan8SymbolsError(Exception):
    def __init__(self):
        Exception.__init__(self, "Your password must be at least 8 letters!")


class MissingCapitalLetterError(Exception):
    def __init__(self):
        Exception.__init__(self, "Missing capital letter, at least one is required!")


class MissingNumberError(Exception):
    def __init__(self):
        Exception.__init__(self, "Missing number, at least one is required!")


class MissingSpecialSymbolError(Exception):
    def __init__(self):
        Exception.__init__(self, "Missing special symbol, at least one is required!")


class MissingUserError(Exception):
    def __init__(self):
        Exception.__init__(self, "There's no such user in database!")
