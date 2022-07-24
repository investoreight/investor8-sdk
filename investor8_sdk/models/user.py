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

class User(object):
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
        'id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'roles': 'list[str]',
        'opt_for_newsletter': 'bool',
        'country': 'str',
        'email_confirmed': 'bool',
        'created_time': 'int',
        'last_modified': 'int',
        'profile_name': 'str',
        'api_key': 'str',
        'auth_source': 'str',
        'external_id': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'email': 'Email',
        'roles': 'Roles',
        'opt_for_newsletter': 'OptForNewsletter',
        'country': 'Country',
        'email_confirmed': 'EmailConfirmed',
        'created_time': 'CreatedTime',
        'last_modified': 'LastModified',
        'profile_name': 'ProfileName',
        'api_key': 'ApiKey',
        'auth_source': 'AuthSource',
        'external_id': 'ExternalId'
    }

    def __init__(self, id=None, first_name=None, last_name=None, email=None, roles=None, opt_for_newsletter=None, country=None, email_confirmed=None, created_time=None, last_modified=None, profile_name=None, api_key=None, auth_source=None, external_id=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._roles = None
        self._opt_for_newsletter = None
        self._country = None
        self._email_confirmed = None
        self._created_time = None
        self._last_modified = None
        self._profile_name = None
        self._api_key = None
        self._auth_source = None
        self._external_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if roles is not None:
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
        if api_key is not None:
            self.api_key = api_key
        if auth_source is not None:
            self.auth_source = auth_source
        if external_id is not None:
            self.external_id = external_id

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501


        :return: The roles of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.


        :param roles: The roles of this User.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def opt_for_newsletter(self):
        """Gets the opt_for_newsletter of this User.  # noqa: E501


        :return: The opt_for_newsletter of this User.  # noqa: E501
        :rtype: bool
        """
        return self._opt_for_newsletter

    @opt_for_newsletter.setter
    def opt_for_newsletter(self, opt_for_newsletter):
        """Sets the opt_for_newsletter of this User.


        :param opt_for_newsletter: The opt_for_newsletter of this User.  # noqa: E501
        :type: bool
        """

        self._opt_for_newsletter = opt_for_newsletter

    @property
    def country(self):
        """Gets the country of this User.  # noqa: E501


        :return: The country of this User.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this User.


        :param country: The country of this User.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email_confirmed(self):
        """Gets the email_confirmed of this User.  # noqa: E501


        :return: The email_confirmed of this User.  # noqa: E501
        :rtype: bool
        """
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, email_confirmed):
        """Sets the email_confirmed of this User.


        :param email_confirmed: The email_confirmed of this User.  # noqa: E501
        :type: bool
        """

        self._email_confirmed = email_confirmed

    @property
    def created_time(self):
        """Gets the created_time of this User.  # noqa: E501


        :return: The created_time of this User.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this User.


        :param created_time: The created_time of this User.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def last_modified(self):
        """Gets the last_modified of this User.  # noqa: E501


        :return: The last_modified of this User.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this User.


        :param last_modified: The last_modified of this User.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def profile_name(self):
        """Gets the profile_name of this User.  # noqa: E501


        :return: The profile_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this User.


        :param profile_name: The profile_name of this User.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def api_key(self):
        """Gets the api_key of this User.  # noqa: E501


        :return: The api_key of this User.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this User.


        :param api_key: The api_key of this User.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def auth_source(self):
        """Gets the auth_source of this User.  # noqa: E501


        :return: The auth_source of this User.  # noqa: E501
        :rtype: str
        """
        return self._auth_source

    @auth_source.setter
    def auth_source(self, auth_source):
        """Sets the auth_source of this User.


        :param auth_source: The auth_source of this User.  # noqa: E501
        :type: str
        """

        self._auth_source = auth_source

    @property
    def external_id(self):
        """Gets the external_id of this User.  # noqa: E501


        :return: The external_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this User.


        :param external_id: The external_id of this User.  # noqa: E501
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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
