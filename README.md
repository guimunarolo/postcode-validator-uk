# postcode-validator-uk

[![Python](https://img.shields.io/pypi/pyversions/postcode-validator-uk)](https://www.python.org/downloads/release/python-3/)
[![CircleCI](https://circleci.com/gh/guimunarolo/postcode-validator-uk.svg?style=shield)](https://circleci.com/gh/guimunarolo/postcode-validator-uk)
[![codecov](https://codecov.io/gh/guimunarolo/postcode-validator-uk/branch/master/graph/badge.svg)](https://codecov.io/gh/guimunarolo/postcode-validator-uk)

A simple UK postcode validator.

> Implemented following these instructions: [Wikipedia - Postcodes in the United Kingdom](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting).


## Install

postcode-validator-uk is available on PyPI:

```bash
$ pip install postcode-validator-uk
```


## Usage

```python
from postcode_validator_uk.validators import UKPostcode

postcode = UKPostcode('ec1a 1bb')
postcode.validate()

postcode.validated_postcode
# output
'EC1A 1BB'

postcode.raw_postcode
# output
'ec1a 1bb'

postcode.outward
# output
'EC1A'

postcode.inward
# output
'1BB'

postcode.area
# output
'EC'

postcode.district
# output
'1A'

postcode.sector
# output
'1'

postcode.unit
# output
'BB'
```


## Running tests

```bash
$ pipenv install --dev
$ make test
```
