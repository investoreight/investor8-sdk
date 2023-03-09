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

class MetricsMetadata(object):
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
        'metric_name': 'str',
        'display_name': 'str',
        'description': 'str',
        'unit': 'str',
        'categories': 'list[str]',
        'data_format': 'str',
        'display_format': 'str',
        'type': 'str',
        'last_modified': 'int',
        'period_type_default': 'str',
        'remarks': 'str',
        'screening_conditions': 'list[ScreeningCondition]',
        'internal_comment': 'str',
        'aliases': 'str',
        'colorable': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'metric_name': 'MetricName',
        'display_name': 'DisplayName',
        'description': 'Description',
        'unit': 'Unit',
        'categories': 'Categories',
        'data_format': 'DataFormat',
        'display_format': 'DisplayFormat',
        'type': 'Type',
        'last_modified': 'LastModified',
        'period_type_default': 'PeriodTypeDefault',
        'remarks': 'Remarks',
        'screening_conditions': 'ScreeningConditions',
        'internal_comment': 'InternalComment',
        'aliases': 'Aliases',
        'colorable': 'Colorable',
        'id': 'Id'
    }

    def __init__(self, metric_name=None, display_name=None, description=None, unit=None, categories=None, data_format=None, display_format=None, type=None, last_modified=None, period_type_default=None, remarks=None, screening_conditions=None, internal_comment=None, aliases=None, colorable=None, id=None):  # noqa: E501
        """MetricsMetadata - a model defined in Swagger"""  # noqa: E501
        self._metric_name = None
        self._display_name = None
        self._description = None
        self._unit = None
        self._categories = None
        self._data_format = None
        self._display_format = None
        self._type = None
        self._last_modified = None
        self._period_type_default = None
        self._remarks = None
        self._screening_conditions = None
        self._internal_comment = None
        self._aliases = None
        self._colorable = None
        self._id = None
        self.discriminator = None
        if metric_name is not None:
            self.metric_name = metric_name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if unit is not None:
            self.unit = unit
        if categories is not None:
            self.categories = categories
        if data_format is not None:
            self.data_format = data_format
        if display_format is not None:
            self.display_format = display_format
        if type is not None:
            self.type = type
        if last_modified is not None:
            self.last_modified = last_modified
        if period_type_default is not None:
            self.period_type_default = period_type_default
        if remarks is not None:
            self.remarks = remarks
        if screening_conditions is not None:
            self.screening_conditions = screening_conditions
        if internal_comment is not None:
            self.internal_comment = internal_comment
        if aliases is not None:
            self.aliases = aliases
        if colorable is not None:
            self.colorable = colorable
        if id is not None:
            self.id = id

    @property
    def metric_name(self):
        """Gets the metric_name of this MetricsMetadata.  # noqa: E501


        :return: The metric_name of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricsMetadata.


        :param metric_name: The metric_name of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

    @property
    def display_name(self):
        """Gets the display_name of this MetricsMetadata.  # noqa: E501


        :return: The display_name of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MetricsMetadata.


        :param display_name: The display_name of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this MetricsMetadata.  # noqa: E501


        :return: The description of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MetricsMetadata.


        :param description: The description of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def unit(self):
        """Gets the unit of this MetricsMetadata.  # noqa: E501


        :return: The unit of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MetricsMetadata.


        :param unit: The unit of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def categories(self):
        """Gets the categories of this MetricsMetadata.  # noqa: E501


        :return: The categories of this MetricsMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this MetricsMetadata.


        :param categories: The categories of this MetricsMetadata.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def data_format(self):
        """Gets the data_format of this MetricsMetadata.  # noqa: E501


        :return: The data_format of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this MetricsMetadata.


        :param data_format: The data_format of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

    @property
    def display_format(self):
        """Gets the display_format of this MetricsMetadata.  # noqa: E501


        :return: The display_format of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._display_format

    @display_format.setter
    def display_format(self, display_format):
        """Sets the display_format of this MetricsMetadata.


        :param display_format: The display_format of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._display_format = display_format

    @property
    def type(self):
        """Gets the type of this MetricsMetadata.  # noqa: E501


        :return: The type of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetricsMetadata.


        :param type: The type of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def last_modified(self):
        """Gets the last_modified of this MetricsMetadata.  # noqa: E501


        :return: The last_modified of this MetricsMetadata.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this MetricsMetadata.


        :param last_modified: The last_modified of this MetricsMetadata.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def period_type_default(self):
        """Gets the period_type_default of this MetricsMetadata.  # noqa: E501


        :return: The period_type_default of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._period_type_default

    @period_type_default.setter
    def period_type_default(self, period_type_default):
        """Sets the period_type_default of this MetricsMetadata.


        :param period_type_default: The period_type_default of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._period_type_default = period_type_default

    @property
    def remarks(self):
        """Gets the remarks of this MetricsMetadata.  # noqa: E501


        :return: The remarks of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this MetricsMetadata.


        :param remarks: The remarks of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._remarks = remarks

    @property
    def screening_conditions(self):
        """Gets the screening_conditions of this MetricsMetadata.  # noqa: E501


        :return: The screening_conditions of this MetricsMetadata.  # noqa: E501
        :rtype: list[ScreeningCondition]
        """
        return self._screening_conditions

    @screening_conditions.setter
    def screening_conditions(self, screening_conditions):
        """Sets the screening_conditions of this MetricsMetadata.


        :param screening_conditions: The screening_conditions of this MetricsMetadata.  # noqa: E501
        :type: list[ScreeningCondition]
        """

        self._screening_conditions = screening_conditions

    @property
    def internal_comment(self):
        """Gets the internal_comment of this MetricsMetadata.  # noqa: E501


        :return: The internal_comment of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._internal_comment

    @internal_comment.setter
    def internal_comment(self, internal_comment):
        """Sets the internal_comment of this MetricsMetadata.


        :param internal_comment: The internal_comment of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._internal_comment = internal_comment

    @property
    def aliases(self):
        """Gets the aliases of this MetricsMetadata.  # noqa: E501


        :return: The aliases of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this MetricsMetadata.


        :param aliases: The aliases of this MetricsMetadata.  # noqa: E501
        :type: str
        """

        self._aliases = aliases

    @property
    def colorable(self):
        """Gets the colorable of this MetricsMetadata.  # noqa: E501


        :return: The colorable of this MetricsMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._colorable

    @colorable.setter
    def colorable(self, colorable):
        """Sets the colorable of this MetricsMetadata.


        :param colorable: The colorable of this MetricsMetadata.  # noqa: E501
        :type: bool
        """

        self._colorable = colorable

    @property
    def id(self):
        """Gets the id of this MetricsMetadata.  # noqa: E501


        :return: The id of this MetricsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetricsMetadata.


        :param id: The id of this MetricsMetadata.  # noqa: E501
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
        if issubclass(MetricsMetadata, dict):
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
        if not isinstance(other, MetricsMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
