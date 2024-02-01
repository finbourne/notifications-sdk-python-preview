# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.912
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


class UpdateAwsSqsPrincipalAuthNotification(object):
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
        'body': 'str',
        'description': 'str',
        'queue_url_ref': 'str'
    }

    attribute_map = {
        'body': 'body',
        'description': 'description',
        'queue_url_ref': 'queueUrlRef'
    }

    required_map = {
        'body': 'required',
        'description': 'required',
        'queue_url_ref': 'required'
    }

    def __init__(self, body=None, description=None, queue_url_ref=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAwsSqsPrincipalAuthNotification - a model defined in OpenAPI"
        
        :param body:  The body of the Amazon Queue Message (required)
        :type body: str
        :param description:  The summary of the services provided by the notification (required)
        :type description: str
        :param queue_url_ref:  Reference to queue url from Configuration Store (required)
        :type queue_url_ref: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._body = None
        self._description = None
        self._queue_url_ref = None
        self.discriminator = None

        self.body = body
        self.description = description
        self.queue_url_ref = queue_url_ref

    @property
    def body(self):
        """Gets the body of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501

        The body of the Amazon Queue Message  # noqa: E501

        :return: The body of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAwsSqsPrincipalAuthNotification.

        The body of the Amazon Queue Message  # noqa: E501

        :param body: The body of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501
        :type body: str
        """
        if self.local_vars_configuration.client_side_validation and body is None:  # noqa: E501
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                body is not None and len(body) > 1024):
            raise ValueError("Invalid value for `body`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                body is not None and len(body) < 1):
            raise ValueError("Invalid value for `body`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                body is not None and not re.search(r'^[\s\S]*$', body)):  # noqa: E501
            raise ValueError(r"Invalid value for `body`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._body = body

    @property
    def description(self):
        """Gets the description of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501

        The summary of the services provided by the notification  # noqa: E501

        :return: The description of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAwsSqsPrincipalAuthNotification.

        The summary of the services provided by the notification  # noqa: E501

        :param description: The description of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501
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
    def queue_url_ref(self):
        """Gets the queue_url_ref of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501

        Reference to queue url from Configuration Store  # noqa: E501

        :return: The queue_url_ref of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501
        :rtype: str
        """
        return self._queue_url_ref

    @queue_url_ref.setter
    def queue_url_ref(self, queue_url_ref):
        """Sets the queue_url_ref of this UpdateAwsSqsPrincipalAuthNotification.

        Reference to queue url from Configuration Store  # noqa: E501

        :param queue_url_ref: The queue_url_ref of this UpdateAwsSqsPrincipalAuthNotification.  # noqa: E501
        :type queue_url_ref: str
        """
        if self.local_vars_configuration.client_side_validation and queue_url_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `queue_url_ref`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                queue_url_ref is not None and len(queue_url_ref) < 1):
            raise ValueError("Invalid value for `queue_url_ref`, length must be greater than or equal to `1`")  # noqa: E501

        self._queue_url_ref = queue_url_ref

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
        if not isinstance(other, UpdateAwsSqsPrincipalAuthNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAwsSqsPrincipalAuthNotification):
            return True

        return self.to_dict() != other.to_dict()
