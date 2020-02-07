import pytest
from uk_postcode_validator.validators import UKPostcode


@pytest.fixture
def raw_uk_postalcode():
    return "EC1A 1BB"


@pytest.fixture
def uk_postalcode_instance(raw_uk_postalcode):
    return UKPostcode(raw_uk_postalcode)
