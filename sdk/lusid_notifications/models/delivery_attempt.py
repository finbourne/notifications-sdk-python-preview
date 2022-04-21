# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.300
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


class DeliveryAttempt(object):
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
        'attempt_number': 'int',
        'attempted_time': 'datetime',
        'attempt_status': 'AttemptStatus'
    }

    attribute_map = {
        'attempt_number': 'attemptNumber',
        'attempted_time': 'attemptedTime',
        'attempt_status': 'attemptStatus'
    }

    required_map = {
        'attempt_number': 'required',
        'attempted_time': 'required',
        'attempt_status': 'required'
    }

    def __init__(self, attempt_number=None, attempted_time=None, attempt_status=None, local_vars_configuration=None):  # noqa: E501
        """DeliveryAttempt - a model defined in OpenAPI"
        
        :param attempt_number:  The total number of attempts made immediately after this delivery attempt (required)
        :type attempt_number: int
        :param attempted_time:  The time that the delivery was attempted (required)
        :type attempted_time: datetime
        :param attempt_status:  (required)
        :type attempt_status: lusid_notifications.AttemptStatus

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._attempt_number = None
        self._attempted_time = None
        self._attempt_status = None
        self.discriminator = None

        self.attempt_number = attempt_number
        self.attempted_time = attempted_time
        self.attempt_status = attempt_status

    @property
    def attempt_number(self):
        """Gets the attempt_number of this DeliveryAttempt.  # noqa: E501

        The total number of attempts made immediately after this delivery attempt  # noqa: E501

        :return: The attempt_number of this DeliveryAttempt.  # noqa: E501
        :rtype: int
        """
        return self._attempt_number

    @attempt_number.setter
    def attempt_number(self, attempt_number):
        """Sets the attempt_number of this DeliveryAttempt.

        The total number of attempts made immediately after this delivery attempt  # noqa: E501

        :param attempt_number: The attempt_number of this DeliveryAttempt.  # noqa: E501
        :type attempt_number: int
        """
        if self.local_vars_configuration.client_side_validation and attempt_number is None:  # noqa: E501
            raise ValueError("Invalid value for `attempt_number`, must not be `None`")  # noqa: E501

        self._attempt_number = attempt_number

    @property
    def attempted_time(self):
        """Gets the attempted_time of this DeliveryAttempt.  # noqa: E501

        The time that the delivery was attempted  # noqa: E501

        :return: The attempted_time of this DeliveryAttempt.  # noqa: E501
        :rtype: datetime
        """
        return self._attempted_time

    @attempted_time.setter
    def attempted_time(self, attempted_time):
        """Sets the attempted_time of this DeliveryAttempt.

        The time that the delivery was attempted  # noqa: E501

        :param attempted_time: The attempted_time of this DeliveryAttempt.  # noqa: E501
        :type attempted_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and attempted_time is None:  # noqa: E501
            raise ValueError("Invalid value for `attempted_time`, must not be `None`")  # noqa: E501

        self._attempted_time = attempted_time

    @property
    def attempt_status(self):
        """Gets the attempt_status of this DeliveryAttempt.  # noqa: E501


        :return: The attempt_status of this DeliveryAttempt.  # noqa: E501
        :rtype: lusid_notifications.AttemptStatus
        """
        return self._attempt_status

    @attempt_status.setter
    def attempt_status(self, attempt_status):
        """Sets the attempt_status of this DeliveryAttempt.


        :param attempt_status: The attempt_status of this DeliveryAttempt.  # noqa: E501
        :type attempt_status: lusid_notifications.AttemptStatus
        """
        if self.local_vars_configuration.client_side_validation and attempt_status is None:  # noqa: E501
            raise ValueError("Invalid value for `attempt_status`, must not be `None`")  # noqa: E501

        self._attempt_status = attempt_status

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
        if not isinstance(other, DeliveryAttempt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeliveryAttempt):
            return True

        return self.to_dict() != other.to_dict()
