# lusid_notification.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](NotificationsApi.md#create_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications | [EXPERIMENTAL] CreateNotification: Add a Notification to a Subscription.
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /api/subscriptions/{scope}/{code}/notifications/{id} | [EXPERIMENTAL] DeleteNotification: Delete a notification for a given subscription.
[**get_notification**](NotificationsApi.md#get_notification) | **GET** /api/subscriptions/{scope}/{code}/notifications/{id} | [EXPERIMENTAL] GetNotification: Get a notification on a subscription.
[**list_notifications**](NotificationsApi.md#list_notifications) | **GET** /api/subscriptions/{scope}/{code}/notifications | [EXPERIMENTAL] ListNotifications: List all notifications on a subscription.
[**update_notification**](NotificationsApi.md#update_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/{id} | [EXPERIMENTAL] UpdateNotification: Update a Notification for a Subscription


# **create_notification**
> Notification create_notification(scope, code, create_notification_request)

[EXPERIMENTAL] CreateNotification: Add a Notification to a Subscription.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_notification
from lusid_notification.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_notification.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
create_notification_request = {"notificationId":"TestId","displayName":"TestDisplayName","description":"TestDescription","notificationType":{"Type":"Email","Subject":"Event with id of {{id}}","PlainTextBody":"Event with message {{message}} and subject {{subject}}","HtmlBody":"<p>Event with message {{message}} and subject {{subject}}</p>","EmailAddressTo":["recipient@finbourne.com"],"EmailAddressCc":["recipientcc@finbourne.com"],"EmailAddressBcc":["recipientbcc@finbourne.com"]}} # CreateNotificationRequest | The data to create a notification

    try:
        # [EXPERIMENTAL] CreateNotification: Add a Notification to a Subscription.
        api_response = api_instance.create_notification(scope, code, create_notification_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **create_notification_request** | [**CreateNotificationRequest**](CreateNotificationRequest.md)| The data to create a notification | 

### Return type

[**Notification**](Notification.md)

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

# **delete_notification**
> delete_notification(scope, code, id)

[EXPERIMENTAL] DeleteNotification: Delete a notification for a given subscription.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_notification
from lusid_notification.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_notification.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification

    try:
        # [EXPERIMENTAL] DeleteNotification: Delete a notification for a given subscription.
        api_instance.delete_notification(scope, code, id)
    except ApiException as e:
        print("Exception when calling NotificationsApi->delete_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification**
> Notification get_notification(scope, code, id)

[EXPERIMENTAL] GetNotification: Get a notification on a subscription.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_notification
from lusid_notification.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_notification.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification

    try:
        # [EXPERIMENTAL] GetNotification: Get a notification on a subscription.
        api_response = api_instance.get_notification(scope, code, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->get_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 

### Return type

[**Notification**](Notification.md)

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
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> ResourceListOfNotification list_notifications(scope, code)

[EXPERIMENTAL] ListNotifications: List all notifications on a subscription.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_notification
from lusid_notification.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_notification.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription

    try:
        # [EXPERIMENTAL] ListNotifications: List all notifications on a subscription.
        api_response = api_instance.list_notifications(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->list_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 

### Return type

[**ResourceListOfNotification**](ResourceListOfNotification.md)

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
**404** | No notifications exists with the provided filter(s) |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification**
> Notification update_notification(scope, code, id, update_notification_request)

[EXPERIMENTAL] UpdateNotification: Update a Notification for a Subscription

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_notification
from lusid_notification.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_notification.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_notification.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification
update_notification_request = {"displayName":"TestDisplayName","description":"Example description","notificationType":{"Type":"Email","Subject":"Event with id of {{id}}","PlainTextBody":"Event with message {{message}} and subject {{subject}}","HtmlBody":"<p>Event with message {{message}} and subject {{subject}}</p>","EmailAddressTo":["recipient@finbourne.com"],"EmailAddressCc":["recipientcc@finbourne.com"],"EmailAddressBcc":["recipientbcc@finbourne.com"]}} # UpdateNotificationRequest | The data to update a notification

    try:
        # [EXPERIMENTAL] UpdateNotification: Update a Notification for a Subscription
        api_response = api_instance.update_notification(scope, code, id, update_notification_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->update_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 
 **update_notification_request** | [**UpdateNotificationRequest**](UpdateNotificationRequest.md)| The data to update a notification | 

### Return type

[**Notification**](Notification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

