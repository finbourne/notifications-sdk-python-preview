# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.906
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


class NotificationType(object):
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
        'type': 'required',
        'api_key_ref': 'required',
        'api_secret_ref': 'required',
        'body': 'required',
        'queue_url_ref': 'required',
        'subject': 'required',
        'plain_text_body': 'required',
        'html_body': 'optional',
        'email_address_to': 'required',
        'email_address_cc': 'optional',
        'email_address_bcc': 'optional',
        'recipients': 'required',
        'http_method': 'required',
        'url': 'required',
        'authentication_type': 'required',
        'authentication_configuration_item_paths': 'optional',
        'content_type': 'required',
        'content': 'optional'
    }

    def __init__(self, type=None, api_key_ref=None, api_secret_ref=None, body=None, queue_url_ref=None, subject=None, plain_text_body=None, html_body=None, email_address_to=None, email_address_cc=None, email_address_bcc=None, recipients=None, http_method=None, url=None, authentication_type=None, authentication_configuration_item_paths=None, content_type=None, content=None, local_vars_configuration=None):  # noqa: E501
        """NotificationType - a model defined in OpenAPI"
        
        :param type:  The type of delivery mechanism for this notification (required)
        :type type: str
        :param api_key_ref:  Reference to API key from Configuration Store (required)
        :type api_key_ref: str
        :param api_secret_ref:  Reference to API secret from Configuration Store (required)
        :type api_secret_ref: str
        :param body:  The body of the SMS (required)
        :type body: str
        :param queue_url_ref:  Reference to queue url from Configuration Store (required)
        :type queue_url_ref: str
        :param subject:  The subject of the email (required)
        :type subject: str
        :param plain_text_body:  The plain text body of the email (required)
        :type plain_text_body: str
        :param html_body:  The HTML body of the email (if any)
        :type html_body: str
        :param email_address_to:  'To' recipients of the email (required)
        :type email_address_to: list[str]
        :param email_address_cc:  'Cc' recipients of the email
        :type email_address_cc: list[str]
        :param email_address_bcc:  'Bcc' recipients of the email
        :type email_address_bcc: list[str]
        :param recipients:  The phone numbers to which the SMS will be sent to (E.164 format) (required)
        :type recipients: list[str]
        :param http_method:  The HTTP method such as GET, POST, etc. to use on the request (required)
        :type http_method: str
        :param url:  The URL to send the request to (required)
        :type url: str
        :param authentication_type:  The type of authentication to use on the request, can be one of the following values:  - Lusid -  Internal LUSID call  - BasicAuth - User specified Username and password  - BearerToken - Authorization header with Bearer scheme and user specified key  - None - No Authorization required on the webhook call (required)
        :type authentication_type: str
        :param authentication_configuration_item_paths:  The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires 'Username' and 'Password'  - BearerToken - Requires 'BearerToken' and optionally 'BearerScheme'  - None - None required                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \"authenticationType\": \"BasicAuth\",      \"authenticationConfigurationItemPaths\": {          \"Username\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\",          \"Password\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\"      }
        :type authentication_configuration_item_paths: dict[str, str]
        :param content_type:  The type of the content e.g. Json (required)
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
        """Gets the type of this NotificationType.  # noqa: E501

        The type of delivery mechanism for this notification  # noqa: E501

        :return: The type of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationType.

        The type of delivery mechanism for this notification  # noqa: E501

        :param type: The type of this NotificationType.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Webhook"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def api_key_ref(self):
        """Gets the api_key_ref of this NotificationType.  # noqa: E501

        Reference to API key from Configuration Store  # noqa: E501

        :return: The api_key_ref of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._api_key_ref

    @api_key_ref.setter
    def api_key_ref(self, api_key_ref):
        """Sets the api_key_ref of this NotificationType.

        Reference to API key from Configuration Store  # noqa: E501

        :param api_key_ref: The api_key_ref of this NotificationType.  # noqa: E501
        :type api_key_ref: str
        """
        if self.local_vars_configuration.client_side_validation and api_key_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key_ref`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                api_key_ref is not None and len(api_key_ref) < 1):
            raise ValueError("Invalid value for `api_key_ref`, length must be greater than or equal to `1`")  # noqa: E501

        self._api_key_ref = api_key_ref

    @property
    def api_secret_ref(self):
        """Gets the api_secret_ref of this NotificationType.  # noqa: E501

        Reference to API secret from Configuration Store  # noqa: E501

        :return: The api_secret_ref of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._api_secret_ref

    @api_secret_ref.setter
    def api_secret_ref(self, api_secret_ref):
        """Sets the api_secret_ref of this NotificationType.

        Reference to API secret from Configuration Store  # noqa: E501

        :param api_secret_ref: The api_secret_ref of this NotificationType.  # noqa: E501
        :type api_secret_ref: str
        """
        if self.local_vars_configuration.client_side_validation and api_secret_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `api_secret_ref`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                api_secret_ref is not None and len(api_secret_ref) < 1):
            raise ValueError("Invalid value for `api_secret_ref`, length must be greater than or equal to `1`")  # noqa: E501

        self._api_secret_ref = api_secret_ref

    @property
    def body(self):
        """Gets the body of this NotificationType.  # noqa: E501

        The body of the SMS  # noqa: E501

        :return: The body of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NotificationType.

        The body of the SMS  # noqa: E501

        :param body: The body of this NotificationType.  # noqa: E501
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
    def queue_url_ref(self):
        """Gets the queue_url_ref of this NotificationType.  # noqa: E501

        Reference to queue url from Configuration Store  # noqa: E501

        :return: The queue_url_ref of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._queue_url_ref

    @queue_url_ref.setter
    def queue_url_ref(self, queue_url_ref):
        """Sets the queue_url_ref of this NotificationType.

        Reference to queue url from Configuration Store  # noqa: E501

        :param queue_url_ref: The queue_url_ref of this NotificationType.  # noqa: E501
        :type queue_url_ref: str
        """
        if self.local_vars_configuration.client_side_validation and queue_url_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `queue_url_ref`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                queue_url_ref is not None and len(queue_url_ref) < 1):
            raise ValueError("Invalid value for `queue_url_ref`, length must be greater than or equal to `1`")  # noqa: E501

        self._queue_url_ref = queue_url_ref

    @property
    def subject(self):
        """Gets the subject of this NotificationType.  # noqa: E501

        The subject of the email  # noqa: E501

        :return: The subject of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this NotificationType.

        The subject of the email  # noqa: E501

        :param subject: The subject of this NotificationType.  # noqa: E501
        :type subject: str
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) > 1024):
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) < 1):
            raise ValueError("Invalid value for `subject`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and not re.search(r'^[\s\S]*$', subject)):  # noqa: E501
            raise ValueError(r"Invalid value for `subject`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._subject = subject

    @property
    def plain_text_body(self):
        """Gets the plain_text_body of this NotificationType.  # noqa: E501

        The plain text body of the email  # noqa: E501

        :return: The plain_text_body of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._plain_text_body

    @plain_text_body.setter
    def plain_text_body(self, plain_text_body):
        """Sets the plain_text_body of this NotificationType.

        The plain text body of the email  # noqa: E501

        :param plain_text_body: The plain_text_body of this NotificationType.  # noqa: E501
        :type plain_text_body: str
        """
        if self.local_vars_configuration.client_side_validation and plain_text_body is None:  # noqa: E501
            raise ValueError("Invalid value for `plain_text_body`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plain_text_body is not None and len(plain_text_body) > 2147483647):
            raise ValueError("Invalid value for `plain_text_body`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plain_text_body is not None and len(plain_text_body) < 1):
            raise ValueError("Invalid value for `plain_text_body`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plain_text_body is not None and not re.search(r'^[\s\S]*$', plain_text_body)):  # noqa: E501
            raise ValueError(r"Invalid value for `plain_text_body`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._plain_text_body = plain_text_body

    @property
    def html_body(self):
        """Gets the html_body of this NotificationType.  # noqa: E501

        The HTML body of the email (if any)  # noqa: E501

        :return: The html_body of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, html_body):
        """Sets the html_body of this NotificationType.

        The HTML body of the email (if any)  # noqa: E501

        :param html_body: The html_body of this NotificationType.  # noqa: E501
        :type html_body: str
        """
        if (self.local_vars_configuration.client_side_validation and
                html_body is not None and not re.search(r'^[\s\S]*$', html_body)):  # noqa: E501
            raise ValueError(r"Invalid value for `html_body`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._html_body = html_body

    @property
    def email_address_to(self):
        """Gets the email_address_to of this NotificationType.  # noqa: E501

        'To' recipients of the email  # noqa: E501

        :return: The email_address_to of this NotificationType.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_to

    @email_address_to.setter
    def email_address_to(self, email_address_to):
        """Sets the email_address_to of this NotificationType.

        'To' recipients of the email  # noqa: E501

        :param email_address_to: The email_address_to of this NotificationType.  # noqa: E501
        :type email_address_to: list[str]
        """
        if self.local_vars_configuration.client_side_validation and email_address_to is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address_to`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email_address_to is not None and len(email_address_to) > 10):
            raise ValueError("Invalid value for `email_address_to`, number of items must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email_address_to is not None and len(email_address_to) < 1):
            raise ValueError("Invalid value for `email_address_to`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._email_address_to = email_address_to

    @property
    def email_address_cc(self):
        """Gets the email_address_cc of this NotificationType.  # noqa: E501

        'Cc' recipients of the email  # noqa: E501

        :return: The email_address_cc of this NotificationType.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_cc

    @email_address_cc.setter
    def email_address_cc(self, email_address_cc):
        """Sets the email_address_cc of this NotificationType.

        'Cc' recipients of the email  # noqa: E501

        :param email_address_cc: The email_address_cc of this NotificationType.  # noqa: E501
        :type email_address_cc: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                email_address_cc is not None and len(email_address_cc) > 10):
            raise ValueError("Invalid value for `email_address_cc`, number of items must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email_address_cc is not None and len(email_address_cc) < 0):
            raise ValueError("Invalid value for `email_address_cc`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._email_address_cc = email_address_cc

    @property
    def email_address_bcc(self):
        """Gets the email_address_bcc of this NotificationType.  # noqa: E501

        'Bcc' recipients of the email  # noqa: E501

        :return: The email_address_bcc of this NotificationType.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_address_bcc

    @email_address_bcc.setter
    def email_address_bcc(self, email_address_bcc):
        """Sets the email_address_bcc of this NotificationType.

        'Bcc' recipients of the email  # noqa: E501

        :param email_address_bcc: The email_address_bcc of this NotificationType.  # noqa: E501
        :type email_address_bcc: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                email_address_bcc is not None and len(email_address_bcc) > 10):
            raise ValueError("Invalid value for `email_address_bcc`, number of items must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email_address_bcc is not None and len(email_address_bcc) < 0):
            raise ValueError("Invalid value for `email_address_bcc`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._email_address_bcc = email_address_bcc

    @property
    def recipients(self):
        """Gets the recipients of this NotificationType.  # noqa: E501

        The phone numbers to which the SMS will be sent to (E.164 format)  # noqa: E501

        :return: The recipients of this NotificationType.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this NotificationType.

        The phone numbers to which the SMS will be sent to (E.164 format)  # noqa: E501

        :param recipients: The recipients of this NotificationType.  # noqa: E501
        :type recipients: list[str]
        """
        if self.local_vars_configuration.client_side_validation and recipients is None:  # noqa: E501
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                recipients is not None and len(recipients) > 10):
            raise ValueError("Invalid value for `recipients`, number of items must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                recipients is not None and len(recipients) < 1):
            raise ValueError("Invalid value for `recipients`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._recipients = recipients

    @property
    def http_method(self):
        """Gets the http_method of this NotificationType.  # noqa: E501

        The HTTP method such as GET, POST, etc. to use on the request  # noqa: E501

        :return: The http_method of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this NotificationType.

        The HTTP method such as GET, POST, etc. to use on the request  # noqa: E501

        :param http_method: The http_method of this NotificationType.  # noqa: E501
        :type http_method: str
        """
        if self.local_vars_configuration.client_side_validation and http_method is None:  # noqa: E501
            raise ValueError("Invalid value for `http_method`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                http_method is not None and len(http_method) < 1):
            raise ValueError("Invalid value for `http_method`, length must be greater than or equal to `1`")  # noqa: E501

        self._http_method = http_method

    @property
    def url(self):
        """Gets the url of this NotificationType.  # noqa: E501

        The URL to send the request to  # noqa: E501

        :return: The url of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NotificationType.

        The URL to send the request to  # noqa: E501

        :param url: The url of this NotificationType.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) > 16384):
            raise ValueError("Invalid value for `url`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 1):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and not re.search(r'^([A-Za-z0-9-._~:\/?#[\]@!$&\'()*+,;%=]|(\{\{([a-zA-Z0-9\s.])*\}\}))*$', url)):  # noqa: E501
            raise ValueError(r"Invalid value for `url`, must be a follow pattern or equal to `/^([A-Za-z0-9-._~:\/?#[\]@!$&'()*+,;%=]|(\{\{([a-zA-Z0-9\s.])*\}\}))*$/`")  # noqa: E501

        self._url = url

    @property
    def authentication_type(self):
        """Gets the authentication_type of this NotificationType.  # noqa: E501

        The type of authentication to use on the request, can be one of the following values:  - Lusid -  Internal LUSID call  - BasicAuth - User specified Username and password  - BearerToken - Authorization header with Bearer scheme and user specified key  - None - No Authorization required on the webhook call  # noqa: E501

        :return: The authentication_type of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this NotificationType.

        The type of authentication to use on the request, can be one of the following values:  - Lusid -  Internal LUSID call  - BasicAuth - User specified Username and password  - BearerToken - Authorization header with Bearer scheme and user specified key  - None - No Authorization required on the webhook call  # noqa: E501

        :param authentication_type: The authentication_type of this NotificationType.  # noqa: E501
        :type authentication_type: str
        """
        if self.local_vars_configuration.client_side_validation and authentication_type is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                authentication_type is not None and len(authentication_type) < 1):
            raise ValueError("Invalid value for `authentication_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._authentication_type = authentication_type

    @property
    def authentication_configuration_item_paths(self):
        """Gets the authentication_configuration_item_paths of this NotificationType.  # noqa: E501

        The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires 'Username' and 'Password'  - BearerToken - Requires 'BearerToken' and optionally 'BearerScheme'  - None - None required                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \"authenticationType\": \"BasicAuth\",      \"authenticationConfigurationItemPaths\": {          \"Username\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\",          \"Password\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\"      }  # noqa: E501

        :return: The authentication_configuration_item_paths of this NotificationType.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._authentication_configuration_item_paths

    @authentication_configuration_item_paths.setter
    def authentication_configuration_item_paths(self, authentication_configuration_item_paths):
        """Sets the authentication_configuration_item_paths of this NotificationType.

        The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires 'Username' and 'Password'  - BearerToken - Requires 'BearerToken' and optionally 'BearerScheme'  - None - None required                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \"authenticationType\": \"BasicAuth\",      \"authenticationConfigurationItemPaths\": {          \"Username\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\",          \"Password\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\"      }  # noqa: E501

        :param authentication_configuration_item_paths: The authentication_configuration_item_paths of this NotificationType.  # noqa: E501
        :type authentication_configuration_item_paths: dict[str, str]
        """

        self._authentication_configuration_item_paths = authentication_configuration_item_paths

    @property
    def content_type(self):
        """Gets the content_type of this NotificationType.  # noqa: E501

        The type of the content e.g. Json  # noqa: E501

        :return: The content_type of this NotificationType.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this NotificationType.

        The type of the content e.g. Json  # noqa: E501

        :param content_type: The content_type of this NotificationType.  # noqa: E501
        :type content_type: str
        """
        if self.local_vars_configuration.client_side_validation and content_type is None:  # noqa: E501
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                content_type is not None and len(content_type) < 1):
            raise ValueError("Invalid value for `content_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._content_type = content_type

    @property
    def content(self):
        """Gets the content of this NotificationType.  # noqa: E501

        The content of the request  # noqa: E501

        :return: The content of this NotificationType.  # noqa: E501
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this NotificationType.

        The content of the request  # noqa: E501

        :param content: The content of this NotificationType.  # noqa: E501
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
        if not isinstance(other, NotificationType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationType):
            return True

        return self.to_dict() != other.to_dict()
