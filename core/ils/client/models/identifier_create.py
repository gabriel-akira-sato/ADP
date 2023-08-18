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

class IdentifierCreate(object):
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
        'code': 'str',
        'salt': 'str',
        'type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'salt': 'salt',
        'type': 'type'
    }

    def __init__(self, code=None, salt=None, type=None):  # noqa: E501
        """IdentifierCreate - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._salt = None
        self._type = None
        self.discriminator = None
        self.code = code
        if salt is not None:
            self.salt = salt
        self.type = type

    @property
    def code(self):
        """Gets the code of this IdentifierCreate.  # noqa: E501

        Code of the identifier (e.g dataMatrix, Barcode, RFID Tag uid)  # noqa: E501

        :return: The code of this IdentifierCreate.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this IdentifierCreate.

        Code of the identifier (e.g dataMatrix, Barcode, RFID Tag uid)  # noqa: E501

        :param code: The code of this IdentifierCreate.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def salt(self):
        """Gets the salt of this IdentifierCreate.  # noqa: E501

        (Optional) Can be either empty or any value to represent a scope of values that would result in unique values, even if provided the same code  # noqa: E501

        :return: The salt of this IdentifierCreate.  # noqa: E501
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """Sets the salt of this IdentifierCreate.

        (Optional) Can be either empty or any value to represent a scope of values that would result in unique values, even if provided the same code  # noqa: E501

        :param salt: The salt of this IdentifierCreate.  # noqa: E501
        :type: str
        """

        self._salt = salt

    @property
    def type(self):
        """Gets the type of this IdentifierCreate.  # noqa: E501

        The type of the Identifier. Use CODE when targeting the value of a barcode or rfid tag, and use DEVICE when targeting for example the id or MAC address of a physical device  # noqa: E501

        :return: The type of this IdentifierCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentifierCreate.

        The type of the Identifier. Use CODE when targeting the value of a barcode or rfid tag, and use DEVICE when targeting for example the id or MAC address of a physical device  # noqa: E501

        :param type: The type of this IdentifierCreate.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["CODE", "DEVICE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(IdentifierCreate, dict):
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
        if not isinstance(other, IdentifierCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other