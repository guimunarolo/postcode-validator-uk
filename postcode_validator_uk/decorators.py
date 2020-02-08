from .exceptions import PostcodeNotValidated


def validaton_protected_property(f):
    @property
    def wrapper(self, *args, **kwargs):
        if self.validated_postcode is None:
            raise PostcodeNotValidated

        return f(self, *args, **kwargs)

    return wrapper
