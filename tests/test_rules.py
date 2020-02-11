import re
from unittest import mock

import pytest
from postcode_validator_uk.rules import DoubleDigitDistrict, PostcodeRule, SingleDigitDistrict


def test_rule_validation_raises_attr_error_without_required_attr():
    PostcodeRule.attr_applied = "outward"

    postcode = mock.Mock(outward=None)

    with pytest.raises(AttributeError):
        PostcodeRule.is_valid(postcode)


def test_rule_validation_returns_true_without_match_any_case():
    PostcodeRule.attr_applied = "outward"
    PostcodeRule.cases = ("BR", "FY")

    postcode = mock.Mock(outward="HA1")

    assert PostcodeRule.is_valid(postcode) is True


def test_rule_validation_returns_false_with_invalid_postcode():
    PostcodeRule.attr_applied = "outward"
    PostcodeRule.cases = ("BR", "FY")
    PostcodeRule.expression = re.compile(r"^[A-Z]{2}[0-9]$")

    postcode = mock.Mock(outward="BRA")

    assert PostcodeRule.is_valid(postcode) is False


@pytest.mark.parametrize("area", SingleDigitDistrict.cases)
def test_single_digit_district_validating_valid_postcodes(area):
    outward = f"{area}1" if area != "WC" else f"{area}1A"
    postcode = mock.Mock(outward=outward)

    assert SingleDigitDistrict.is_valid(postcode) is True


@pytest.mark.parametrize("area", SingleDigitDistrict.cases)
def test_single_digit_district_invalidating_when_has_double_digits(area):
    postcode = mock.Mock(outward=f"{area}11")

    assert SingleDigitDistrict.is_valid(postcode) is False


@pytest.mark.parametrize("area", SingleDigitDistrict.cases)
def test_single_digit_district_invalidating_when_has_alphanumeric(area):
    postcode = mock.Mock(outward=f"{area}A")

    assert SingleDigitDistrict.is_valid(postcode) is False


@pytest.mark.parametrize("area", SingleDigitDistrict.cases)
def test_single_digit_district_invalidating_when_has_no_digit(area):
    postcode = mock.Mock(outward=f"{area}")

    assert SingleDigitDistrict.is_valid(postcode) is False


@pytest.mark.parametrize("area", DoubleDigitDistrict.cases)
def test_double_digit_district_validating_valid_postcode(area):
    postcode = mock.Mock(outward=f"{area}11")

    assert DoubleDigitDistrict.is_valid(postcode) is True


@pytest.mark.parametrize("area", DoubleDigitDistrict.cases)
def test_double_digit_district_invalidating_when_has_only_one_digit(area):
    postcode = mock.Mock(outward=f"{area}1")

    assert DoubleDigitDistrict.is_valid(postcode) is False


@pytest.mark.parametrize("area", DoubleDigitDistrict.cases)
def test_double_digit_district_invalidating_when_has_alphanumeric(area):
    postcode = mock.Mock(outward=f"{area}A1")

    assert DoubleDigitDistrict.is_valid(postcode) is False


@pytest.mark.parametrize("area", DoubleDigitDistrict.cases)
def test_double_digit_district_invalidating_has_no_digit(area):
    postcode = mock.Mock(outward=f"{area}")

    assert DoubleDigitDistrict.is_valid(postcode) is False
