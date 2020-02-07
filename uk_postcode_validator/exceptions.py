class PostcodeNotValidated(Exception):
    def __init__(self, message=None):
        super().__init__("This postcode is not validated")
