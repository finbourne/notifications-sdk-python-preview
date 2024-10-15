# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1055
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


class AzureServiceBusTypeResponse(object):
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
        'namespace_ref': 'str',
        'queue_name_ref': 'str',
        'body': 'str',
        'tenant_id_ref': 'str',
        'client_id_ref': 'str',
        'client_secret_ref': 'str'
    }

    attribute_map = {
        'type': 'type',
        'namespace_ref': 'namespaceRef',
        'queue_name_ref': 'queueNameRef',
        'body': 'body',
        'tenant_id_ref': 'tenantIdRef',
        'client_id_ref': 'clientIdRef',
        'client_secret_ref': 'clientSecretRef'
    }

    required_map = {
        'type': 'optional',
        'namespace_ref': 'optional',
        'queue_name_ref': 'optional',
        'body': 'optional',
        'tenant_id_ref': 'optional',
        'client_id_ref': 'optional',
        'client_secret_ref': 'optional'
    }

    def __init__(self, type=None, namespace_ref=None, queue_name_ref=None, body=None, tenant_id_ref=None, client_id_ref=None, client_secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """AzureServiceBusTypeResponse - a model defined in OpenAPI"
        
        :param type:  The type of delivery mechanism for this notification
        :type type: str
        :param namespace_ref:  Reference to namespace from Configuration Store
        :type namespace_ref: str
        :param queue_name_ref:  Reference to queue name from Configuration Store
        :type queue_name_ref: str
        :param body:  The body of the Azure service bus Message
        :type body: str
        :param tenant_id_ref:  Reference to tenant id  from Configuration Store
        :type tenant_id_ref: str
        :param client_id_ref:  Reference to client id from Configuration Store
        :type client_id_ref: str
        :param client_secret_ref:  Reference to client secret from Configuration Store
        :type client_secret_ref: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._namespace_ref = None
        self._queue_name_ref = None
        self._body = None
        self._tenant_id_ref = None
        self._client_id_ref = None
        self._client_secret_ref = None
        self.discriminator = None

        self.type = type
        self.namespace_ref = namespace_ref
        self.queue_name_ref = queue_name_ref
        self.body = body
        self.tenant_id_ref = tenant_id_ref
        self.client_id_ref = client_id_ref
        self.client_secret_ref = client_secret_ref

    @property
    def type(self):
        """Gets the type of this AzureServiceBusTypeResponse.  # noqa: E501

        The type of delivery mechanism for this notification  # noqa: E501

        :return: The type of this AzureServiceBusTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AzureServiceBusTypeResponse.

        The type of delivery mechanism for this notification  # noqa: E501

        :param type: The type of this AzureServiceBusTypeResponse.  # noqa: E501
        :type type: str
        """
        allowed_values = [None,"AzureServiceBus"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def namespace_ref(self):
        """Gets the namespace_ref of this AzureServiceBusTypeResponse.  # noqa: E501

        Reference to namespace from Configuration Store  # noqa: E501

        :return: The namespace_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._namespace_ref

    @namespace_ref.setter
    def namespace_ref(self, namespace_ref):
        """Sets the namespace_ref of this AzureServiceBusTypeResponse.

        Reference to namespace from Configuration Store  # noqa: E501

        :param namespace_ref: The namespace_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :type namespace_ref: str
        """

        self._namespace_ref = namespace_ref

    @property
    def queue_name_ref(self):
        """Gets the queue_name_ref of this AzureServiceBusTypeResponse.  # noqa: E501

        Reference to queue name from Configuration Store  # noqa: E501

        :return: The queue_name_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._queue_name_ref

    @queue_name_ref.setter
    def queue_name_ref(self, queue_name_ref):
        """Sets the queue_name_ref of this AzureServiceBusTypeResponse.

        Reference to queue name from Configuration Store  # noqa: E501

        :param queue_name_ref: The queue_name_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :type queue_name_ref: str
        """

        self._queue_name_ref = queue_name_ref

    @property
    def body(self):
        """Gets the body of this AzureServiceBusTypeResponse.  # noqa: E501

        The body of the Azure service bus Message  # noqa: E501

        :return: The body of this AzureServiceBusTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AzureServiceBusTypeResponse.

        The body of the Azure service bus Message  # noqa: E501

        :param body: The body of this AzureServiceBusTypeResponse.  # noqa: E501
        :type body: str
        """

        self._body = body

    @property
    def tenant_id_ref(self):
        """Gets the tenant_id_ref of this AzureServiceBusTypeResponse.  # noqa: E501

        Reference to tenant id  from Configuration Store  # noqa: E501

        :return: The tenant_id_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id_ref

    @tenant_id_ref.setter
    def tenant_id_ref(self, tenant_id_ref):
        """Sets the tenant_id_ref of this AzureServiceBusTypeResponse.

        Reference to tenant id  from Configuration Store  # noqa: E501

        :param tenant_id_ref: The tenant_id_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :type tenant_id_ref: str
        """

        self._tenant_id_ref = tenant_id_ref

    @property
    def client_id_ref(self):
        """Gets the client_id_ref of this AzureServiceBusTypeResponse.  # noqa: E501

        Reference to client id from Configuration Store  # noqa: E501

        :return: The client_id_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_id_ref

    @client_id_ref.setter
    def client_id_ref(self, client_id_ref):
        """Sets the client_id_ref of this AzureServiceBusTypeResponse.

        Reference to client id from Configuration Store  # noqa: E501

        :param client_id_ref: The client_id_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :type client_id_ref: str
        """

        self._client_id_ref = client_id_ref

    @property
    def client_secret_ref(self):
        """Gets the client_secret_ref of this AzureServiceBusTypeResponse.  # noqa: E501

        Reference to client secret from Configuration Store  # noqa: E501

        :return: The client_secret_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_secret_ref

    @client_secret_ref.setter
    def client_secret_ref(self, client_secret_ref):
        """Sets the client_secret_ref of this AzureServiceBusTypeResponse.

        Reference to client secret from Configuration Store  # noqa: E501

        :param client_secret_ref: The client_secret_ref of this AzureServiceBusTypeResponse.  # noqa: E501
        :type client_secret_ref: str
        """

        self._client_secret_ref = client_secret_ref

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
        if not isinstance(other, AzureServiceBusTypeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureServiceBusTypeResponse):
            return True

        return self.to_dict() != other.to_dict()