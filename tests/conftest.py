import pytest
from postcode_validator_uk.validators import UKPostcode


@pytest.fixture
def raw_uk_postcode():
    return "EC1A 1BB"


@pytest.fixture
def uk_postcode_validator():
    UKPostcode._rules_list = []

    return UKPostcode


@pytest.fixture
def uk_postcode_validator_instance(raw_uk_postcode, uk_postcode_validator):
    uk_postcode_validator_instance = uk_postcode_validator(raw_uk_postcode)
    uk_postcode_validator_instance.validate()

    return uk_postcode_validator_instance
