# coding: utf-8

"""
    Investor8.Core

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import investor8_sdk
from investor8_sdk.api.search_api import SearchApi  # noqa: E501
from investor8_sdk.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_stocks(self):
        """Test case for search_stocks

        """
        pass


if __name__ == '__main__':
    unittest.main()
