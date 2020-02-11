import re

from .exceptions import InvalidPostcode


class PostcodeRule:
    attr_applied = None
    applied_areas_regex = None
    rule_regex = None

    def __init__(self, postcode):
        self.postcode = postcode

    def validate(self):
        postcode_attr_value = getattr(self.postcode, self.attr_applied, None)
        if not postcode_attr_value:
            raise AttributeError(f"This entity has not attr {self.attr_applied}")

        if not self.applied_areas_regex.match(postcode_attr_value):
            return

        if not self.rule_regex.match(postcode_attr_value):
            raise InvalidPostcode


class SingleDigitDistrict(PostcodeRule):
    """
    Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE
    (although WC is always subdivided by a further letter, e.g. WC1A)
    """

    attr_applied = "outward"
    applied_areas_regex = re.compile(r"^(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)")
    rule_regex = re.compile(r"^(?!WC)[A-Z]{2}[0-9]$|^WC[0-9][A-Z]$")


class DoubleDigitDistrict(PostcodeRule):
    """Areas with only double-digit districts: AB, LL, SO"""

    attr_applied = "outward"
    applied_areas_regex = re.compile(r"^(AB|LL|SO)")
    rule_regex = re.compile(r"^[A-Z]{2}[0-9]{2}$")
