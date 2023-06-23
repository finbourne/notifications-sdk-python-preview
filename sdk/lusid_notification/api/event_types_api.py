# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.756
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid_notification.api_client import ApiClient
from lusid_notification.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid_notification.models.event_type_schema import EventTypeSchema
from lusid_notification.models.lusid_problem_details import LusidProblemDetails
from lusid_notification.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid_notification.models.resource_list_of_event_type_schema import ResourceListOfEventTypeSchema


class EventTypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_event_type(self, event_type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetEventType: Gets the specified event type schema.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_type(event_type, async_req=True)
        >>> result = thread.get()

        :param event_type: The event type to retrieve schema for. (required)
        :type event_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: EventTypeSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.get_event_type_with_http_info(event_type, **kwargs)  # noqa: E501

    def get_event_type_with_http_info(self, event_type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetEventType: Gets the specified event type schema.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_type_with_http_info(event_type, async_req=True)
        >>> result = thread.get()

        :param event_type: The event type to retrieve schema for. (required)
        :type event_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (EventTypeSchema, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'event_type'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'event_type' is set
        if self.api_client.client_side_validation and ('event_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_type` when calling `get_event_type`")  # noqa: E501

        if self.api_client.client_side_validation and ('event_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['event_type']) > 512):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `event_type` when calling `get_event_type`, length must be less than or equal to `512`")  # noqa: E501
        if self.api_client.client_side_validation and ('event_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['event_type']) < 0):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `event_type` when calling `get_event_type`, length must be greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'event_type' in local_var_params and not re.search(r'^[a-zA-Z]*$', local_var_params['event_type']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `event_type` when calling `get_event_type`, must conform to the pattern `/^[a-zA-Z]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'event_type' in local_var_params:
            path_params['eventType'] = local_var_params['event_type']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.1.756'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "EventTypeSchema",
            400: "LusidValidationProblemDetails",
            404: "str",
        }

        return self.api_client.call_api(
            '/api/eventtypes/{eventType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_event_types(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListEventTypes: Lists all of the available event types.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_event_types(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfEventTypeSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.list_event_types_with_http_info(**kwargs)  # noqa: E501

    def list_event_types_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListEventTypes: Lists all of the available event types.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_event_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ResourceListOfEventTypeSchema, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_event_types" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.1.756'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "ResourceListOfEventTypeSchema",
            404: "str",
        }

        return self.api_client.call_api(
            '/api/eventtypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
