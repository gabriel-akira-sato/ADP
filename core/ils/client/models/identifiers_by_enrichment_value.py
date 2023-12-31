# coding: utf-8

"""
    ILS API Documentation

    Neoception® Intralogistics Suite is a collection of modules for automation in the context of manufacturing.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@neoception.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IdentifiersByEnrichmentValue(object):
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
        'value': 'str',
        'identifiers': 'list[Identifier]'
    }

    attribute_map = {
        'value': 'value',
        'identifiers': 'identifiers'
    }

    def __init__(self, value=None, identifiers=None):  # noqa: E501
        """IdentifiersByEnrichmentValue - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._identifiers = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if identifiers is not None:
            self.identifiers = identifiers

    @property
    def value(self):
        """Gets the value of this IdentifiersByEnrichmentValue.  # noqa: E501


        :return: The value of this IdentifiersByEnrichmentValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IdentifiersByEnrichmentValue.


        :param value: The value of this IdentifiersByEnrichmentValue.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def identifiers(self):
        """Gets the identifiers of this IdentifiersByEnrichmentValue.  # noqa: E501


        :return: The identifiers of this IdentifiersByEnrichmentValue.  # noqa: E501
        :rtype: list[Identifier]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this IdentifiersByEnrichmentValue.


        :param identifiers: The identifiers of this IdentifiersByEnrichmentValue.  # noqa: E501
        :type: list[Identifier]
        """

        self._identifiers = identifiers

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
        if issubclass(IdentifiersByEnrichmentValue, dict):
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
        if not isinstance(other, IdentifiersByEnrichmentValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
