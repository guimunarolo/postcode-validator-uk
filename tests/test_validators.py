from unittest import mock

import pytest
from postcode_validator_uk.exceptions import InvalidPostcode, PostcodeNotValidated

from .factories import RuleFactory


def test_uk_postcode_validator_constructor(raw_uk_postcode, uk_postcode_validator_instance):
    assert uk_postcode_validator_instance.raw_postcode == raw_uk_postcode


def test_uk_postcode_validator_string_conversion(raw_uk_postcode, uk_postcode_validator_instance):
    assert f"{uk_postcode_validator_instance}" == raw_uk_postcode


@pytest.mark.parametrize(
    "raw_postcode", ("W31BB", "W3 1BB", "W3  1BB", "W3  1BB",),
)
def test_uk_postcode_validator_validate_with_any_spaces_amount(raw_postcode, uk_postcode_validator):
    assert uk_postcode_validator(raw_postcode).validate() is None


@pytest.mark.parametrize(
    "raw_postcode",
    (
        "EC1A 1BB",
        "W1A 0AX",
        "M1 1AE",
        "B33 8TH",
        "CR2 6XH",
        "DN55 1PT",
        "SW1W 0NY",
        "PO16 7GZ",
        "GU16 7HF",
        "L1 8JQ",
    ),
)
def test_uk_postcode_validator_validate_lowercase_postcodes(raw_postcode, uk_postcode_validator):
    assert uk_postcode_validator(raw_postcode.lower()).validate() is None


@pytest.mark.parametrize(
    "raw_postcode",
    (
        "EC1A 1BB",
        "W1A 0AX",
        "M1 1AE",
        "B33 8TH",
        "CR2 6XH",
        "DN55 1PT",
        "SW1W 0NY",
        "PO16 7GZ",
        "GU16 7HF",
        "L1 8JQ",
    ),
)
def test_uk_postcode_validator_validate_uppercase_postcodes(raw_postcode, uk_postcode_validator):
    assert uk_postcode_validator(raw_postcode).validate() is None


@pytest.mark.parametrize(
    "invalid_postcode", ("EC1A A4BB", "1W1A 0AX", "M001 1AE", "B338-TH5", "CR2 6XH#", "", "0000000", None,),
)
def test_uk_postcode_validator_validate_raises_validation_exception(invalid_postcode, uk_postcode_validator):
    with pytest.raises(InvalidPostcode):
        uk_postcode_validator(invalid_postcode).validate()


def test_uk_postcode_validator_outward_raises_exception_when_not_validated(uk_postcode_validator):
    postcode_instance = uk_postcode_validator("EC1A 1BB")
    with pytest.raises(PostcodeNotValidated):
        postcode_instance.outward


@pytest.mark.parametrize(
    "raw_postcode, expected_outward",
    (
        ("EC1A 1BB", "EC1A"),
        ("W1A 0AX", "W1A"),
        ("M1 1AE", "M1"),
        ("EC1A1BB", "EC1A"),
        ("W1A0AX", "W1A"),
        ("M11AE", "M1"),
    ),
)
def test_uk_postcode_validator_outward_result(raw_postcode, expected_outward, uk_postcode_validator):
    postcode_instance = uk_postcode_validator(raw_postcode)
    postcode_instance.validate()

    assert postcode_instance.outward == expected_outward


def test_uk_postcode_validator_inward_raises_exception_when_not_validated(uk_postcode_validator):
    postcode_instance = uk_postcode_validator("EC1A 1BB")
    with pytest.raises(PostcodeNotValidated):
        postcode_instance.inward


@pytest.mark.parametrize(
    "raw_postcode, expected_inward",
    (
        ("EC1A 1BB", "1BB"),
        ("W1A 0AX", "0AX"),
        ("M1 1AE", "1AE"),
        ("EC1A1BB", "1BB"),
        ("W1A0AX", "0AX"),
        ("M11AE", "1AE"),
    ),
)
def test_uk_postcode_validator_inward_result(raw_postcode, expected_inward, uk_postcode_validator):
    postcode_instance = uk_postcode_validator(raw_postcode)
    postcode_instance.validate()

    assert postcode_instance.inward == expected_inward


