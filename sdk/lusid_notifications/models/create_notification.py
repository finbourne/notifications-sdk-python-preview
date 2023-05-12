# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.679-2
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


class CreateNotification(object):
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
        'notification_id': 'str',
        'display_name': 'str',
        'description': 'str',
        'notification_type': 'str',
        'notification_content': 'object'
    }

    attribute_map = {
        'notification_id': 'notificationId',
        'display_name': 'displayName',
        'description': 'description',
        'notification_type': 'notificationType',
        'notification_content': 'notificationContent'
    }

    required_map = {
        'notification_id': 'required',
        'display_name': 'optional',
        'description': 'required',
        'notification_type': 'required',
        'notification_content': 'required'
    }

    def __init__(self, notification_id=None, display_name=None, description=None, notification_type=None, notification_content=None, local_vars_configuration=None):  # noqa: E501
        """CreateNotification - a model defined in OpenAPI"
        
        :param notification_id:  The identifier of the notification. (required)
        :type notification_id: str
        :param display_name:  The name of the notification
        :type display_name: str
        :param description:  The summary of the services provided by the notification (required)
        :type description: str
        :param notification_type:  The type of notification (required)
        :type notification_type: str
        :param notification_content:  The contents of the notification. (required)
        :type notification_content: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._notification_id = None
        self._display_name = None
        self._description = None
        self._notification_type = None
        self._notification_content = None
        self.discriminator = None

        self.notification_id = notification_id
        self.display_name = display_name
        self.description = description
        self.notification_type = notification_type
        self.notification_content = notification_content

    @property
    def notification_id(self):
        """Gets the notification_id of this CreateNotification.  # noqa: E501

        The identifier of the notification.  # noqa: E501

        :return: The notification_id of this CreateNotification.  # noqa: E501
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this CreateNotification.

        The identifier of the notification.  # noqa: E501

        :param notification_id: The notification_id of this CreateNotification.  # noqa: E501
        :type notification_id: str
        """
        if self.local_vars_configuration.client_side_validation and notification_id is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                notification_id is not None and len(notification_id) > 100):
            raise ValueError("Invalid value for `notification_id`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                notification_id is not None and len(notification_id) < 1):
            raise ValueError("Invalid value for `notification_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                notification_id is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', notification_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `notification_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._notification_id = notification_id

    @property
    def display_name(self):
        """Gets the display_name of this CreateNotification.  # noqa: E501

        The name of the notification  # noqa: E501

        :return: The display_name of this CreateNotification.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateNotification.

        The name of the notification  # noqa: E501

        :param display_name: The display_name of this CreateNotification.  # noqa: E501
        :type display_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 64):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 0):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CreateNotification.  # noqa: E501

        The summary of the services provided by the notification  # noqa: E501

        :return: The description of this CreateNotification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNotification.

        The summary of the services provided by the notification  # noqa: E501

        :param description: The description of this CreateNotification.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 512):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def notification_type(self):
        """Gets the notification_type of this CreateNotification.  # noqa: E501

        The type of notification  # noqa: E501

        :return: The notification_type of this CreateNotification.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this CreateNotification.

        The type of notification  # noqa: E501

        :param notification_type: The notification_type of this CreateNotification.  # noqa: E501
        :type notification_type: str
        """
        if self.local_vars_configuration.client_side_validation and notification_type is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                notification_type is not None and len(notification_type) < 1):
            raise ValueError("Invalid value for `notification_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def notification_content(self):
        """Gets the notification_content of this CreateNotification.  # noqa: E501

        The contents of the notification.  # noqa: E501

        :return: The notification_content of this CreateNotification.  # noqa: E501
        :rtype: object
        """
        return self._notification_content

    @notification_content.setter
    def notification_content(self, notification_content):
        """Sets the notification_content of this CreateNotification.

        The contents of the notification.  # noqa: E501

        :param notification_content: The notification_content of this CreateNotification.  # noqa: E501
        :type notification_content: object
        """

        self._notification_content = notification_content

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
        if not isinstance(other, CreateNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateNotification):
            return True

        return self.to_dict() != other.to_dict()
