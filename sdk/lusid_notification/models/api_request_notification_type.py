# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.758
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


class ApiRequestNotificationType(object):
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
        'http_method': 'str',
        'path_and_query': 'str',
        'content': 'object'
    }

    attribute_map = {
        'type': 'type',
        'http_method': 'httpMethod',
        'path_and_query': 'pathAndQuery',
        'content': 'content'
    }

    required_map = {
        'type': 'required',
        'http_method': 'required',
        'path_and_query': 'required',
        'content': 'optional'
    }

    def __init__(self, type=None, http_method=None, path_and_query=None, content=None, local_vars_configuration=None):  # noqa: E501
        """ApiRequestNotificationType - a model defined in OpenAPI"
        
        :param type:  The type of delivery mechanism for this notification (required)
        :type type: str
        :param http_method:  The HTTP method such as GET, POST, etc. to use on the Api Request (required)
        :type http_method: str
        :param path_and_query:  The url to send the request to. (required)
        :type path_and_query: str
        :param content:  The content of the request
        :type content: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._http_method = None
        self._path_and_query = None
        self._content = None
        self.discriminator = None

        self.type = type
        self.http_method = http_method
        self.path_and_query = path_and_query
        self.content = content

    @property
    def type(self):
        """Gets the type of this ApiRequestNotificationType.  # noqa: E501

        The type of delivery mechanism for this notification  # noqa: E501

        :return: The type of this ApiRequestNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiRequestNotificationType.

        The type of delivery mechanism for this notification  # noqa: E501

        :param type: The type of this ApiRequestNotificationType.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ApiRequest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def http_method(self):
        """Gets the http_method of this ApiRequestNotificationType.  # noqa: E501

        The HTTP method such as GET, POST, etc. to use on the Api Request  # noqa: E501

        :return: The http_method of this ApiRequestNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this ApiRequestNotificationType.

        The HTTP method such as GET, POST, etc. to use on the Api Request  # noqa: E501

        :param http_method: The http_method of this ApiRequestNotificationType.  # noqa: E501
        :type http_method: str
        """
        if self.local_vars_configuration.client_side_validation and http_method is None:  # noqa: E501
            raise ValueError("Invalid value for `http_method`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                http_method is not None and len(http_method) < 1):
            raise ValueError("Invalid value for `http_method`, length must be greater than or equal to `1`")  # noqa: E501

        self._http_method = http_method

    @property
    def path_and_query(self):
        """Gets the path_and_query of this ApiRequestNotificationType.  # noqa: E501

        The url to send the request to.  # noqa: E501

        :return: The path_and_query of this ApiRequestNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._path_and_query

    @path_and_query.setter
    def path_and_query(self, path_and_query):
        """Sets the path_and_query of this ApiRequestNotificationType.

        The url to send the request to.  # noqa: E501

        :param path_and_query: The path_and_query of this ApiRequestNotificationType.  # noqa: E501
        :type path_and_query: str
        """
        if self.local_vars_configuration.client_side_validation and path_and_query is None:  # noqa: E501
            raise ValueError("Invalid value for `path_and_query`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path_and_query is not None and len(path_and_query) > 16384):
            raise ValueError("Invalid value for `path_and_query`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path_and_query is not None and len(path_and_query) < 1):
            raise ValueError("Invalid value for `path_and_query`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path_and_query is not None and not re.search(r'^([A-Za-z0-9-._~:\/?#[\]@!$&\'()*+,;%=]|(\{\{([a-zA-Z0-9\s])*\}\}))*$', path_and_query)):  # noqa: E501
            raise ValueError(r"Invalid value for `path_and_query`, must be a follow pattern or equal to `/^([A-Za-z0-9-._~:\/?#[\]@!$&'()*+,;%=]|(\{\{([a-zA-Z0-9\s])*\}\}))*$/`")  # noqa: E501

        self._path_and_query = path_and_query

    @property
    def content(self):
        """Gets the content of this ApiRequestNotificationType.  # noqa: E501

        The content of the request  # noqa: E501

        :return: The content of this ApiRequestNotificationType.  # noqa: E501
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ApiRequestNotificationType.

        The content of the request  # noqa: E501

        :param content: The content of this ApiRequestNotificationType.  # noqa: E501
        :type content: object
        """

        self._content = content

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
        if not isinstance(other, ApiRequestNotificationType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiRequestNotificationType):
            return True

        return self.to_dict() != other.to_dict()
