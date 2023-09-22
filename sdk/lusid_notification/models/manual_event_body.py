# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.864
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


class ManualEventBody(object):
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
        'subject': 'str',
        'message': 'str',
        'json_message': 'object'
    }

    attribute_map = {
        'subject': 'subject',
        'message': 'message',
        'json_message': 'jsonMessage'
    }

    required_map = {
        'subject': 'required',
        'message': 'required',
        'json_message': 'optional'
    }

    def __init__(self, subject=None, message=None, json_message=None, local_vars_configuration=None):  # noqa: E501
        """ManualEventBody - a model defined in OpenAPI"
        
        :param subject:  The subject of the manual event (required)
        :type subject: str
        :param message:  The message of the manual event (required)
        :type message: str
        :param json_message:  The JSON message of the manual event
        :type json_message: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._subject = None
        self._message = None
        self._json_message = None
        self.discriminator = None

        self.subject = subject
        self.message = message
        self.json_message = json_message

    @property
    def subject(self):
        """Gets the subject of this ManualEventBody.  # noqa: E501

        The subject of the manual event  # noqa: E501

        :return: The subject of this ManualEventBody.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ManualEventBody.

        The subject of the manual event  # noqa: E501

        :param subject: The subject of this ManualEventBody.  # noqa: E501
        :type subject: str
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) > 256):
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) < 1):
            raise ValueError("Invalid value for `subject`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and not re.search(r'^[\s\S]*$', subject)):  # noqa: E501
            raise ValueError(r"Invalid value for `subject`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._subject = subject

    @property
    def message(self):
        """Gets the message of this ManualEventBody.  # noqa: E501

        The message of the manual event  # noqa: E501

        :return: The message of this ManualEventBody.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ManualEventBody.

        The message of the manual event  # noqa: E501

        :param message: The message of this ManualEventBody.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) > 2147483647):
            raise ValueError("Invalid value for `message`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) < 1):
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message is not None and not re.search(r'^[\s\S]*$', message)):  # noqa: E501
            raise ValueError(r"Invalid value for `message`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._message = message

    @property
    def json_message(self):
        """Gets the json_message of this ManualEventBody.  # noqa: E501

        The JSON message of the manual event  # noqa: E501

        :return: The json_message of this ManualEventBody.  # noqa: E501
        :rtype: object
        """
        return self._json_message

    @json_message.setter
    def json_message(self, json_message):
        """Sets the json_message of this ManualEventBody.

        The JSON message of the manual event  # noqa: E501

        :param json_message: The json_message of this ManualEventBody.  # noqa: E501
        :type json_message: object
        """

        self._json_message = json_message

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
        if not isinstance(other, ManualEventBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManualEventBody):
            return True

        return self.to_dict() != other.to_dict()
