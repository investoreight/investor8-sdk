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

class CreateUserDto(object):
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
        'user_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'password': 'str',
        'roles': 'list[str]',
        'opt_for_newsletter': 'bool',
        'country': 'str',
        'email_confirmed': 'bool',
        'created_time': 'int',
        'last_modified': 'int',
        'profile_name': 'ProfileName',
        'auth_source': 'AuthenticationSource',
        'external_id': 'str'
    }

    attribute_map = {
        'user_id': 'UserId',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'email': 'Email',
        'password': 'Password',
        'roles': 'Roles',
        'opt_for_newsletter': 'OptForNewsletter',
        'country': 'Country',
        'email_confirmed': 'EmailConfirmed',
        'created_time': 'CreatedTime',
        'last_modified': 'LastModified',
        'profile_name': 'ProfileName',
        'auth_source': 'AuthSource',
        'external_id': 'ExternalId'
    }

    def __init__(self, user_id=None, first_name=None, last_name=None, email=None, password=None, roles=None, opt_for_newsletter=None, country=None, email_confirmed=None, created_time=None, last_modified=None, profile_name=None, auth_source=None, external_id=None):  # noqa: E501
        """CreateUserDto - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._password = None
        self._roles = None
        self._opt_for_newsletter = None
        self._country = None
        self._email_confirmed = None
        self._created_time = None
        self._last_modified = None
        self._profile_name = None
        self._auth_source = None
        self._external_id = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        self.email = email
        if password is not None:
            self.password = password
        self.roles = roles
        if opt_for_newsletter is not None:
            self.opt_for_newsletter = opt_for_newsletter
        if country is not None:
            self.country = country
        if email_confirmed is not None:
            self.email_confirmed = email_confirmed
        if created_time is not None:
            self.created_time = created_time
        if last_modified is not None:
            self.last_modified = last_modified
        if profile_name is not None:
            self.profile_name = profile_name
        if auth_source is not None:
            self.auth_source = auth_source
        if external_id is not None:
            self.external_id = external_id

    @property
    def user_id(self):
        """Gets the user_id of this CreateUserDto.  # noqa: E501


        :return: The user_id of this CreateUserDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateUserDto.


        :param user_id: The user_id of this CreateUserDto.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def first_name(self):
        """Gets the first_name of this CreateUserDto.  # noqa: E501


        :return: The first_name of this CreateUserDto.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CreateUserDto.


        :param first_name: The first_name of this CreateUserDto.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CreateUserDto.  # noqa: E501


        :return: The last_name of this CreateUserDto.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CreateUserDto.


        :param last_name: The last_name of this CreateUserDto.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this CreateUserDto.  # noqa: E501


        :return: The email of this CreateUserDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateUserDto.


        :param email: The email of this CreateUserDto.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this CreateUserDto.  # noqa: E501


        :return: The password of this CreateUserDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateUserDto.


        :param password: The password of this CreateUserDto.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def roles(self):
        """Gets the roles of this CreateUserDto.  # noqa: E501


        :return: The roles of this CreateUserDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CreateUserDto.


        :param roles: The roles of this CreateUserDto.  # noqa: E501
        :type: list[str]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

        self._roles = roles

    @property
    def opt_for_newsletter(self):
        """Gets the opt_for_newsletter of this CreateUserDto.  # noqa: E501


        :return: The opt_for_newsletter of this CreateUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._opt_for_newsletter

    @opt_for_newsletter.setter
    def opt_for_newsletter(self, opt_for_newsletter):
        """Sets the opt_for_newsletter of this CreateUserDto.


        :param opt_for_newsletter: The opt_for_newsletter of this CreateUserDto.  # noqa: E501
        :type: bool
        """

        self._opt_for_newsletter = opt_for_newsletter

    @property
    def country(self):
        """Gets the country of this CreateUserDto.  # noqa: E501


        :return: The country of this CreateUserDto.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreateUserDto.


        :param country: The country of this CreateUserDto.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email_confirmed(self):
        """Gets the email_confirmed of this CreateUserDto.  # noqa: E501


        :return: The email_confirmed of this CreateUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, email_confirmed):
        """Sets the email_confirmed of this CreateUserDto.


        :param email_confirmed: The email_confirmed of this CreateUserDto.  # noqa: E501
        :type: bool
        """

        self._email_confirmed = email_confirmed

    @property
    def created_time(self):
        """Gets the created_time of this CreateUserDto.  # noqa: E501


        :return: The created_time of this CreateUserDto.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CreateUserDto.


        :param created_time: The created_time of this CreateUserDto.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def last_modified(self):
        """Gets the last_modified of this CreateUserDto.  # noqa: E501


        :return: The last_modified of this CreateUserDto.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this CreateUserDto.


        :param last_modified: The last_modified of this CreateUserDto.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def profile_name(self):
        """Gets the profile_name of this CreateUserDto.  # noqa: E501


        :return: The profile_name of this CreateUserDto.  # noqa: E501
        :rtype: ProfileName
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this CreateUserDto.


        :param profile_name: The profile_name of this CreateUserDto.  # noqa: E501
        :type: ProfileName
        """

        self._profile_name = profile_name

    @property
    def auth_source(self):
        """Gets the auth_source of this CreateUserDto.  # noqa: E501


        :return: The auth_source of this CreateUserDto.  # noqa: E501
        :rtype: AuthenticationSource
        """
        return self._auth_source

    @auth_source.setter
    def auth_source(self, auth_source):
        """Sets the auth_source of this CreateUserDto.


        :param auth_source: The auth_source of this CreateUserDto.  # noqa: E501
        :type: AuthenticationSource
        """

        self._auth_source = auth_source

    @property
    def external_id(self):
        """Gets the external_id of this CreateUserDto.  # noqa: E501


        :return: The external_id of this CreateUserDto.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateUserDto.


        :param external_id: The external_id of this CreateUserDto.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if issubclass(CreateUserDto, dict):
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
        if not isinstance(other, CreateUserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
