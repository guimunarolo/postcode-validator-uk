import re

from .constants import (
    UK_POSTCODE_AREA_REGEX,
    UK_POSTCODE_DISTRICT_REGEX,
    UK_POSTCODE_RULES_LIST,
    UK_POSTCODE_SECTOR_REGEX,
    UK_POSTCODE_UNIT_REGEX,
    UK_POSTCODE_VALIDATION_REGEX,
)
from .exceptions import InvalidPostcode, PostcodeNotValidated


class UKPostcode:
    raw_postcode = None
    validated_postcode = None
    _outward = None
    _inward = None
    _rules_list = UK_POSTCODE_RULES_LIST

    def __init__(self, postcode):
        self.raw_postcode = f"{postcode}"

    def __str__(self):
        return f"{self.raw_postcode}"

    @property
    def outward(self):
        if self._outward is None:
            raise PostcodeNotValidated

        return self._outward

    @property
    def inward(self):
        if self._inward is None:
            raise PostcodeNotValidated

        return self._inward

    @property
    def area(self):
        return re.search(UK_POSTCODE_AREA_REGEX, self.outward).group()

    @property
    def district(self):
        return re.search(UK_POSTCODE_DISTRICT_REGEX, self.outward).group()

    @property
    def sector(self):
        return re.search(UK_POSTCODE_SECTOR_REGEX, self.inward).group()

    @property
    def unit(self):
        return re.search(UK_POSTCODE_UNIT_REGEX, self.inward).group()

    def validate(self):
        postcode = self.raw_postcode.upper()
        postcode_matchs = UK_POSTCODE_VALIDATION_REGEX.match(postcode)
        if not postcode_matchs:
            raise InvalidPostcode

        self._outward, self._inward = postcode_matchs.groups()
        self.validated_postcode = f"{self._outward} {self._inward}"

        for rule_class in self._rules_list:
            rule = rule_class(self)
            rule.validate()
