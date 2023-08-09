# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.820
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


class MatchingPattern(object):
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
        'filter': 'str'
    }

    attribute_map = {
        'event_type': 'eventType',
        'filter': 'filter'
    }

    required_map = {
        'event_type': 'required',
        'filter': 'optional'
    }

    def __init__(self, event_type=None, filter=None, local_vars_configuration=None):  # noqa: E501
        """MatchingPattern - a model defined in OpenAPI"
        
        :param event_type:  The type of event to subscribe to. The list of available event types can be discovered  by calling the ‘List available EventTypes’ API endpoint. (required)
        :type event_type: str
        :param filter:  A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched
        :type filter: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._filter = None
        self.discriminator = None

        self.event_type = event_type
        self.filter = filter

    @property
    def event_type(self):
        """Gets the event_type of this MatchingPattern.  # noqa: E501

        The type of event to subscribe to. The list of available event types can be discovered  by calling the ‘List available EventTypes’ API endpoint.  # noqa: E501

        :return: The event_type of this MatchingPattern.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this MatchingPattern.

        The type of event to subscribe to. The list of available event types can be discovered  by calling the ‘List available EventTypes’ API endpoint.  # noqa: E501

        :param event_type: The event_type of this MatchingPattern.  # noqa: E501
        :type event_type: str
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                event_type is not None and len(event_type) > 512):
            raise ValueError("Invalid value for `event_type`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                event_type is not None and len(event_type) < 0):
            raise ValueError("Invalid value for `event_type`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                event_type is not None and not re.search(r'^[a-zA-Z]*$', event_type)):  # noqa: E501
            raise ValueError(r"Invalid value for `event_type`, must be a follow pattern or equal to `/^[a-zA-Z]*$/`")  # noqa: E501

        self._event_type = event_type

    @property
    def filter(self):
        """Gets the filter of this MatchingPattern.  # noqa: E501

        A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched  # noqa: E501

        :return: The filter of this MatchingPattern.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this MatchingPattern.

        A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched  # noqa: E501

        :param filter: The filter of this MatchingPattern.  # noqa: E501
        :type filter: str
        """
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and len(filter) > 16384):
            raise ValueError("Invalid value for `filter`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and len(filter) < 0):
            raise ValueError("Invalid value for `filter`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and not re.search(r'^[\s\S]*$', filter)):  # noqa: E501
            raise ValueError(r"Invalid value for `filter`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._filter = filter

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
        if not isinstance(other, MatchingPattern):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchingPattern):
            return True

        return self.to_dict() != other.to_dict()
