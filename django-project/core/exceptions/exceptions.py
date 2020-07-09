class NonNumericalException(Exception):

    def __init__(self, message="Enter a numerical value for ID"):
        self.message = message
        super().__init__(self.message)


class NonValidID(Exception):

    def __init__(self, message="Enter a valid ID"):
        self.message = message
        super().__init__(self.message)
