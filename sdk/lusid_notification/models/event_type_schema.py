# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.762.2
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


class EventTypeSchema(object):
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
        'application': 'str',
        'header_schema': 'list[EventFieldDefinition]',
        'body_schema': 'list[EventFieldDefinition]',
        'href': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'application': 'application',
        'header_schema': 'headerSchema',
        'body_schema': 'bodySchema',
        'href': 'href'
    }

    required_map = {
        'id': 'optional',
        'display_name': 'optional',
        'description': 'optional',
        'application': 'optional',
        'header_schema': 'optional',
        'body_schema': 'optional',
        'href': 'optional'
    }

    def __init__(self, id=None, display_name=None, description=None, application=None, header_schema=None, body_schema=None, href=None, local_vars_configuration=None):  # noqa: E501
        """EventTypeSchema - a model defined in OpenAPI"
        
        :param id:  The identifier of the event type
        :type id: str
        :param display_name:  Identifier name of the event
        :type display_name: str
        :param description:  The summary of the event
        :type description: str
        :param application:  The application associated with the event
        :type application: str
        :param header_schema:  The header schema for the event type
        :type header_schema: list[lusid_notification.EventFieldDefinition]
        :param body_schema:  The body schema for the event type
        :type body_schema: list[lusid_notification.EventFieldDefinition]
        :param href:  A URI for retrieving this schema
        :type href: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._description = None
        self._application = None
        self._header_schema = None
        self._body_schema = None
        self._href = None
        self.discriminator = None

        self.id = id
        self.display_name = display_name
        self.description = description
        self.application = application
        self.header_schema = header_schema
        self.body_schema = body_schema
        self.href = href

    @property
    def id(self):
        """Gets the id of this EventTypeSchema.  # noqa: E501

        The identifier of the event type  # noqa: E501

        :return: The id of this EventTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventTypeSchema.

        The identifier of the event type  # noqa: E501

        :param id: The id of this EventTypeSchema.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this EventTypeSchema.  # noqa: E501

        Identifier name of the event  # noqa: E501

        :return: The display_name of this EventTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this EventTypeSchema.

        Identifier name of the event  # noqa: E501

        :param display_name: The display_name of this EventTypeSchema.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this EventTypeSchema.  # noqa: E501

        The summary of the event  # noqa: E501

        :return: The description of this EventTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventTypeSchema.

        The summary of the event  # noqa: E501

        :param description: The description of this EventTypeSchema.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def application(self):
        """Gets the application of this EventTypeSchema.  # noqa: E501

        The application associated with the event  # noqa: E501

        :return: The application of this EventTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this EventTypeSchema.

        The application associated with the event  # noqa: E501

        :param application: The application of this EventTypeSchema.  # noqa: E501
        :type application: str
        """

        self._application = application

    @property
    def header_schema(self):
        """Gets the header_schema of this EventTypeSchema.  # noqa: E501

        The header schema for the event type  # noqa: E501

        :return: The header_schema of this EventTypeSchema.  # noqa: E501
        :rtype: list[lusid_notification.EventFieldDefinition]
        """
        return self._header_schema

    @header_schema.setter
    def header_schema(self, header_schema):
        """Sets the header_schema of this EventTypeSchema.

        The header schema for the event type  # noqa: E501

        :param header_schema: The header_schema of this EventTypeSchema.  # noqa: E501
        :type header_schema: list[lusid_notification.EventFieldDefinition]
        """

        self._header_schema = header_schema

    @property
    def body_schema(self):
        """Gets the body_schema of this EventTypeSchema.  # noqa: E501

        The body schema for the event type  # noqa: E501

        :return: The body_schema of this EventTypeSchema.  # noqa: E501
        :rtype: list[lusid_notification.EventFieldDefinition]
        """
        return self._body_schema

    @body_schema.setter
    def body_schema(self, body_schema):
        """Sets the body_schema of this EventTypeSchema.

        The body schema for the event type  # noqa: E501

        :param body_schema: The body_schema of this EventTypeSchema.  # noqa: E501
        :type body_schema: list[lusid_notification.EventFieldDefinition]
        """

        self._body_schema = body_schema

    @property
    def href(self):
        """Gets the href of this EventTypeSchema.  # noqa: E501

        A URI for retrieving this schema  # noqa: E501

        :return: The href of this EventTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this EventTypeSchema.

        A URI for retrieving this schema  # noqa: E501

        :param href: The href of this EventTypeSchema.  # noqa: E501
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
        if not isinstance(other, EventTypeSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventTypeSchema):
            return True

        return self.to_dict() != other.to_dict()
