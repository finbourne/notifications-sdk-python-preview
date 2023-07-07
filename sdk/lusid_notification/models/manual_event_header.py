# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.775
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

from lusid_notification.configuration import Configuration


class ManualEventHeader(object):
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
        'event_type': 'str',
        'timestamp': 'datetime',
        'user_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'event_type': 'eventType',
        'timestamp': 'timestamp',
        'user_id': 'userId',
        'request_id': 'requestId'
    }

    required_map = {
        'event_type': 'optional',
        'timestamp': 'optional',
        'user_id': 'optional',
        'request_id': 'optional'
    }

    def __init__(self, event_type=None, timestamp=None, user_id=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """ManualEventHeader - a model defined in OpenAPI"
        
        :param event_type:  The event type of the manual event
        :type event_type: str
        :param timestamp:  The timestamp of the manual event
        :type timestamp: datetime
        :param user_id:  The user ID of the manual event
        :type user_id: str
        :param request_id:  The request ID of the manual event
        :type request_id: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._timestamp = None
        self._user_id = None
        self._request_id = None
        self.discriminator = None

        self.event_type = event_type
        if timestamp is not None:
            self.timestamp = timestamp
        self.user_id = user_id
        self.request_id = request_id

    @property
    def event_type(self):
        """Gets the event_type of this ManualEventHeader.  # noqa: E501

        The event type of the manual event  # noqa: E501

        :return: The event_type of this ManualEventHeader.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ManualEventHeader.

        The event type of the manual event  # noqa: E501

        :param event_type: The event_type of this ManualEventHeader.  # noqa: E501
        :type event_type: str
        """

        self._event_type = event_type

    @property
    def timestamp(self):
        """Gets the timestamp of this ManualEventHeader.  # noqa: E501

        The timestamp of the manual event  # noqa: E501

        :return: The timestamp of this ManualEventHeader.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ManualEventHeader.

        The timestamp of the manual event  # noqa: E501

        :param timestamp: The timestamp of this ManualEventHeader.  # noqa: E501
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def user_id(self):
        """Gets the user_id of this ManualEventHeader.  # noqa: E501

        The user ID of the manual event  # noqa: E501

        :return: The user_id of this ManualEventHeader.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ManualEventHeader.

        The user ID of the manual event  # noqa: E501

        :param user_id: The user_id of this ManualEventHeader.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def request_id(self):
        """Gets the request_id of this ManualEventHeader.  # noqa: E501

        The request ID of the manual event  # noqa: E501

        :return: The request_id of this ManualEventHeader.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ManualEventHeader.

        The request ID of the manual event  # noqa: E501

        :param request_id: The request_id of this ManualEventHeader.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

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
        if not isinstance(other, ManualEventHeader):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManualEventHeader):
            return True

        return self.to_dict() != other.to_dict()
