class BankruptException(Exception):
    def __init__(self, *message):
        self.message = message

    def __str__(self):
        return self.message


class DeathException(Exception):
    def __init__(self, *message):
        self.message = message

    def __str__(self):
        return self.message


class DepressionException(Exception):
    def __init__(self, *message):
        self.message = message

    def __str__(self):
        return self.message
