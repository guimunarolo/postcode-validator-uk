import pytest


def test_uk_postcode_validator_constructor(raw_uk_postalcode, uk_postalcode_instance):
    assert uk_postalcode_instance.raw_postcode == raw_uk_postalcode


def test_uk_postcode_validator_string_conversion(raw_uk_postalcode, uk_postalcode_instance):
    assert f"{uk_postalcode_instance}" == raw_uk_postalcode


def test_uk_postcode_validator_validate_is_not_implemented(uk_postalcode_instance):
    with pytest.raises(NotImplementedError):
        uk_postalcode_instance.validate()
