# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.772.7
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


class Subscription(object):
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
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'status': 'str',
        'matching_pattern': 'MatchingPattern',
        'created_at': 'datetime',
        'user_id_created': 'str',
        'modified_at': 'datetime',
        'user_id_modified': 'str',
        'use_as_auth': 'str',
        'href': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'status': 'status',
        'matching_pattern': 'matchingPattern',
        'created_at': 'createdAt',
        'user_id_created': 'userIdCreated',
        'modified_at': 'modifiedAt',
        'user_id_modified': 'userIdModified',
        'use_as_auth': 'useAsAuth',
        'href': 'href'
    }

    required_map = {
        'id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'status': 'required',
        'matching_pattern': 'required',
        'created_at': 'required',
        'user_id_created': 'required',
        'modified_at': 'required',
        'user_id_modified': 'required',
        'use_as_auth': 'required',
        'href': 'optional'
    }

    def __init__(self, id=None, display_name=None, description=None, status=None, matching_pattern=None, created_at=None, user_id_created=None, modified_at=None, user_id_modified=None, use_as_auth=None, href=None, local_vars_configuration=None):  # noqa: E501
        """Subscription - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid_notification.ResourceId
        :param display_name:  The name of the subscription (required)
        :type display_name: str
        :param description:  The summary of the services provided by the subscription
        :type description: str
        :param status:  The current status of the subscription (required)
        :type status: str
        :param matching_pattern:  (required)
        :type matching_pattern: lusid_notification.MatchingPattern
        :param created_at:  The time at which the subscription was made (required)
        :type created_at: datetime
        :param user_id_created:  The user who made the subscription (required)
        :type user_id_created: str
        :param modified_at:  The time at which the subscription was last modified (required)
        :type modified_at: datetime
        :param user_id_modified:  The user who last modified the subscription (required)
        :type user_id_modified: str
        :param use_as_auth:  The user to use as auth for the subscription (required)
        :type use_as_auth: str
        :param href:  A URI for retrieving this subscription
        :type href: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._description = None
        self._status = None
        self._matching_pattern = None
        self._created_at = None
        self._user_id_created = None
        self._modified_at = None
        self._user_id_modified = None
        self._use_as_auth = None
        self._href = None
        self.discriminator = None

        self.id = id
        self.display_name = display_name
        self.description = description
        self.status = status
        self.matching_pattern = matching_pattern
        self.created_at = created_at
        self.user_id_created = user_id_created
        self.modified_at = modified_at
        self.user_id_modified = user_id_modified
        self.use_as_auth = use_as_auth
        self.href = href

    @property
    def id(self):
        """Gets the id of this Subscription.  # noqa: E501


        :return: The id of this Subscription.  # noqa: E501
        :rtype: lusid_notification.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.


        :param id: The id of this Subscription.  # noqa: E501
        :type id: lusid_notification.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this Subscription.  # noqa: E501

        The name of the subscription  # noqa: E501

        :return: The display_name of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Subscription.

        The name of the subscription  # noqa: E501

        :param display_name: The display_name of this Subscription.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Subscription.  # noqa: E501

        The summary of the services provided by the subscription  # noqa: E501

        :return: The description of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subscription.

        The summary of the services provided by the subscription  # noqa: E501

        :param description: The description of this Subscription.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Subscription.  # noqa: E501

        The current status of the subscription  # noqa: E501

        :return: The status of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Subscription.

        The current status of the subscription  # noqa: E501

        :param status: The status of this Subscription.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def matching_pattern(self):
        """Gets the matching_pattern of this Subscription.  # noqa: E501


        :return: The matching_pattern of this Subscription.  # noqa: E501
        :rtype: lusid_notification.MatchingPattern
        """
        return self._matching_pattern

    @matching_pattern.setter
    def matching_pattern(self, matching_pattern):
        """Sets the matching_pattern of this Subscription.


        :param matching_pattern: The matching_pattern of this Subscription.  # noqa: E501
        :type matching_pattern: lusid_notification.MatchingPattern
        """
        if self.local_vars_configuration.client_side_validation and matching_pattern is None:  # noqa: E501
            raise ValueError("Invalid value for `matching_pattern`, must not be `None`")  # noqa: E501

        self._matching_pattern = matching_pattern

    @property
    def created_at(self):
        """Gets the created_at of this Subscription.  # noqa: E501

        The time at which the subscription was made  # noqa: E501

        :return: The created_at of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Subscription.

        The time at which the subscription was made  # noqa: E501

        :param created_at: The created_at of this Subscription.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def user_id_created(self):
        """Gets the user_id_created of this Subscription.  # noqa: E501

        The user who made the subscription  # noqa: E501

        :return: The user_id_created of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._user_id_created

    @user_id_created.setter
    def user_id_created(self, user_id_created):
        """Sets the user_id_created of this Subscription.

        The user who made the subscription  # noqa: E501

        :param user_id_created: The user_id_created of this Subscription.  # noqa: E501
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
        """Gets the modified_at of this Subscription.  # noqa: E501

        The time at which the subscription was last modified  # noqa: E501

        :return: The modified_at of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Subscription.

        The time at which the subscription was last modified  # noqa: E501

        :param modified_at: The modified_at of this Subscription.  # noqa: E501
        :type modified_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def user_id_modified(self):
        """Gets the user_id_modified of this Subscription.  # noqa: E501

        The user who last modified the subscription  # noqa: E501

        :return: The user_id_modified of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._user_id_modified

    @user_id_modified.setter
    def user_id_modified(self, user_id_modified):
        """Sets the user_id_modified of this Subscription.

        The user who last modified the subscription  # noqa: E501

        :param user_id_modified: The user_id_modified of this Subscription.  # noqa: E501
        :type user_id_modified: str
        """
        if self.local_vars_configuration.client_side_validation and user_id_modified is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id_modified`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id_modified is not None and len(user_id_modified) < 1):
            raise ValueError("Invalid value for `user_id_modified`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_id_modified = user_id_modified

    @property
    def use_as_auth(self):
        """Gets the use_as_auth of this Subscription.  # noqa: E501

        The user to use as auth for the subscription  # noqa: E501

        :return: The use_as_auth of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._use_as_auth

    @use_as_auth.setter
    def use_as_auth(self, use_as_auth):
        """Sets the use_as_auth of this Subscription.

        The user to use as auth for the subscription  # noqa: E501

        :param use_as_auth: The use_as_auth of this Subscription.  # noqa: E501
        :type use_as_auth: str
        """
        if self.local_vars_configuration.client_side_validation and use_as_auth is None:  # noqa: E501
            raise ValueError("Invalid value for `use_as_auth`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                use_as_auth is not None and len(use_as_auth) < 1):
            raise ValueError("Invalid value for `use_as_auth`, length must be greater than or equal to `1`")  # noqa: E501

        self._use_as_auth = use_as_auth

    @property
    def href(self):
        """Gets the href of this Subscription.  # noqa: E501

        A URI for retrieving this subscription  # noqa: E501

        :return: The href of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Subscription.

        A URI for retrieving this subscription  # noqa: E501

        :param href: The href of this Subscription.  # noqa: E501
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
        if not isinstance(other, Subscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Subscription):
            return True

        return self.to_dict() != other.to_dict()
