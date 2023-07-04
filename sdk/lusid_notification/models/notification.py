# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.762-2
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


class Notification(object):
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
        'notification_type': 'NotificationTypeResponse',
        'created_at': 'datetime',
        'user_id_created': 'str',
        'modified_at': 'datetime',
        'user_id_modified': 'str',
        'href': 'str'
    }

    attribute_map = {
        'notification_id': 'notificationId',
        'display_name': 'displayName',
        'description': 'description',
        'notification_type': 'notificationType',
        'created_at': 'createdAt',
        'user_id_created': 'userIdCreated',
        'modified_at': 'modifiedAt',
        'user_id_modified': 'userIdModified',
        'href': 'href'
    }

    required_map = {
        'notification_id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'notification_type': 'required',
        'created_at': 'required',
        'user_id_created': 'required',
        'modified_at': 'required',
        'user_id_modified': 'required',
        'href': 'optional'
    }

    def __init__(self, notification_id=None, display_name=None, description=None, notification_type=None, created_at=None, user_id_created=None, modified_at=None, user_id_modified=None, href=None, local_vars_configuration=None):  # noqa: E501
        """Notification - a model defined in OpenAPI"
        
        :param notification_id:  The identifier of the notification (required)
        :type notification_id: str
        :param display_name:  The name of the notification (required)
        :type display_name: str
        :param description:  The summary of the services provided by the notification
        :type description: str
        :param notification_type:  (required)
        :type notification_type: lusid_notification.NotificationTypeResponse
        :param created_at:  The time at which the subscription was made (required)
        :type created_at: datetime
        :param user_id_created:  The user who made the subscription (required)
        :type user_id_created: str
        :param modified_at:  The time at which the subscription was last modified (required)
        :type modified_at: datetime
        :param user_id_modified:  The user who last modified the subscription (required)
        :type user_id_modified: str
        :param href:  A URI for retrieving this notification
        :type href: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._notification_id = None
        self._display_name = None
        self._description = None
        self._notification_type = None
        self._created_at = None
        self._user_id_created = None
        self._modified_at = None
        self._user_id_modified = None
        self._href = None
        self.discriminator = None

        self.notification_id = notification_id
        self.display_name = display_name
        self.description = description
        self.notification_type = notification_type
        self.created_at = created_at
        self.user_id_created = user_id_created
        self.modified_at = modified_at
        self.user_id_modified = user_id_modified
        self.href = href

    @property
    def notification_id(self):
        """Gets the notification_id of this Notification.  # noqa: E501

        The identifier of the notification  # noqa: E501

        :return: The notification_id of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this Notification.

        The identifier of the notification  # noqa: E501

        :param notification_id: The notification_id of this Notification.  # noqa: E501
        :type notification_id: str
        """
        if self.local_vars_configuration.client_side_validation and notification_id is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                notification_id is not None and len(notification_id) < 1):
            raise ValueError("Invalid value for `notification_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._notification_id = notification_id

    @property
    def display_name(self):
        """Gets the display_name of this Notification.  # noqa: E501

        The name of the notification  # noqa: E501

        :return: The display_name of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Notification.

        The name of the notification  # noqa: E501

        :param display_name: The display_name of this Notification.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
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
        """Gets the description of this Notification.  # noqa: E501

        The summary of the services provided by the notification  # noqa: E501

        :return: The description of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Notification.

        The summary of the services provided by the notification  # noqa: E501

        :param description: The description of this Notification.  # noqa: E501
        :type description: str
        """
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
        """Gets the notification_type of this Notification.  # noqa: E501


        :return: The notification_type of this Notification.  # noqa: E501
        :rtype: lusid_notification.NotificationTypeResponse
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this Notification.


        :param notification_type: The notification_type of this Notification.  # noqa: E501
        :type notification_type: lusid_notification.NotificationTypeResponse
        """
        if self.local_vars_configuration.client_side_validation and notification_type is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def created_at(self):
        """Gets the created_at of this Notification.  # noqa: E501

        The time at which the subscription was made  # noqa: E501

        :return: The created_at of this Notification.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Notification.

        The time at which the subscription was made  # noqa: E501

        :param created_at: The created_at of this Notification.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def user_id_created(self):
        """Gets the user_id_created of this Notification.  # noqa: E501

        The user who made the subscription  # noqa: E501

        :return: The user_id_created of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._user_id_created

    @user_id_created.setter
    def user_id_created(self, user_id_created):
        """Sets the user_id_created of this Notification.

        The user who made the subscription  # noqa: E501

        :param user_id_created: The user_id_created of this Notification.  # noqa: E501
        :type user_id_created: str
        """
        if self.local_vars_configuration.client_side_validation and user_id_created is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id_created`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id_created is not None and len(user_id_created) < 1):
            raise ValueError("Invalid value for `user_id_created`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_id_created = user_id_created

    @property
    def modified_at(self):
        """Gets the modified_at of this Notification.  # noqa: E501

        The time at which the subscription was last modified  # noqa: E501

        :return: The modified_at of this Notification.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Notification.

        The time at which the subscription was last modified  # noqa: E501

        :param modified_at: The modified_at of this Notification.  # noqa: E501
        :type modified_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def user_id_modified(self):
        """Gets the user_id_modified of this Notification.  # noqa: E501

        The user who last modified the subscription  # noqa: E501

        :return: The user_id_modified of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._user_id_modified

    @user_id_modified.setter
    def user_id_modified(self, user_id_modified):
        """Sets the user_id_modified of this Notification.

        The user who last modified the subscription  # noqa: E501

        :param user_id_modified: The user_id_modified of this Notification.  # noqa: E501
        :type user_id_modified: str
        """
        if self.local_vars_configuration.client_side_validation and user_id_modified is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id_modified`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id_modified is not None and len(user_id_modified) < 1):
            raise ValueError("Invalid value for `user_id_modified`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_id_modified = user_id_modified

    @property
    def href(self):
        """Gets the href of this Notification.  # noqa: E501

        A URI for retrieving this notification  # noqa: E501

        :return: The href of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Notification.

        A URI for retrieving this notification  # noqa: E501

        :param href: The href of this Notification.  # noqa: E501
        :type href: str
        """

        self._href = href

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
        if not isinstance(other, Notification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Notification):
            return True

        return self.to_dict() != other.to_dict()
