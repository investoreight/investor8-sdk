# coding: utf-8

"""
    Investoreight Core API

    Investoreight API Documentation:  https://api.investoreight.com/api-docs/index.html  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@investoreight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AuthenticationRequest(object):
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
        'request_id': 'str',
        'email': 'str',
        'expiration_time': 'int',
        'expired': 'bool',
        'verification_code': 'str',
        'req_type': 'ReqType'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'email': 'Email',
        'expiration_time': 'ExpirationTime',
        'expired': 'Expired',
        'verification_code': 'VerificationCode',
        'req_type': 'ReqType'
    }

    def __init__(self, request_id=None, email=None, expiration_time=None, expired=None, verification_code=None, req_type=None):  # noqa: E501
        """AuthenticationRequest - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._email = None
        self._expiration_time = None
        self._expired = None
        self._verification_code = None
        self._req_type = None
        self.discriminator = None
        if request_id is not None:
            self.request_id = request_id
        if email is not None:
            self.email = email
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if expired is not None:
            self.expired = expired
        if verification_code is not None:
            self.verification_code = verification_code
        if req_type is not None:
            self.req_type = req_type

    @property
    def request_id(self):
        """Gets the request_id of this AuthenticationRequest.  # noqa: E501


        :return: The request_id of this AuthenticationRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AuthenticationRequest.


        :param request_id: The request_id of this AuthenticationRequest.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def email(self):
        """Gets the email of this AuthenticationRequest.  # noqa: E501


        :return: The email of this AuthenticationRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AuthenticationRequest.


        :param email: The email of this AuthenticationRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def expiration_time(self):
        """Gets the expiration_time of this AuthenticationRequest.  # noqa: E501


        :return: The expiration_time of this AuthenticationRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this AuthenticationRequest.


        :param expiration_time: The expiration_time of this AuthenticationRequest.  # noqa: E501
        :type: int
        """

        self._expiration_time = expiration_time

    @property
    def expired(self):
        """Gets the expired of this AuthenticationRequest.  # noqa: E501


        :return: The expired of this AuthenticationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this AuthenticationRequest.


        :param expired: The expired of this AuthenticationRequest.  # noqa: E501
        :type: bool
        """

        self._expired = expired

    @property
    def verification_code(self):
        """Gets the verification_code of this AuthenticationRequest.  # noqa: E501


        :return: The verification_code of this AuthenticationRequest.  # noqa: E501
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this AuthenticationRequest.


        :param verification_code: The verification_code of this AuthenticationRequest.  # noqa: E501
        :type: str
        """

        self._verification_code = verification_code

    @property
    def req_type(self):
        """Gets the req_type of this AuthenticationRequest.  # noqa: E501


        :return: The req_type of this AuthenticationRequest.  # noqa: E501
        :rtype: ReqType
        """
        return self._req_type

    @req_type.setter
    def req_type(self, req_type):
        """Sets the req_type of this AuthenticationRequest.


        :param req_type: The req_type of this AuthenticationRequest.  # noqa: E501
        :type: ReqType
        """

        self._req_type = req_type

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
        if issubclass(AuthenticationRequest, dict):
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
        if not isinstance(other, AuthenticationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
