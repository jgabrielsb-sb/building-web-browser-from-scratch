class ConversorPortException(Exception):
    def __init__(self, message: str):
        if not isinstance(message, str):
            raise TypeError('message must be a str')

        self.message = message

class RequestPortException(Exception):
    def __init__(self, message: str):
        if not isinstance(message, str):
            raise TypeError('message must be a str')

        self.message = message