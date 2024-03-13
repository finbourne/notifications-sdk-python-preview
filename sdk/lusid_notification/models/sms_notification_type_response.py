# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.919
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


class SmsNotificationTypeResponse(object):
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
        'type': 'str',
        'body': 'str',
        'recipients': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'body': 'body',
        'recipients': 'recipients'
    }

    required_map = {
        'type': 'optional',
        'body': 'optional',
        'recipients': 'optional'
    }

    def __init__(self, type=None, body=None, recipients=None, local_vars_configuration=None):  # noqa: E501
        """SmsNotificationTypeResponse - a model defined in OpenAPI"
        
        :param type:  The type of delivery mechanism for this notification
        :type type: str
        :param body:  The body of the SMS
        :type body: str
        :param recipients:  The phone numbers to which the SMS will be sent to (E.164 format)
        :type recipients: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._body = None
        self._recipients = None
        self.discriminator = None

        self.type = type
        self.body = body
        self.recipients = recipients

    @property
    def type(self):
        """Gets the type of this SmsNotificationTypeResponse.  # noqa: E501

        The type of delivery mechanism for this notification  # noqa: E501

        :return: The type of this SmsNotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SmsNotificationTypeResponse.

        The type of delivery mechanism for this notification  # noqa: E501

        :param type: The type of this SmsNotificationTypeResponse.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def body(self):
        """Gets the body of this SmsNotificationTypeResponse.  # noqa: E501

        The body of the SMS  # noqa: E501

        :return: The body of this SmsNotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SmsNotificationTypeResponse.

        The body of the SMS  # noqa: E501

        :param body: The body of this SmsNotificationTypeResponse.  # noqa: E501
        :type body: str
        """

        self._body = body

    @property
    def recipients(self):
        """Gets the recipients of this SmsNotificationTypeResponse.  # noqa: E501

        The phone numbers to which the SMS will be sent to (E.164 format)  # noqa: E501

        :return: The recipients of this SmsNotificationTypeResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this SmsNotificationTypeResponse.

        The phone numbers to which the SMS will be sent to (E.164 format)  # noqa: E501

        :param recipients: The recipients of this SmsNotificationTypeResponse.  # noqa: E501
        :type recipients: list[str]
        """

        self._recipients = recipients

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
        if not isinstance(other, SmsNotificationTypeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmsNotificationTypeResponse):
            return True

        return self.to_dict() != other.to_dict()
