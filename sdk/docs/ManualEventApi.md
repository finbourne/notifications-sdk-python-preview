# lusid_notification.ManualEventApi

All URIs are relative to *https://www.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_manual_event**](ManualEventApi.md#trigger_manual_event) | **POST** /api/manualevent | [EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.


# **trigger_manual_event**
> ManualEvent trigger_manual_event(manual_event_request)

[EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_notification
from lusid_notification.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/notification
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_notification.Configuration(
    host = "https://www.lusid.com/notification"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_notification.Configuration(
    host = "https://www.lusid.com/notification"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_notification.ManualEventApi(api_client)
    manual_event_request = {"body":{"subject":"TestSubject","message":"TestMessage","jsonMessage":{"TestField1":"TestValue1","TestField2":"TestValue2"}}} # ManualEventRequest | The data required to trigger a manual event.

    try:
        # [EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.
        api_response = api_instance.trigger_manual_event(manual_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManualEventApi->trigger_manual_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_event_request** | [**ManualEventRequest**](ManualEventRequest.md)| The data required to trigger a manual event. | 

### Return type

[**ManualEvent**](ManualEvent.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

