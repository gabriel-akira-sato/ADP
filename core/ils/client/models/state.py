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

class State(object):
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
        'present': 'bool',
        'read_time': 'datetime'
    }

    attribute_map = {
        'present': 'present',
        'read_time': 'readTime'
    }

    def __init__(self, present=None, read_time=None):  # noqa: E501
        """State - a model defined in Swagger"""  # noqa: E501
        self._present = None
        self._read_time = None
        self.discriminator = None
        if present is not None:
            self.present = present
        if read_time is not None:
            self.read_time = read_time

    @property
    def present(self):
        """Gets the present of this State.  # noqa: E501


        :return: The present of this State.  # noqa: E501
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """Sets the present of this State.


        :param present: The present of this State.  # noqa: E501
        :type: bool
        """

        self._present = present

    @property
    def read_time(self):
        """Gets the read_time of this State.  # noqa: E501


        :return: The read_time of this State.  # noqa: E501
        :rtype: datetime
        """
        return self._read_time

    @read_time.setter
    def read_time(self, read_time):
        """Sets the read_time of this State.


        :param read_time: The read_time of this State.  # noqa: E501
        :type: datetime
        """

        self._read_time = read_time

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
        if issubclass(State, dict):
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
        if not isinstance(other, State):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other