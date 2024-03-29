# coding: utf-8

"""
    Investoreight Core API

    Investoreight API Documentation:  https://api.investoreight.com/api-docs/index.html  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@investoreight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "investor8-sdk"
VERSION = "1.1.108"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


def get_long_description() -> str:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
    return long_description


REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

PROJECT_URLS = {
    "Homepage": "https://www.investoreight.com/",
    "Documentation": "https://github.com/investoreight/investor8-sdk#readme",
    "Download": "https://github.com/investoreight/investor8-sdk/releases",
    "Source Code": "https://github.com/investoreight/investor8-sdk",
    "Bug Tracker": "https://github.com/investoreight/investor8-sdk/issues"
}


setup(
    name=NAME,
    version=VERSION,
    project_urls=PROJECT_URLS,
    description="Investoreight Core API",
    author_email="info@investoreight.com",
    url="",
    keywords=["Swagger", "Investoreight Core API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=get_long_description(),
    long_description_content_type="text/markdown"
)
