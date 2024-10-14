# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1053
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


class AzureServiceBusNotificationType(object):
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
        'namespace': 'str',
        'queue_name': 'str',
        'body': 'str',
        'tenant_id': 'str',
        'client_id': 'str',
        'client_secret': 'str'
    }

    attribute_map = {
        'type': 'type',
        'namespace': 'namespace',
        'queue_name': 'queueName',
        'body': 'body',
        'tenant_id': 'tenantId',
        'client_id': 'clientId',
        'client_secret': 'clientSecret'
    }

    required_map = {
        'type': 'required',
        'namespace': 'required',
        'queue_name': 'required',
        'body': 'required',
        'tenant_id': 'required',
        'client_id': 'required',
        'client_secret': 'required'
    }

    def __init__(self, type=None, namespace=None, queue_name=None, body=None, tenant_id=None, client_id=None, client_secret=None, local_vars_configuration=None):  # noqa: E501
        """AzureServiceBusNotificationType - a model defined in OpenAPI"
        
        :param type:  The type of delivery mechanism for this notification (required)
        :type type: str
        :param namespace:  Reference to namespace from Configuration Store (required)
        :type namespace: str
        :param queue_name:  Reference to queue name from Configuration Store (required)
        :type queue_name: str
        :param body:  The body of the Azure Service Bus Message (required)
        :type body: str
        :param tenant_id:  Reference to tenant id from Configuration Store (required)
        :type tenant_id: str
        :param client_id:  Reference to client id from Configuration Store (required)
        :type client_id: str
        :param client_secret:  Reference to client secret from Configuration Store (required)
        :type client_secret: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._namespace = None
        self._queue_name = None
        self._body = None
        self._tenant_id = None
        self._client_id = None
        self._client_secret = None
        self.discriminator = None

        self.type = type
        self.namespace = namespace
        self.queue_name = queue_name
        self.body = body
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

    @property
    def type(self):
        """Gets the type of this AzureServiceBusNotificationType.  # noqa: E501

        The type of delivery mechanism for this notification  # noqa: E501

        :return: The type of this AzureServiceBusNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AzureServiceBusNotificationType.

        The type of delivery mechanism for this notification  # noqa: E501

        :param type: The type of this AzureServiceBusNotificationType.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["AzureServiceBus"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def namespace(self):
        """Gets the namespace of this AzureServiceBusNotificationType.  # noqa: E501

        Reference to namespace from Configuration Store  # noqa: E501

        :return: The namespace of this AzureServiceBusNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AzureServiceBusNotificationType.

        Reference to namespace from Configuration Store  # noqa: E501

        :param namespace: The namespace of this AzureServiceBusNotificationType.  # noqa: E501
        :type namespace: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                namespace is not None and len(namespace) < 1):
            raise ValueError("Invalid value for `namespace`, length must be greater than or equal to `1`")  # noqa: E501

        self._namespace = namespace

    @property
    def queue_name(self):
        """Gets the queue_name of this AzureServiceBusNotificationType.  # noqa: E501

        Reference to queue name from Configuration Store  # noqa: E501

        :return: The queue_name of this AzureServiceBusNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this AzureServiceBusNotificationType.

        Reference to queue name from Configuration Store  # noqa: E501

        :param queue_name: The queue_name of this AzureServiceBusNotificationType.  # noqa: E501
        :type queue_name: str
        """
        if self.local_vars_configuration.client_side_validation and queue_name is None:  # noqa: E501
            raise ValueError("Invalid value for `queue_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                queue_name is not None and len(queue_name) < 1):
            raise ValueError("Invalid value for `queue_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._queue_name = queue_name

    @property
    def body(self):
        """Gets the body of this AzureServiceBusNotificationType.  # noqa: E501

        The body of the Azure Service Bus Message  # noqa: E501

        :return: The body of this AzureServiceBusNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AzureServiceBusNotificationType.

        The body of the Azure Service Bus Message  # noqa: E501

        :param body: The body of this AzureServiceBusNotificationType.  # noqa: E501
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
    def tenant_id(self):
        """Gets the tenant_id of this AzureServiceBusNotificationType.  # noqa: E501

        Reference to tenant id from Configuration Store  # noqa: E501

        :return: The tenant_id of this AzureServiceBusNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AzureServiceBusNotificationType.

        Reference to tenant id from Configuration Store  # noqa: E501

        :param tenant_id: The tenant_id of this AzureServiceBusNotificationType.  # noqa: E501
        :type tenant_id: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) < 1):
            raise ValueError("Invalid value for `tenant_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def client_id(self):
        """Gets the client_id of this AzureServiceBusNotificationType.  # noqa: E501

        Reference to client id from Configuration Store  # noqa: E501

        :return: The client_id of this AzureServiceBusNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AzureServiceBusNotificationType.

        Reference to client id from Configuration Store  # noqa: E501

        :param client_id: The client_id of this AzureServiceBusNotificationType.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_id is not None and len(client_id) < 1):
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this AzureServiceBusNotificationType.  # noqa: E501

        Reference to client secret from Configuration Store  # noqa: E501

        :return: The client_secret of this AzureServiceBusNotificationType.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this AzureServiceBusNotificationType.

        Reference to client secret from Configuration Store  # noqa: E501

        :param client_secret: The client_secret of this AzureServiceBusNotificationType.  # noqa: E501
        :type client_secret: str
        """
        if self.local_vars_configuration.client_side_validation and client_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_secret is not None and len(client_secret) < 1):
            raise ValueError("Invalid value for `client_secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_secret = client_secret

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
        if not isinstance(other, AzureServiceBusNotificationType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureServiceBusNotificationType):
            return True

        return self.to_dict() != other.to_dict()
