# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.804
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
        'event_name': 'str',
        'description': 'str',
        'entity': 'str',
        'application': 'str',
        'json_schema': 'object',
        'header_schema': 'list[EventFieldDefinition]',
        'body_schema': 'list[EventFieldDefinition]'
    }

    attribute_map = {
        'id': 'id',
        'event_name': 'eventName',
        'description': 'description',
        'entity': 'entity',
        'application': 'application',
        'json_schema': 'jsonSchema',
        'header_schema': 'headerSchema',
        'body_schema': 'bodySchema'
    }

    required_map = {
        'id': 'optional',
        'event_name': 'optional',
        'description': 'optional',
        'entity': 'optional',
        'application': 'optional',
        'json_schema': 'optional',
        'header_schema': 'optional',
        'body_schema': 'optional'
    }

    def __init__(self, id=None, event_name=None, description=None, entity=None, application=None, json_schema=None, header_schema=None, body_schema=None, local_vars_configuration=None):  # noqa: E501
        """EventTypeSchema - a model defined in OpenAPI"
        
        :param id:  The identifier of the event type
        :type id: str
        :param event_name:  Identifier name of the event
        :type event_name: str
        :param description:  The summary of the event
        :type description: str
        :param entity:  The entity against which the event originated
        :type entity: str
        :param application:  The application associated with the event
        :type application: str
        :param json_schema:  The schema of the event
        :type json_schema: object
        :param header_schema:  The header schema for the event type
        :type header_schema: list[lusid_notifications.EventFieldDefinition]
        :param body_schema:  The body schema for the event type
        :type body_schema: list[lusid_notifications.EventFieldDefinition]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._event_name = None
        self._description = None
        self._entity = None
        self._application = None
        self._json_schema = None
        self._header_schema = None
        self._body_schema = None
        self.discriminator = None

        self.id = id
        self.event_name = event_name
        self.description = description
        self.entity = entity
        self.application = application
        self.json_schema = json_schema
        self.header_schema = header_schema
        self.body_schema = body_schema

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
    def event_name(self):
        """Gets the event_name of this EventTypeSchema.  # noqa: E501

        Identifier name of the event  # noqa: E501

        :return: The event_name of this EventTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this EventTypeSchema.

        Identifier name of the event  # noqa: E501

        :param event_name: The event_name of this EventTypeSchema.  # noqa: E501
        :type event_name: str
        """

        self._event_name = event_name

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
    def entity(self):
        """Gets the entity of this EventTypeSchema.  # noqa: E501

        The entity against which the event originated  # noqa: E501

        :return: The entity of this EventTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this EventTypeSchema.

        The entity against which the event originated  # noqa: E501

        :param entity: The entity of this EventTypeSchema.  # noqa: E501
        :type entity: str
        """

        self._entity = entity

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
    def json_schema(self):
        """Gets the json_schema of this EventTypeSchema.  # noqa: E501

        The schema of the event  # noqa: E501

        :return: The json_schema of this EventTypeSchema.  # noqa: E501
        :rtype: object
        """
        return self._json_schema

    @json_schema.setter
    def json_schema(self, json_schema):
        """Sets the json_schema of this EventTypeSchema.

        The schema of the event  # noqa: E501

        :param json_schema: The json_schema of this EventTypeSchema.  # noqa: E501
        :type json_schema: object
        """

        self._json_schema = json_schema

    @property
    def header_schema(self):
        """Gets the header_schema of this EventTypeSchema.  # noqa: E501

        The header schema for the event type  # noqa: E501

        :return: The header_schema of this EventTypeSchema.  # noqa: E501
        :rtype: list[lusid_notifications.EventFieldDefinition]
        """
        return self._header_schema

    @header_schema.setter
    def header_schema(self, header_schema):
        """Sets the header_schema of this EventTypeSchema.

        The header schema for the event type  # noqa: E501

        :param header_schema: The header_schema of this EventTypeSchema.  # noqa: E501
        :type header_schema: list[lusid_notifications.EventFieldDefinition]
        """

        self._header_schema = header_schema

    @property
    def body_schema(self):
        """Gets the body_schema of this EventTypeSchema.  # noqa: E501

        The body schema for the event type  # noqa: E501

        :return: The body_schema of this EventTypeSchema.  # noqa: E501
        :rtype: list[lusid_notifications.EventFieldDefinition]
        """
        return self._body_schema

    @body_schema.setter
    def body_schema(self, body_schema):
        """Sets the body_schema of this EventTypeSchema.

        The body schema for the event type  # noqa: E501

        :param body_schema: The body_schema of this EventTypeSchema.  # noqa: E501
        :type body_schema: list[lusid_notifications.EventFieldDefinition]
        """

        self._body_schema = body_schema

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
