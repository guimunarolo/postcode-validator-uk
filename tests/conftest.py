import pytest
from uk_postcode_validator.validators import UKPostcode


@pytest.fixture
def raw_uk_postalcode():
    return "EC1A 1BB"


@pytest.fixture
def uk_postalcode_validator():
    return UKPostcode


@pytest.fixture
def uk_postalcode_validator_instance(raw_uk_postalcode, uk_postalcode_validator):
    uk_postalcode_validator_instance = uk_postalcode_validator(raw_uk_postalcode)
    uk_postalcode_validator_instance.validate()

    return uk_postalcode_validator_instance
