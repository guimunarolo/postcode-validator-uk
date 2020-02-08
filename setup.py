import codecs
import os
import re

import setuptools

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
readme = os.path.join(CURRENT_PATH, "README.md")
with open(readme, "r") as fh:
    long_description = fh.read()

# Get version dynamically from CHANGES.rst
version = "0.1.0"
pattern = re.compile(r"^#*\s*(?P<version>[0-9]+\.[0-9]+(\.[0-9]+)?)$")
changes = os.path.join(CURRENT_PATH, "CHANGES.rst")
with codecs.open(changes, encoding="utf-8") as changes:
    for line in changes:
        res = pattern.match(line)
        if res:
            version = res.group("version")
            break


setuptools.setup(
    name="postcode-validator-uk",
    version=version,
    url="https://github.com/guimunarolo/postcode-validator-uk",
    license="MIT",
    author="Guilherme Munarolo",
    author_email="guimunarolo@hotmail.com",
    description="A simple UK postcode validator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3",
)
