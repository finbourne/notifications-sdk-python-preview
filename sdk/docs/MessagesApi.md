# lusid_notifications.MessagesApi

All URIs are relative to *https://www.lusid.com/notifications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_undelivered_messages**](MessagesApi.md#list_undelivered_messages) | **GET** /api/subscriptions/deliveries | [EXPERIMENTAL] ListUndeliveredMessages: List undelivered messages


# **list_undelivered_messages**
> ResourceListOfUndeliveredMessage list_undelivered_messages(page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListUndeliveredMessages: List undelivered messages

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
    api_instance = lusid_notifications.MessagesApi(api_client)
    page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied the filter field should not be supplied. (optional)
limit = 56 # int | The maximum number of messages to retrieve. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\" /> filtering results from LUSID. (optional)

    try:
        # [EXPERIMENTAL] ListUndeliveredMessages: List undelivered messages
        api_response = api_instance.list_undelivered_messages(page=page, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->list_undelivered_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied the filter field should not be supplied. | [optional] 
 **limit** | **int**| The maximum number of messages to retrieve. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot; /&gt; filtering results from LUSID. | [optional] 

### Return type

[**ResourceListOfUndeliveredMessage**](ResourceListOfUndeliveredMessage.md)

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
**404** | No undelivered messages exists with the provided filter(s) |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

