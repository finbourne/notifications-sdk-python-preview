# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.921
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
        'id': 'str',
        'display_name': 'str',
        'description': 'str',
        'delivery_channel': 'str',
        'recipients': 'dict(str, object)',
        'content': 'dict(str, object)',
        'status': 'NotificationStatus',
        'created_at': 'datetime',
        'created_by': 'str',
        'last_modified_at': 'datetime',
        'last_modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'delivery_channel': 'deliveryChannel',
        'recipients': 'recipients',
        'content': 'content',
        'status': 'status',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'last_modified_at': 'lastModifiedAt',
        'last_modified_by': 'lastModifiedBy'
    }

    required_map = {
        'id': 'required',
        'display_name': 'optional',
        'description': 'optional',
        'delivery_channel': 'required',
        'recipients': 'required',
        'content': 'required',
        'status': 'optional',
        'created_at': 'required',
        'created_by': 'required',
        'last_modified_at': 'required',
        'last_modified_by': 'required'
    }

    def __init__(self, id=None, display_name=None, description=None, delivery_channel=None, recipients=None, content=None, status=None, created_at=None, created_by=None, last_modified_at=None, last_modified_by=None, local_vars_configuration=None):  # noqa: E501
        """Notification - a model defined in OpenAPI"
        
        :param id:  The identifier of the notification (required)
        :type id: str
        :param display_name:  The name of the notification
        :type display_name: str
        :param description:  The summary of the services provided by the notification
        :type description: str
        :param delivery_channel:  The medium through which the notification is delivered (required)
        :type delivery_channel: str
        :param recipients:  Recipient of the notification (required)
        :type recipients: dict(str, object)
        :param content:  The contents of the notification (required)
        :type content: dict(str, object)
        :param status: 
        :type status: lusid_notifications.NotificationStatus
        :param created_at:  The time at which the subscription was made (required)
        :type created_at: datetime
        :param created_by:  The user who made the subscription (required)
        :type created_by: str
        :param last_modified_at:  The time at which the subscription was last modified (required)
        :type last_modified_at: datetime
        :param last_modified_by:  The user who last modified the subscription (required)
        :type last_modified_by: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._description = None
        self._delivery_channel = None
        self._recipients = None
        self._content = None
        self._status = None
        self._created_at = None
        self._created_by = None
        self._last_modified_at = None
        self._last_modified_by = None
        self.discriminator = None

        self.id = id
        self.display_name = display_name
        self.description = description
        self.delivery_channel = delivery_channel
        self.recipients = recipients
        self.content = content
        if status is not None:
            self.status = status
        self.created_at = created_at
        self.created_by = created_by
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by

    @property
    def id(self):
        """Gets the id of this Notification.  # noqa: E501

        The identifier of the notification  # noqa: E501

        :return: The id of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Notification.

        The identifier of the notification  # noqa: E501

        :param id: The id of this Notification.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

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
    def delivery_channel(self):
        """Gets the delivery_channel of this Notification.  # noqa: E501

        The medium through which the notification is delivered  # noqa: E501

        :return: The delivery_channel of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._delivery_channel

    @delivery_channel.setter
    def delivery_channel(self, delivery_channel):
        """Sets the delivery_channel of this Notification.

        The medium through which the notification is delivered  # noqa: E501

        :param delivery_channel: The delivery_channel of this Notification.  # noqa: E501
        :type delivery_channel: str
        """
        if self.local_vars_configuration.client_side_validation and delivery_channel is None:  # noqa: E501
            raise ValueError("Invalid value for `delivery_channel`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                delivery_channel is not None and len(delivery_channel) < 1):
            raise ValueError("Invalid value for `delivery_channel`, length must be greater than or equal to `1`")  # noqa: E501

        self._delivery_channel = delivery_channel

    @property
    def recipients(self):
        """Gets the recipients of this Notification.  # noqa: E501

        Recipient of the notification  # noqa: E501

        :return: The recipients of this Notification.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this Notification.

        Recipient of the notification  # noqa: E501

        :param recipients: The recipients of this Notification.  # noqa: E501
        :type recipients: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and recipients is None:  # noqa: E501
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def content(self):
        """Gets the content of this Notification.  # noqa: E501

        The contents of the notification  # noqa: E501

        :return: The content of this Notification.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Notification.

        The contents of the notification  # noqa: E501

        :param content: The content of this Notification.  # noqa: E501
        :type content: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def status(self):
        """Gets the status of this Notification.  # noqa: E501


        :return: The status of this Notification.  # noqa: E501
        :rtype: lusid_notifications.NotificationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Notification.


        :param status: The status of this Notification.  # noqa: E501
        :type status: lusid_notifications.NotificationStatus
        """

        self._status = status

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
    def created_by(self):
        """Gets the created_by of this Notification.  # noqa: E501

        The user who made the subscription  # noqa: E501

        :return: The created_by of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Notification.

        The user who made the subscription  # noqa: E501

        :param created_by: The created_by of this Notification.  # noqa: E501
        :type created_by: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                created_by is not None and len(created_by) < 1):
            raise ValueError("Invalid value for `created_by`, length must be greater than or equal to `1`")  # noqa: E501

        self._created_by = created_by

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this Notification.  # noqa: E501

        The time at which the subscription was last modified  # noqa: E501

        :return: The last_modified_at of this Notification.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this Notification.

        The time at which the subscription was last modified  # noqa: E501

        :param last_modified_at: The last_modified_at of this Notification.  # noqa: E501
        :type last_modified_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_at`, must not be `None`")  # noqa: E501

        self._last_modified_at = last_modified_at

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this Notification.  # noqa: E501

        The user who last modified the subscription  # noqa: E501

        :return: The last_modified_by of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this Notification.

        The user who last modified the subscription  # noqa: E501

        :param last_modified_by: The last_modified_by of this Notification.  # noqa: E501
        :type last_modified_by: str
        """
        if self.local_vars_configuration.client_side_validation and last_modified_by is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_by`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_modified_by is not None and len(last_modified_by) < 1):
            raise ValueError("Invalid value for `last_modified_by`, length must be greater than or equal to `1`")  # noqa: E501

        self._last_modified_by = last_modified_by

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