def test_uk_postcode_validator_area_raises_exception_when_not_validated(uk_postcode_validator):
    postcode_instance = uk_postcode_validator("EC1A 1BB")
    with pytest.raises(PostcodeNotValidated):
        postcode_instance.area


@pytest.mark.parametrize(
    "raw_postcode, expected_area",
    (
        ("EC1A 1BB", "EC"),
        ("W1A 0AX", "W"),
        ("M1 1AE", "M"),
        ("EC1A1BB", "EC"),
        ("W1A0AX", "W"),
        ("M11AE", "M"),
    ),
)
def test_uk_postcode_validator_area_result(raw_postcode, expected_area, uk_postcode_validator):
    postcode_instance = uk_postcode_validator(raw_postcode)
    postcode_instance.validate()

    assert postcode_instance.area == expected_area


def test_uk_postcode_validator_district_raises_exception_when_not_validated(uk_postcode_validator):
    postcode_instance = uk_postcode_validator("EC1A 1BB")
    with pytest.raises(PostcodeNotValidated):
        postcode_instance.district


@pytest.mark.parametrize(
    "raw_postcode, expected_district",
    (
        ("EC1A 1BB", "1A"),
        ("W1A 0AX", "1A"),
        ("M1 1AE", "1"),
        ("EC1A1BB", "1A"),
        ("W1A0AX", "1A"),
        ("M11AE", "1"),
    ),
)
def test_uk_postcode_validator_district_result(raw_postcode, expected_district, uk_postcode_validator):
    postcode_instance = uk_postcode_validator(raw_postcode)
    postcode_instance.validate()

    assert postcode_instance.district == expected_district


def test_uk_postcode_validator_sector_raises_exception_when_not_validated(uk_postcode_validator):
    postcode_instance = uk_postcode_validator("EC1A 1BB")
    with pytest.raises(PostcodeNotValidated):
        postcode_instance.sector


@pytest.mark.parametrize(
    "raw_postcode, expected_sector",
    (
        ("EC1A 1BB", "1"),
        ("W1A 0AX", "0"),
        ("M1 1AE", "1"),
        ("EC1A1BB", "1"),
        ("W1A0AX", "0"),
        ("M11AE", "1"),
    ),
)
def test_uk_postcode_validator_sector_result(raw_postcode, expected_sector, uk_postcode_validator):
    postcode_instance = uk_postcode_validator(raw_postcode)
    postcode_instance.validate()

    assert postcode_instance.sector == expected_sector


def test_uk_postcode_validator_unit_raises_exception_when_not_validated(uk_postcode_validator):
    postcode_instance = uk_postcode_validator("EC1A 1BB")
    with pytest.raises(PostcodeNotValidated):
        postcode_instance.unit


@pytest.mark.parametrize(
    "raw_postcode, expected_unit",
    (
        ("EC1A 1BB", "BB"),
        ("W1A 0AX", "AX"),
        ("M1 1AE", "AE"),
        ("EC1A1BB", "BB"),
        ("W1A0AX", "AX"),
        ("M11AE", "AE"),
    ),
)
def test_uk_postcode_validator_unit_result(raw_postcode, expected_unit, uk_postcode_validator):
    postcode_instance = uk_postcode_validator(raw_postcode)
    postcode_instance.validate()

    assert postcode_instance.unit == expected_unit


def test_uk_postcode_validator_validate_rules_iterate_list(uk_postcode_validator, raw_uk_postcode):
    RuleFactory.validate = mock.Mock()
    uk_postcode_validator._rules_list = (RuleFactory, RuleFactory)

    assert uk_postcode_validator(raw_uk_postcode).validate() is None
    assert RuleFactory.validate.call_count == 2


def test_uk_postcode_validator_validate_raises_validation_exception_from_rules(uk_postcode_validator):
    RuleFactory.validate.side_effect = InvalidPostcode
    uk_postcode_validator._rules_list = (RuleFactory, RuleFactory)

    with pytest.raises(InvalidPostcode):
        uk_postcode_validator(uk_postcode_validator).validate()
        assert RuleFactory.validate.called_count == 1
