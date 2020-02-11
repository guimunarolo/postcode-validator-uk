import re
from unittest import mock

import pytest
from postcode_validator_uk.exceptions import InvalidPostcode
from postcode_validator_uk.rules import (
    DoubleDigitDistrict,
    PostcodeRule,
    SingleDigitDistrict,
    ZeroOrTenDistrict,
)

SINGLE_DIGIT_DISTRICTS_AREAS = (
    "BR",
    "FY",
    "HA",
    "HD",
    "HG",
    "HR",
    "HS",
    "HX",
    "JE",
    "LD",
    "SM",
    "SR",
    "WC",
    "WN",
    "ZE",
)
DOUBLE_DIGIT_DISTRICTS_AREAS = ("AB", "LL", "SO")
ZERO_OR_TEN_DISTRICTS_AREAS = ("BL", "BS", "CM", "CR", "FY", "HA", "PR", "SL", "SS")


class TestPostcodeRule:
    def test_validation_raises_attr_error_without_required_attr(self):
        PostcodeRule.attr_applied = "outward"

        postcode = mock.Mock(outward=None)

        with pytest.raises(AttributeError):
            rule = PostcodeRule(postcode)
            rule.validate()

    def test_validation_returns_none_without_match_any_case(self):
        PostcodeRule.attr_applied = "outward"
        PostcodeRule.applied_areas_regex = re.compile(r"BR|FY")

        postcode = mock.Mock(outward="HA1")
        rule = PostcodeRule(postcode)

        assert rule.validate() is None

    def test_validation_returns_false_with_invalid_postcode(self):
        PostcodeRule.attr_applied = "outward"
        PostcodeRule.applied_areas_regex = re.compile(r"BR|FY")
        PostcodeRule.rule_regex = re.compile(r"^[A-Z]{2}[0-9]$")

        postcode = mock.Mock(outward="BRA")
        rule = PostcodeRule(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()


class TestSingleDigitDistrict:
    @pytest.mark.parametrize("area", SINGLE_DIGIT_DISTRICTS_AREAS)
    def test_validating_valid_postcodes(self, area):
        outward = f"{area}1" if area != "WC" else f"{area}1A"
        postcode = mock.Mock(outward=outward)
        rule = SingleDigitDistrict(postcode)

        assert rule.validate() is None

    @pytest.mark.parametrize("area", SINGLE_DIGIT_DISTRICTS_AREAS)
    def test_invalidating_when_has_double_digits(self, area):
        postcode = mock.Mock(outward=f"{area}11")
        rule = SingleDigitDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()

    @pytest.mark.parametrize("area", SINGLE_DIGIT_DISTRICTS_AREAS)
    def test_invalidating_when_has_alphanumeric(self, area):
        postcode = mock.Mock(outward=f"{area}A")
        rule = SingleDigitDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()

    @pytest.mark.parametrize("area", SINGLE_DIGIT_DISTRICTS_AREAS)
    def test_invalidating_when_has_no_digit(self, area):
        postcode = mock.Mock(outward=f"{area}")
        rule = SingleDigitDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()


class TestDoubleDigitDistrict:
    @pytest.mark.parametrize("area", DOUBLE_DIGIT_DISTRICTS_AREAS)
    def test_validating_valid_postcode(self, area):
        postcode = mock.Mock(outward=f"{area}11")
        rule = DoubleDigitDistrict(postcode)

        assert rule.validate() is None

    @pytest.mark.parametrize("area", DOUBLE_DIGIT_DISTRICTS_AREAS)
    def test_invalidating_when_has_only_one_digit(self, area):
        postcode = mock.Mock(outward=f"{area}1")
        rule = DoubleDigitDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()

    @pytest.mark.parametrize("area", DOUBLE_DIGIT_DISTRICTS_AREAS)
    def test_invalidating_when_has_alphanumeric(self, area):
        postcode = mock.Mock(outward=f"{area}A1")
        rule = DoubleDigitDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()

    @pytest.mark.parametrize("area", DOUBLE_DIGIT_DISTRICTS_AREAS)
    def test_invalidating_has_no_digit(self, area):
        postcode = mock.Mock(outward=f"{area}")
        rule = DoubleDigitDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()


class TestZeroOrTenDistrict:
    @pytest.mark.parametrize("area", ZERO_OR_TEN_DISTRICTS_AREAS)
    def test_validating_valid_postcode_with_ditrict_zero(self, area):
        postcode = mock.Mock(outward=f"{area}0")
        rule = ZeroOrTenDistrict(postcode)

        assert rule.validate() is None

    @pytest.mark.parametrize("area", ZERO_OR_TEN_DISTRICTS_AREAS)
    def test_validating_valid_postcode_with_district_ten_only_with_BS(self, area):
        postcode = mock.Mock(outward=f"{area}10")
        rule = ZeroOrTenDistrict(postcode)

        if area == "BS":
            assert rule.validate() is None
        else:
            with pytest.raises(InvalidPostcode):
                rule.validate()

    @pytest.mark.parametrize("area", ZERO_OR_TEN_DISTRICTS_AREAS)
    def test_invalidating_when_has_wrong_digit(self, area):
        postcode = mock.Mock(outward=f"{area}1")
        rule = ZeroOrTenDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()

    @pytest.mark.parametrize("area", ZERO_OR_TEN_DISTRICTS_AREAS)
    def test_invalidating_when_has_alphanumeric(self, area):
        postcode = mock.Mock(outward=f"{area}A")
        rule = ZeroOrTenDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()

    @pytest.mark.parametrize("area", ZERO_OR_TEN_DISTRICTS_AREAS)
    def test_invalidating_when_has_too_many_digits(self, area):
        postcode = mock.Mock(outward=f"{area}101")
        rule = ZeroOrTenDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()

    @pytest.mark.parametrize("area", ZERO_OR_TEN_DISTRICTS_AREAS)
    def test_invalidating_has_no_digit(self, area):
        postcode = mock.Mock(outward=f"{area}")
        rule = ZeroOrTenDistrict(postcode)

        with pytest.raises(InvalidPostcode):
            rule.validate()
