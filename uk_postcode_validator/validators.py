class UKPostcode:
    outward_code = None
    inward_code = None
    area = None
    district = None
    sector = None
    unit = None
    raw_postcode = None

    def __init__(self, postcode):
        self.raw_postcode = postcode

    def __str__(self):
        return f"{self.raw_postcode}"

    def validate(self):
        raise NotImplementedError()
