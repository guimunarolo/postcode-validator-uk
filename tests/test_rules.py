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


@pytest.mark.parametrize(
    "outward",
    (
        "BR1",
        "FY1",
        "HA1",
        "HD1",
        "HG1",
        "HR1",
        "HS1",
        "HX1",
        "JE1",
        "LD1",
        "SM1",
        "SR1",
        "WC1",
        "WN1A",
        "ZE1",
    ),
)
def test_single_digit_district_validation(outward):
    valid_postcode = mock.Mock(outward=outward)
    assert SingleDigitDistrict.is_valid(valid_postcode) is True

    invalid_postcode = mock.Mock(outward=f"{outward}11")
    assert SingleDigitDistrict.is_valid(invalid_postcode) is False

    invalid_postcode = mock.Mock(outward=f"{outward}A")
    assert SingleDigitDistrict.is_valid(invalid_postcode) is False

    invalid_postcode = mock.Mock(outward=f"{outward[:2]}")
    assert SingleDigitDistrict.is_valid(invalid_postcode) is False


@pytest.mark.parametrize("outward", ("AB11", "LL11", "SO11"))
def test_double_digit_district_validation(outward):
    valid_postcode = mock.Mock(outward=outward)
    assert DoubleDigitDistrict.is_valid(valid_postcode) is True

    invalid_postcode = mock.Mock(outward=f"{outward}1")
    assert DoubleDigitDistrict.is_valid(invalid_postcode) is False

    invalid_postcode = mock.Mock(outward=f"{outward}A")
    assert DoubleDigitDistrict.is_valid(invalid_postcode) is False

    invalid_postcode = mock.Mock(outward=f"{outward[:2]}")
    assert DoubleDigitDistrict.is_valid(invalid_postcode) is False
