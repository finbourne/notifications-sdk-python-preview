# lusid_notification.DeliveriesApi

All URIs are relative to *https://www.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_deliveries**](DeliveriesApi.md#list_deliveries) | **GET** /api/deliveries | [EXPERIMENTAL] ListDeliveries: List Deliveries


# **list_deliveries**
> ResourceListOfDelivery list_deliveries(page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListDeliveries: List Deliveries

Currently only returns deliveries with failed attempts.

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
    api_instance = lusid_notification.DeliveriesApi(api_client)
    page = 'page_example' # str | The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied. (optional)
limit = 56 # int | The maximum number of delivery attempts to retrieve. Defaults to 5000 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)

    try:
        # [EXPERIMENTAL] ListDeliveries: List Deliveries
        api_response = api_instance.list_deliveries(page=page, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeliveriesApi->list_deliveries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied. | [optional] 
 **limit** | **int**| The maximum number of delivery attempts to retrieve. Defaults to 5000 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 

### Return type

[**ResourceListOfDelivery**](ResourceListOfDelivery.md)

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
**404** | No deliveries exists with the provided filter(s) |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

