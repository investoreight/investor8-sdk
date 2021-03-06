# coding: utf-8

"""
    Investor8.Core

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SendEmailDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email_address': 'str',
        'email_type': 'EmailType',
        'url_link': 'str',
        'verification_code': 'str'
    }

    attribute_map = {
        'email_address': 'EmailAddress',
        'email_type': 'EmailType',
        'url_link': 'UrlLink',
        'verification_code': 'VerificationCode'
    }

    def __init__(self, email_address=None, email_type=None, url_link=None, verification_code=None):  # noqa: E501
        """SendEmailDto - a model defined in Swagger"""  # noqa: E501
        self._email_address = None
        self._email_type = None
        self._url_link = None
        self._verification_code = None
        self.discriminator = None
        if email_address is not None:
            self.email_address = email_address
        if email_type is not None:
            self.email_type = email_type
        if url_link is not None:
            self.url_link = url_link
        if verification_code is not None:
            self.verification_code = verification_code

    @property
    def email_address(self):
        """Gets the email_address of this SendEmailDto.  # noqa: E501


        :return: The email_address of this SendEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this SendEmailDto.


        :param email_address: The email_address of this SendEmailDto.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def email_type(self):
        """Gets the email_type of this SendEmailDto.  # noqa: E501


        :return: The email_type of this SendEmailDto.  # noqa: E501
        :rtype: EmailType
        """
        return self._email_type

    @email_type.setter
    def email_type(self, email_type):
        """Sets the email_type of this SendEmailDto.


        :param email_type: The email_type of this SendEmailDto.  # noqa: E501
        :type: EmailType
        """

        self._email_type = email_type

    @property
    def url_link(self):
        """Gets the url_link of this SendEmailDto.  # noqa: E501


        :return: The url_link of this SendEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._url_link

    @url_link.setter
    def url_link(self, url_link):
        """Sets the url_link of this SendEmailDto.


        :param url_link: The url_link of this SendEmailDto.  # noqa: E501
        :type: str
        """

        self._url_link = url_link

    @property
    def verification_code(self):
        """Gets the verification_code of this SendEmailDto.  # noqa: E501


        :return: The verification_code of this SendEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this SendEmailDto.


        :param verification_code: The verification_code of this SendEmailDto.  # noqa: E501
        :type: str
        """

        self._verification_code = verification_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SendEmailDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendEmailDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
