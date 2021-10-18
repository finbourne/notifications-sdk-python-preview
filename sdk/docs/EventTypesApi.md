# lusid_notifications.EventTypesApi

All URIs are relative to *https://www.lusid.com/notifications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_type**](EventTypesApi.md#get_event_type) | **GET** /api/eventtypes/{eventType} | [EXPERIMENTAL] Gets the specified event type schema.
[**list_event_types**](EventTypesApi.md#list_event_types) | **GET** /api/eventtypes | [EXPERIMENTAL] Lists all of the available event types.


# **get_event_type**
> EventTypeSchema get_event_type(event_type)

[EXPERIMENTAL] Gets the specified event type schema.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_notifications
from lusid_notifications.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/notifications
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_notifications.Configuration(
    host = "https://www.lusid.com/notifications"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_notifications.Configuration(
    host = "https://www.lusid.com/notifications"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_notifications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_notifications.EventTypesApi(api_client)
    event_type = 'event_type_example' # str | The event type

    try:
        # [EXPERIMENTAL] Gets the specified event type schema.
        api_response = api_instance.get_event_type(event_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventTypesApi->get_event_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**| The event type | 

### Return type

[**EventTypeSchema**](EventTypeSchema.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No event type exists with the specified type |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_types**
> ResourceListOfEventTypeSchema list_event_types()

[EXPERIMENTAL] Lists all of the available event types.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_notifications
from lusid_notifications.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/notifications
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_notifications.Configuration(
    host = "https://www.lusid.com/notifications"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_notifications.Configuration(
    host = "https://www.lusid.com/notifications"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_notifications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_notifications.EventTypesApi(api_client)
    
    try:
        # [EXPERIMENTAL] Lists all of the available event types.
        api_response = api_instance.list_event_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventTypesApi->list_event_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfEventTypeSchema**](ResourceListOfEventTypeSchema.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | No event types found |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

