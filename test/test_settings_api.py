# coding: utf-8

"""
    Investor8.Core

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import investor8_sdk
from investor8_sdk.api.settings_api import SettingsApi  # noqa: E501
from investor8_sdk.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_i8t_version(self):
        """Test case for get_i8t_version

        """
        pass

    def test_set_i8t_version(self):
        """Test case for set_i8t_version

        """
        pass


if __name__ == '__main__':
    unittest.main()
