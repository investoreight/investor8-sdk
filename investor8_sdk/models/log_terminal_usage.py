# coding: utf-8

"""
    Investoreight Core API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@investoreight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LogTerminalUsage(object):
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
        'command': 'str',
        'usage_date_time': 'datetime',
        'version': 'str',
        'os': 'str',
        'app_instance_id': 'str',
        'exception': 'str',
        'id': 'str'
    }

    attribute_map = {
        'command': 'Command',
        'usage_date_time': 'UsageDateTime',
        'version': 'Version',
        'os': 'OS',
        'app_instance_id': 'AppInstanceId',
        'exception': 'Exception',
        'id': 'Id'
    }

    def __init__(self, command=None, usage_date_time=None, version=None, os=None, app_instance_id=None, exception=None, id=None):  # noqa: E501
        """LogTerminalUsage - a model defined in Swagger"""  # noqa: E501
        self._command = None
        self._usage_date_time = None
        self._version = None
        self._os = None
        self._app_instance_id = None
        self._exception = None
        self._id = None
        self.discriminator = None
        if command is not None:
            self.command = command
        if usage_date_time is not None:
            self.usage_date_time = usage_date_time
        if version is not None:
            self.version = version
        if os is not None:
            self.os = os
        if app_instance_id is not None:
            self.app_instance_id = app_instance_id
        if exception is not None:
            self.exception = exception
        if id is not None:
            self.id = id

    @property
    def command(self):
        """Gets the command of this LogTerminalUsage.  # noqa: E501


        :return: The command of this LogTerminalUsage.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this LogTerminalUsage.


        :param command: The command of this LogTerminalUsage.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def usage_date_time(self):
        """Gets the usage_date_time of this LogTerminalUsage.  # noqa: E501


        :return: The usage_date_time of this LogTerminalUsage.  # noqa: E501
        :rtype: datetime
        """
        return self._usage_date_time

    @usage_date_time.setter
    def usage_date_time(self, usage_date_time):
        """Sets the usage_date_time of this LogTerminalUsage.


        :param usage_date_time: The usage_date_time of this LogTerminalUsage.  # noqa: E501
        :type: datetime
        """

        self._usage_date_time = usage_date_time

    @property
    def version(self):
        """Gets the version of this LogTerminalUsage.  # noqa: E501


        :return: The version of this LogTerminalUsage.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LogTerminalUsage.


        :param version: The version of this LogTerminalUsage.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def os(self):
        """Gets the os of this LogTerminalUsage.  # noqa: E501


        :return: The os of this LogTerminalUsage.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this LogTerminalUsage.


        :param os: The os of this LogTerminalUsage.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def app_instance_id(self):
        """Gets the app_instance_id of this LogTerminalUsage.  # noqa: E501


        :return: The app_instance_id of this LogTerminalUsage.  # noqa: E501
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id):
        """Sets the app_instance_id of this LogTerminalUsage.


        :param app_instance_id: The app_instance_id of this LogTerminalUsage.  # noqa: E501
        :type: str
        """

        self._app_instance_id = app_instance_id

    @property
    def exception(self):
        """Gets the exception of this LogTerminalUsage.  # noqa: E501


        :return: The exception of this LogTerminalUsage.  # noqa: E501
        :rtype: str
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """Sets the exception of this LogTerminalUsage.


        :param exception: The exception of this LogTerminalUsage.  # noqa: E501
        :type: str
        """

        self._exception = exception

    @property
    def id(self):
        """Gets the id of this LogTerminalUsage.  # noqa: E501


        :return: The id of this LogTerminalUsage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogTerminalUsage.


        :param id: The id of this LogTerminalUsage.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(LogTerminalUsage, dict):
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
        if not isinstance(other, LogTerminalUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
