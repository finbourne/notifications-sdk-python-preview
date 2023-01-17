# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.525
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_notifications.configuration import Configuration


class NotificationStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'result': 'str',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'result': 'result',
        'last_updated': 'lastUpdated'
    }

    required_map = {
        'result': 'optional',
        'last_updated': 'optional'
    }

    def __init__(self, result=None, last_updated=None, local_vars_configuration=None):  # noqa: E501
        """NotificationStatus - a model defined in OpenAPI"
        
        :param result:  The status of the notification
        :type result: str
        :param last_updated:  The time at which the notification status was last updated
        :type last_updated: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._last_updated = None
        self.discriminator = None

        self.result = result
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def result(self):
        """Gets the result of this NotificationStatus.  # noqa: E501

        The status of the notification  # noqa: E501

        :return: The result of this NotificationStatus.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this NotificationStatus.

        The status of the notification  # noqa: E501

        :param result: The result of this NotificationStatus.  # noqa: E501
        :type result: str
        """

        self._result = result

    @property
    def last_updated(self):
        """Gets the last_updated of this NotificationStatus.  # noqa: E501

        The time at which the notification status was last updated  # noqa: E501

        :return: The last_updated of this NotificationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this NotificationStatus.

        The time at which the notification status was last updated  # noqa: E501

        :param last_updated: The last_updated of this NotificationStatus.  # noqa: E501
        :type last_updated: datetime
        """

        self._last_updated = last_updated

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationStatus):
            return True

        return self.to_dict() != other.to_dict()
