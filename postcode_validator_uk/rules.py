import re


class PostcodeRule:
    attr_applied = None
    cases = None
    expression = None

    @classmethod
    def is_valid(cls, postcode):
        postcode_attr_value = getattr(postcode, cls.attr_applied)
        if not postcode_attr_value:
            raise AttributeError(f"This entity has not attr {cls.attr_applied}")

        for case in cls.cases:
            if not postcode_attr_value.startswith(case):
                continue

            if not cls.expression.match(postcode_attr_value):
                return False

        return True


class SingleDigitDistrict(PostcodeRule):
    """
    Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE
    (although WC is always subdivided by a further letter, e.g. WC1A)
    """

    attr_applied = "outward"
    cases = ("BR", "FY", "HA", "HD", "HG", "HR", "HS", "HX", "JE", "LD", "SM", "SR", "WC", "WN", "ZE")
    expression = re.compile(r"^(?!WN)[A-Z]{2}[0-9]$|^WN[0-9][A-Z]$")


class DoubleDigitDistrict(PostcodeRule):
    """Areas with only double-digit districts: AB, LL, SO"""

    attr_applied = "outward"
    cases = ("AB", "LL", "SO")
    expression = re.compile(r"^[A-Z]{2}[0-9]{2}$")
