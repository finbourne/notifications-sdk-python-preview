# notifications.EventsApi

All URIs are relative to *https://fbn-ci.lusid.com/notifications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event**](EventsApi.md#create_event) | **POST** /api/events | [EXPERIMENTAL] Create a new event.


# **create_event**
> object create_event(body)

[EXPERIMENTAL] Create a new event.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import notifications
from notifications.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/notifications
# See configuration.py for a list of all supported configuration parameters.
configuration = notifications.Configuration(
    host = "https://fbn-ci.lusid.com/notifications"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = notifications.Configuration(
    host = "https://fbn-ci.lusid.com/notifications"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with notifications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notifications.EventsApi(api_client)
    body = {"EventType":"Manual","Id":"acb5722d-341a-4802-b9fd-cf740a6a7797","Message":"TestMessage","Details":"TestDetails","EventTime":"2021-08-27T17:39:02.9427036+01:00"} # object | The data to create an event.

    try:
        # [EXPERIMENTAL] Create a new event.
        api_response = api_instance.create_event(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->create_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| The data to create an event. | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

