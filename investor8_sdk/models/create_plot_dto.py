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

class CreatePlotDto(object):
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
        'plot_data': 'str',
        'is_public': 'bool',
        'i8_command': 'str',
        'title': 'str',
        'user_notes': 'str',
        'plot_type': 'str',
        'tickers': 'list[str]',
        'tags': 'list[str]',
        'thumbnail': 'str'
    }

    attribute_map = {
        'user_id': 'UserId',
        'plot_data': 'PlotData',
        'is_public': 'IsPublic',
        'i8_command': 'I8Command',
        'title': 'Title',
        'user_notes': 'UserNotes',
        'plot_type': 'PlotType',
        'tickers': 'Tickers',
        'tags': 'Tags',
        'thumbnail': 'Thumbnail'
    }

    def __init__(self, user_id=None, plot_data=None, is_public=None, i8_command=None, title=None, user_notes=None, plot_type=None, tickers=None, tags=None, thumbnail=None):  # noqa: E501
        """CreatePlotDto - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._plot_data = None
        self._is_public = None
        self._i8_command = None
        self._title = None
        self._user_notes = None
        self._plot_type = None
        self._tickers = None
        self._tags = None
        self._thumbnail = None
        self.discriminator = None
        self.user_id = user_id
        self.plot_data = plot_data
        self.is_public = is_public
        self.i8_command = i8_command
        self.title = title
        if user_notes is not None:
            self.user_notes = user_notes
        self.plot_type = plot_type
        if tickers is not None:
            self.tickers = tickers
        if tags is not None:
            self.tags = tags
        self.thumbnail = thumbnail

    @property
    def user_id(self):
        """Gets the user_id of this CreatePlotDto.  # noqa: E501


        :return: The user_id of this CreatePlotDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreatePlotDto.


        :param user_id: The user_id of this CreatePlotDto.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def plot_data(self):
        """Gets the plot_data of this CreatePlotDto.  # noqa: E501


        :return: The plot_data of this CreatePlotDto.  # noqa: E501
        :rtype: str
        """
        return self._plot_data

    @plot_data.setter
    def plot_data(self, plot_data):
        """Sets the plot_data of this CreatePlotDto.


        :param plot_data: The plot_data of this CreatePlotDto.  # noqa: E501
        :type: str
        """
        if plot_data is None:
            raise ValueError("Invalid value for `plot_data`, must not be `None`")  # noqa: E501

        self._plot_data = plot_data

    @property
    def is_public(self):
        """Gets the is_public of this CreatePlotDto.  # noqa: E501


        :return: The is_public of this CreatePlotDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this CreatePlotDto.


        :param is_public: The is_public of this CreatePlotDto.  # noqa: E501
        :type: bool
        """
        if is_public is None:
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def i8_command(self):
        """Gets the i8_command of this CreatePlotDto.  # noqa: E501


        :return: The i8_command of this CreatePlotDto.  # noqa: E501
        :rtype: str
        """
        return self._i8_command

    @i8_command.setter
    def i8_command(self, i8_command):
        """Sets the i8_command of this CreatePlotDto.


        :param i8_command: The i8_command of this CreatePlotDto.  # noqa: E501
        :type: str
        """
        if i8_command is None:
            raise ValueError("Invalid value for `i8_command`, must not be `None`")  # noqa: E501

        self._i8_command = i8_command

    @property
    def title(self):
        """Gets the title of this CreatePlotDto.  # noqa: E501


        :return: The title of this CreatePlotDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreatePlotDto.


        :param title: The title of this CreatePlotDto.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def user_notes(self):
        """Gets the user_notes of this CreatePlotDto.  # noqa: E501


        :return: The user_notes of this CreatePlotDto.  # noqa: E501
        :rtype: str
        """
        return self._user_notes

    @user_notes.setter
    def user_notes(self, user_notes):
        """Sets the user_notes of this CreatePlotDto.


        :param user_notes: The user_notes of this CreatePlotDto.  # noqa: E501
        :type: str
        """

        self._user_notes = user_notes

    @property
    def plot_type(self):
        """Gets the plot_type of this CreatePlotDto.  # noqa: E501


        :return: The plot_type of this CreatePlotDto.  # noqa: E501
        :rtype: str
        """
        return self._plot_type

    @plot_type.setter
    def plot_type(self, plot_type):
        """Sets the plot_type of this CreatePlotDto.


        :param plot_type: The plot_type of this CreatePlotDto.  # noqa: E501
        :type: str
        """
        if plot_type is None:
            raise ValueError("Invalid value for `plot_type`, must not be `None`")  # noqa: E501

        self._plot_type = plot_type

    @property
    def tickers(self):
        """Gets the tickers of this CreatePlotDto.  # noqa: E501


        :return: The tickers of this CreatePlotDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._tickers

    @tickers.setter
    def tickers(self, tickers):
        """Sets the tickers of this CreatePlotDto.


        :param tickers: The tickers of this CreatePlotDto.  # noqa: E501
        :type: list[str]
        """

        self._tickers = tickers

    @property
    def tags(self):
        """Gets the tags of this CreatePlotDto.  # noqa: E501


        :return: The tags of this CreatePlotDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreatePlotDto.


        :param tags: The tags of this CreatePlotDto.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def thumbnail(self):
        """Gets the thumbnail of this CreatePlotDto.  # noqa: E501


        :return: The thumbnail of this CreatePlotDto.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this CreatePlotDto.


        :param thumbnail: The thumbnail of this CreatePlotDto.  # noqa: E501
        :type: str
        """
        if thumbnail is None:
            raise ValueError("Invalid value for `thumbnail`, must not be `None`")  # noqa: E501

        self._thumbnail = thumbnail

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
        if issubclass(CreatePlotDto, dict):
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
        if not isinstance(other, CreatePlotDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
