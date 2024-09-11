# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1050
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


class NotificationTypeResponse(object):
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
        'api_key_ref': 'str',
        'api_secret_ref': 'str',
        'body': 'str',
        'queue_url_ref': 'str',
        'namespace_ref': 'str',
        'queue_name_ref': 'str',
        'tenant_id_ref': 'str',
        'client_id_ref': 'str',
        'client_secret_ref': 'str',
        'subject': 'str',
        'plain_text_body': 'str',
        'html_body': 'str',
        'email_address_to': 'list[str]',
        'email_address_cc': 'list[str]',
        'email_address_bcc': 'list[str]',
        'recipients': 'list[str]',
        'http_method': 'str',
        'url': 'str',
        'authentication_type': 'str',
        'authentication_configuration_item_paths': 'dict[str, str]',
        'content_type': 'str',
        'content': 'object'
    }

    attribute_map = {
        'type': 'type',
        'api_key_ref': 'apiKeyRef',
        'api_secret_ref': 'apiSecretRef',
        'body': 'body',
        'queue_url_ref': 'queueUrlRef',
        'namespace_ref': 'namespaceRef',
        'queue_name_ref': 'queueNameRef',
        'tenant_id_ref': 'tenantIdRef',
        'client_id_ref': 'clientIdRef',
        'client_secret_ref': 'clientSecretRef',
        'subject': 'subject',
        'plain_text_body': 'plainTextBody',
        'html_body': 'htmlBody',
        'email_address_to': 'emailAddressTo',
        'email_address_cc': 'emailAddressCc',
        'email_address_bcc': 'emailAddressBcc',
        'recipients': 'recipients',
        'http_method': 'httpMethod',
        'url': 'url',
        'authentication_type': 'authenticationType',
        'authentication_configuration_item_paths': 'authenticationConfigurationItemPaths',
        'content_type': 'contentType',
        'content': 'content'
    }

    required_map = {
        'type': 'optional',
        'api_key_ref': 'optional',
        'api_secret_ref': 'optional',
        'body': 'optional',
        'queue_url_ref': 'optional',
        'namespace_ref': 'optional',
        'queue_name_ref': 'optional',
        'tenant_id_ref': 'optional',
        'client_id_ref': 'optional',
        'client_secret_ref': 'optional',
        'subject': 'optional',
        'plain_text_body': 'optional',
        'html_body': 'optional',
        'email_address_to': 'optional',
        'email_address_cc': 'optional',
        'email_address_bcc': 'optional',
        'recipients': 'optional',
        'http_method': 'optional',
        'url': 'optional',
        'authentication_type': 'optional',
        'authentication_configuration_item_paths': 'optional',
        'content_type': 'optional',
        'content': 'optional'
    }

    def __init__(self, type=None, api_key_ref=None, api_secret_ref=None, body=None, queue_url_ref=None, namespace_ref=None, queue_name_ref=None, tenant_id_ref=None, client_id_ref=None, client_secret_ref=None, subject=None, plain_text_body=None, html_body=None, email_address_to=None, email_address_cc=None, email_address_bcc=None, recipients=None, http_method=None, url=None, authentication_type=None, authentication_configuration_item_paths=None, content_type=None, content=None, local_vars_configuration=None):  # noqa: E501
        """NotificationTypeResponse - a model defined in OpenAPI"
        
        :param type:  The type of delivery mechanism for this notification
        :type type: str
        :param api_key_ref:  Reference to API key from Configuration Store
        :type api_key_ref: str
        :param api_secret_ref:  Reference to API secret from Configuration Store
        :type api_secret_ref: str
        :param body:  The body of the SMS
        :type body: str
        :param queue_url_ref:  Reference to queue url from Configuration Store
        :type queue_url_ref: str
        :param namespace_ref:  Reference to namespace from Configuration Store
        :type namespace_ref: str
        :param queue_name_ref:  Reference to queue name from Configuration Store
        :type queue_name_ref: str
        :param tenant_id_ref:  Reference to tenant id  from Configuration Store
        :type tenant_id_ref: str
        :param client_id_ref:  Reference to client id from Configuration Store
        :type client_id_ref: str
        :param client_secret_ref:  Reference to client secret from Configuration Store
        :type client_secret_ref: str
        :param subject:  The subject of the email
        :type subject: str
        :param plain_text_body:  The plain text body of the email
        :type plain_text_body: str
        :param html_body:  The HTML body of the email (if any)
        :type html_body: str
        :param email_address_to:  'To' recipients of the email
        :type email_address_to: list[str]
        :param email_address_cc:  'Cc' recipients of the email
        :type email_address_cc: list[str]
        :param email_address_bcc:  'Bcc' recipients of the email
        :type email_address_bcc: list[str]
        :param recipients:  The phone numbers to which the SMS will be sent to (E.164 format)
        :type recipients: list[str]
        :param http_method:  The HTTP method such as GET, POST, etc. to use on the request
        :type http_method: str
        :param url:  The URL to send the request to
        :type url: str
        :param authentication_type:  The type of authentication to use on the request
        :type authentication_type: str
        :param authentication_configuration_item_paths:  The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires 'Username' and 'Password'  - BearerToken - Requires 'BearerToken' and optionally 'BearerScheme'                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \"authenticationType\": \"BasicAuth\",      \"authenticationConfigurationItemPaths\": {          \"Username\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\",          \"Password\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\"      }
        :type authentication_configuration_item_paths: dict[str, str]
        :param content_type:  The type of the content e.g. Json
        :type content_type: str
        :param content:  The content of the request
        :type content: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._api_key_ref = None
        self._api_secret_ref = None
        self._body = None
        self._queue_url_ref = None
        self._namespace_ref = None
        self._queue_name_ref = None
        self._tenant_id_ref = None
        self._client_id_ref = None
        self._client_secret_ref = None
        self._subject = None
        self._plain_text_body = None
        self._html_body = None
        self._email_address_to = None
        self._email_address_cc = None
        self._email_address_bcc = None
        self._recipients = None
        self._http_method = None
        self._url = None
        self._authentication_type = None
        self._authentication_configuration_item_paths = None
        self._content_type = None
        self._content = None
        self.discriminator = None

        self.type = type
        self.api_key_ref = api_key_ref
        self.api_secret_ref = api_secret_ref
        self.body = body
        self.queue_url_ref = queue_url_ref
        self.namespace_ref = namespace_ref
        self.queue_name_ref = queue_name_ref
        self.tenant_id_ref = tenant_id_ref
        self.client_id_ref = client_id_ref
        self.client_secret_ref = client_secret_ref
        self.subject = subject
        self.plain_text_body = plain_text_body
        self.html_body = html_body
        self.email_address_to = email_address_to
        self.email_address_cc = email_address_cc
        self.email_address_bcc = email_address_bcc
        self.recipients = recipients
        self.http_method = http_method
        self.url = url
        self.authentication_type = authentication_type
        self.authentication_configuration_item_paths = authentication_configuration_item_paths
        self.content_type = content_type
        self.content = content

    @property
    def type(self):
        """Gets the type of this NotificationTypeResponse.  # noqa: E501

        The type of delivery mechanism for this notification  # noqa: E501

        :return: The type of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationTypeResponse.

        The type of delivery mechanism for this notification  # noqa: E501

        :param type: The type of this NotificationTypeResponse.  # noqa: E501
        :type type: str
        """
        allowed_values = [None,"Webhook"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def api_key_ref(self):
        """Gets the api_key_ref of this NotificationTypeResponse.  # noqa: E501

        Reference to API key from Configuration Store  # noqa: E501

        :return: The api_key_ref of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_key_ref

    @api_key_ref.setter
    def api_key_ref(self, api_key_ref):
        """Sets the api_key_ref of this NotificationTypeResponse.

        Reference to API key from Configuration Store  # noqa: E501

        :param api_key_ref: The api_key_ref of this NotificationTypeResponse.  # noqa: E501
        :type api_key_ref: str
        """

        self._api_key_ref = api_key_ref

    @property
    def api_secret_ref(self):
        """Gets the api_secret_ref of this NotificationTypeResponse.  # noqa: E501

        Reference to API secret from Configuration Store  # noqa: E501

        :return: The api_secret_ref of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_secret_ref

    @api_secret_ref.setter
    def api_secret_ref(self, api_secret_ref):
        """Sets the api_secret_ref of this NotificationTypeResponse.

        Reference to API secret from Configuration Store  # noqa: E501

        :param api_secret_ref: The api_secret_ref of this NotificationTypeResponse.  # noqa: E501
        :type api_secret_ref: str
        """

        self._api_secret_ref = api_secret_ref

    @property
    def body(self):
        """Gets the body of this NotificationTypeResponse.  # noqa: E501

        The body of the SMS  # noqa: E501

        :return: The body of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NotificationTypeResponse.

        The body of the SMS  # noqa: E501

        :param body: The body of this NotificationTypeResponse.  # noqa: E501
        :type body: str
        """

        self._body = body

    @property
    def queue_url_ref(self):
        """Gets the queue_url_ref of this NotificationTypeResponse.  # noqa: E501

        Reference to queue url from Configuration Store  # noqa: E501

        :return: The queue_url_ref of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._queue_url_ref

    @queue_url_ref.setter
    def queue_url_ref(self, queue_url_ref):
        """Sets the queue_url_ref of this NotificationTypeResponse.

        Reference to queue url from Configuration Store  # noqa: E501

        :param queue_url_ref: The queue_url_ref of this NotificationTypeResponse.  # noqa: E501
        :type queue_url_ref: str
        """

        self._queue_url_ref = queue_url_ref

    @property
    def namespace_ref(self):
        """Gets the namespace_ref of this NotificationTypeResponse.  # noqa: E501

        Reference to namespace from Configuration Store  # noqa: E501

        :return: The namespace_ref of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._namespace_ref

    @namespace_ref.setter
    def namespace_ref(self, namespace_ref):
        """Sets the namespace_ref of this NotificationTypeResponse.

        Reference to namespace from Configuration Store  # noqa: E501

        :param namespace_ref: The namespace_ref of this NotificationTypeResponse.  # noqa: E501
        :type namespace_ref: str
        """

        self._namespace_ref = namespace_ref

    @property
    def queue_name_ref(self):
        """Gets the queue_name_ref of this NotificationTypeResponse.  # noqa: E501

        Reference to queue name from Configuration Store  # noqa: E501

        :return: The queue_name_ref of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._queue_name_ref

    @queue_name_ref.setter
    def queue_name_ref(self, queue_name_ref):
        """Sets the queue_name_ref of this NotificationTypeResponse.

        Reference to queue name from Configuration Store  # noqa: E501

        :param queue_name_ref: The queue_name_ref of this NotificationTypeResponse.  # noqa: E501
        :type queue_name_ref: str
        """

        self._queue_name_ref = queue_name_ref

    @property
    def tenant_id_ref(self):
        """Gets the tenant_id_ref of this NotificationTypeResponse.  # noqa: E501

        Reference to tenant id  from Configuration Store  # noqa: E501

        :return: The tenant_id_ref of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id_ref

    @tenant_id_ref.setter
    def tenant_id_ref(self, tenant_id_ref):
        """Sets the tenant_id_ref of this NotificationTypeResponse.

        Reference to tenant id  from Configuration Store  # noqa: E501

        :param tenant_id_ref: The tenant_id_ref of this NotificationTypeResponse.  # noqa: E501
        :type tenant_id_ref: str
        """

        self._tenant_id_ref = tenant_id_ref

    @property
    def client_id_ref(self):
        """Gets the client_id_ref of this NotificationTypeResponse.  # noqa: E501

        Reference to client id from Configuration Store  # noqa: E501

        :return: The client_id_ref of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_id_ref

    @client_id_ref.setter
    def client_id_ref(self, client_id_ref):
        """Sets the client_id_ref of this NotificationTypeResponse.

        Reference to client id from Configuration Store  # noqa: E501

        :param client_id_ref: The client_id_ref of this NotificationTypeResponse.  # noqa: E501
        :type client_id_ref: str
        """

        self._client_id_ref = client_id_ref

    @property
    def client_secret_ref(self):
        """Gets the client_secret_ref of this NotificationTypeResponse.  # noqa: E501

        Reference to client secret from Configuration Store  # noqa: E501

        :return: The client_secret_ref of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_secret_ref

    @client_secret_ref.setter
    def client_secret_ref(self, client_secret_ref):
        """Sets the client_secret_ref of this NotificationTypeResponse.

        Reference to client secret from Configuration Store  # noqa: E501

        :param client_secret_ref: The client_secret_ref of this NotificationTypeResponse.  # noqa: E501
        :type client_secret_ref: str
        """

        self._client_secret_ref = client_secret_ref

    @property
    def subject(self):
        """Gets the subject of this NotificationTypeResponse.  # noqa: E501

        The subject of the email  # noqa: E501

        :return: The subject of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this NotificationTypeResponse.

        The subject of the email  # noqa: E501

        :param subject: The subject of this NotificationTypeResponse.  # noqa: E501
        :type subject: str
        """

        self._subject = subject

    @property
    def plain_text_body(self):
        """Gets the plain_text_body of this NotificationTypeResponse.  # noqa: E501

        The plain text body of the email  # noqa: E501

        :return: The plain_text_body of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._plain_text_body

    @plain_text_body.setter
    def plain_text_body(self, plain_text_body):
        """Sets the plain_text_body of this NotificationTypeResponse.

        The plain text body of the email  # noqa: E501

        :param plain_text_body: The plain_text_body of this NotificationTypeResponse.  # noqa: E501
        :type plain_text_body: str
        """

        self._plain_text_body = plain_text_body

    @property
    def html_body(self):
        """Gets the html_body of this NotificationTypeResponse.  # noqa: E501

        The HTML body of the email (if any)  # noqa: E501

        :return: The html_body of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, html_body):
        """Sets the html_body of this NotificationTypeResponse.

        The HTML body of the email (if any)  # noqa: E501

        :param html_body: The html_body of this NotificationTypeResponse.  # noqa: E501
        :type html_body: str
        """

        self._html_body = html_body

    @property
    def email_address_to(self):
        """Gets the email_address_to of this NotificationTypeResponse.  # noqa: E501

        'To' recipients of the email  # noqa: E501

        :return: The email_address_to of this NotificationTypeResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_to

    @email_address_to.setter
    def email_address_to(self, email_address_to):
        """Sets the email_address_to of this NotificationTypeResponse.

        'To' recipients of the email  # noqa: E501

        :param email_address_to: The email_address_to of this NotificationTypeResponse.  # noqa: E501
        :type email_address_to: list[str]
        """

        self._email_address_to = email_address_to

    @property
    def email_address_cc(self):
        """Gets the email_address_cc of this NotificationTypeResponse.  # noqa: E501

        'Cc' recipients of the email  # noqa: E501

        :return: The email_address_cc of this NotificationTypeResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_cc

    @email_address_cc.setter
    def email_address_cc(self, email_address_cc):
        """Sets the email_address_cc of this NotificationTypeResponse.

        'Cc' recipients of the email  # noqa: E501

        :param email_address_cc: The email_address_cc of this NotificationTypeResponse.  # noqa: E501
        :type email_address_cc: list[str]
        """

        self._email_address_cc = email_address_cc

    @property
    def email_address_bcc(self):
        """Gets the email_address_bcc of this NotificationTypeResponse.  # noqa: E501

        'Bcc' recipients of the email  # noqa: E501

        :return: The email_address_bcc of this NotificationTypeResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_bcc

    @email_address_bcc.setter
    def email_address_bcc(self, email_address_bcc):
        """Sets the email_address_bcc of this NotificationTypeResponse.

        'Bcc' recipients of the email  # noqa: E501

        :param email_address_bcc: The email_address_bcc of this NotificationTypeResponse.  # noqa: E501
        :type email_address_bcc: list[str]
        """

        self._email_address_bcc = email_address_bcc

    @property
    def recipients(self):
        """Gets the recipients of this NotificationTypeResponse.  # noqa: E501

        The phone numbers to which the SMS will be sent to (E.164 format)  # noqa: E501

        :return: The recipients of this NotificationTypeResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this NotificationTypeResponse.

        The phone numbers to which the SMS will be sent to (E.164 format)  # noqa: E501

        :param recipients: The recipients of this NotificationTypeResponse.  # noqa: E501
        :type recipients: list[str]
        """

        self._recipients = recipients

    @property
    def http_method(self):
        """Gets the http_method of this NotificationTypeResponse.  # noqa: E501

        The HTTP method such as GET, POST, etc. to use on the request  # noqa: E501

        :return: The http_method of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this NotificationTypeResponse.

        The HTTP method such as GET, POST, etc. to use on the request  # noqa: E501

        :param http_method: The http_method of this NotificationTypeResponse.  # noqa: E501
        :type http_method: str
        """

        self._http_method = http_method

    @property
    def url(self):
        """Gets the url of this NotificationTypeResponse.  # noqa: E501

        The URL to send the request to  # noqa: E501

        :return: The url of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NotificationTypeResponse.

        The URL to send the request to  # noqa: E501

        :param url: The url of this NotificationTypeResponse.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def authentication_type(self):
        """Gets the authentication_type of this NotificationTypeResponse.  # noqa: E501

        The type of authentication to use on the request  # noqa: E501

        :return: The authentication_type of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this NotificationTypeResponse.

        The type of authentication to use on the request  # noqa: E501

        :param authentication_type: The authentication_type of this NotificationTypeResponse.  # noqa: E501
        :type authentication_type: str
        """

        self._authentication_type = authentication_type

    @property
    def authentication_configuration_item_paths(self):
        """Gets the authentication_configuration_item_paths of this NotificationTypeResponse.  # noqa: E501

        The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires 'Username' and 'Password'  - BearerToken - Requires 'BearerToken' and optionally 'BearerScheme'                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \"authenticationType\": \"BasicAuth\",      \"authenticationConfigurationItemPaths\": {          \"Username\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\",          \"Password\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\"      }  # noqa: E501

        :return: The authentication_configuration_item_paths of this NotificationTypeResponse.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._authentication_configuration_item_paths

    @authentication_configuration_item_paths.setter
    def authentication_configuration_item_paths(self, authentication_configuration_item_paths):
        """Sets the authentication_configuration_item_paths of this NotificationTypeResponse.

        The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires 'Username' and 'Password'  - BearerToken - Requires 'BearerToken' and optionally 'BearerScheme'                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \"authenticationType\": \"BasicAuth\",      \"authenticationConfigurationItemPaths\": {          \"Username\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\",          \"Password\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\"      }  # noqa: E501

        :param authentication_configuration_item_paths: The authentication_configuration_item_paths of this NotificationTypeResponse.  # noqa: E501
        :type authentication_configuration_item_paths: dict[str, str]
        """

        self._authentication_configuration_item_paths = authentication_configuration_item_paths

    @property
    def content_type(self):
        """Gets the content_type of this NotificationTypeResponse.  # noqa: E501

        The type of the content e.g. Json  # noqa: E501

        :return: The content_type of this NotificationTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this NotificationTypeResponse.

        The type of the content e.g. Json  # noqa: E501

        :param content_type: The content_type of this NotificationTypeResponse.  # noqa: E501
        :type content_type: str
        """

        self._content_type = content_type

    @property
    def content(self):
        """Gets the content of this NotificationTypeResponse.  # noqa: E501

        The content of the request  # noqa: E501

        :return: The content of this NotificationTypeResponse.  # noqa: E501
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this NotificationTypeResponse.

        The content of the request  # noqa: E501

        :param content: The content of this NotificationTypeResponse.  # noqa: E501
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
        if not isinstance(other, NotificationTypeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationTypeResponse):
            return True

        return self.to_dict() != other.to_dict()
