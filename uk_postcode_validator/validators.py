import re

from . import constants


class UKPostcode:
    outward_code = None
    inward_code = None
    area = None
    district = None
    sector = None
    unit = None
    raw_postcode = None

    def __init__(self, postcode):
        self.raw_postcode = f"{postcode}"

    def __str__(self):
        return f"{self.raw_postcode}"

    def validate(self):
        postcode = self.raw_postcode.upper()
        validation_regex = re.compile(constants.UK_POSTCODE_VALIDATION_REGEX)
        if not validation_regex.match(postcode):
            return False

        return True
