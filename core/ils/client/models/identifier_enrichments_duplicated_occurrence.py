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

class IdentifierEnrichmentsDuplicatedOccurrence(object):
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
        'enrichment_key': 'str',
        'occurrences': 'list[IdentifiersByEnrichmentValue]'
    }

    attribute_map = {
        'enrichment_key': 'enrichmentKey',
        'occurrences': 'occurrences'
    }

    def __init__(self, enrichment_key=None, occurrences=None):  # noqa: E501
        """IdentifierEnrichmentsDuplicatedOccurrence - a model defined in Swagger"""  # noqa: E501
        self._enrichment_key = None
        self._occurrences = None
        self.discriminator = None
        if enrichment_key is not None:
            self.enrichment_key = enrichment_key
        if occurrences is not None:
            self.occurrences = occurrences

    @property
    def enrichment_key(self):
        """Gets the enrichment_key of this IdentifierEnrichmentsDuplicatedOccurrence.  # noqa: E501


        :return: The enrichment_key of this IdentifierEnrichmentsDuplicatedOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._enrichment_key

    @enrichment_key.setter
    def enrichment_key(self, enrichment_key):
        """Sets the enrichment_key of this IdentifierEnrichmentsDuplicatedOccurrence.


        :param enrichment_key: The enrichment_key of this IdentifierEnrichmentsDuplicatedOccurrence.  # noqa: E501
        :type: str
        """

        self._enrichment_key = enrichment_key

    @property
    def occurrences(self):
        """Gets the occurrences of this IdentifierEnrichmentsDuplicatedOccurrence.  # noqa: E501


        :return: The occurrences of this IdentifierEnrichmentsDuplicatedOccurrence.  # noqa: E501
        :rtype: list[IdentifiersByEnrichmentValue]
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this IdentifierEnrichmentsDuplicatedOccurrence.


        :param occurrences: The occurrences of this IdentifierEnrichmentsDuplicatedOccurrence.  # noqa: E501
        :type: list[IdentifiersByEnrichmentValue]
        """

        self._occurrences = occurrences

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
        if issubclass(IdentifierEnrichmentsDuplicatedOccurrence, dict):
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
        if not isinstance(other, IdentifierEnrichmentsDuplicatedOccurrence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
