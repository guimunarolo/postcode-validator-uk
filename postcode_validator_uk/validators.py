import re

from .constants import (
    UK_POSTCODE_AREA_REGEX,
    UK_POSTCODE_DISTRICT_REGEX,
    UK_POSTCODE_SECTOR_REGEX,
    UK_POSTCODE_UNIT_REGEX,
    UK_POSTCODE_VALIDATION_REGEX,
)
from .decorators import validaton_protected_property
from .exceptions import InvalidPostcode


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
        return re.search(UK_POSTCODE_AREA_REGEX, self.outward).group()

    @property
    def district(self):
        try:
            return re.search(UK_POSTCODE_DISTRICT_REGEX, self.outward).group()
        except AttributeError:
            return ""

    @property
    def sector(self):
        try:
            return re.search(UK_POSTCODE_SECTOR_REGEX, self.inward).group()
        except AttributeError:
            return ""

    @property
    def unit(self):
        return re.search(UK_POSTCODE_UNIT_REGEX, self.inward).group()

    def validate(self):
        postcode = self.raw_postcode.upper()
        if not UK_POSTCODE_VALIDATION_REGEX.match(postcode):
            raise InvalidPostcode

        self.validated_postcode = postcode
