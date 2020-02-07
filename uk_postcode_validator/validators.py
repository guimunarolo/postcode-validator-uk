import re

from . import constants
from .decorators import validaton_protected_property


class UKPostcode:
    raw_postcode = None
    validated_postcode = None

    def __init__(self, postcode):
        self.raw_postcode = f"{postcode}"

    def __str__(self):
        return f"{self.raw_postcode}"

    @validaton_protected_property
    def outward(self):
        splited_postcode = self.validated_postcode.split(" ")
        if len(splited_postcode) > 1:
            return splited_postcode[0]

        return self.validated_postcode.split("-")[0]

    @validaton_protected_property
    def inward(self):
        splited_postcode = self.validated_postcode.split(" ")
        if len(splited_postcode) > 1:
            return splited_postcode[-1]

        return self.validated_postcode.split("-")[-1]

    @property
    def area(self):
        return re.search(r"^[A-Z]{1,2}", self.outward).group()

    @property
    def district(self):
        try:
            return re.search(r"[0-9]{1,2}[A-Z]?$", self.outward).group()
        except AttributeError:
            return ""

    @property
    def sector(self):
        try:
            return re.search(r"^[0-9]", self.inward).group()
        except AttributeError:
            return ""

    @property
    def unit(self):
        return re.search(r"[A-Z0-9]{2}$", self.inward).group()

    def validate(self):
        postcode = self.raw_postcode.upper()
        validation_regex = re.compile(constants.UK_POSTCODE_VALIDATION_REGEX)
        if not validation_regex.match(postcode):
            return False

        self.validated_postcode = postcode

        return True
