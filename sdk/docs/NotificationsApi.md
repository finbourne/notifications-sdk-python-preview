# notifications.NotificationsApi

All URIs are relative to *https://fbn-ci.lusid.com/notifications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_request_notification**](NotificationsApi.md#create_api_request_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications/apirequest | [EXPERIMENTAL] Add an Api Request notification to a subscription.
[**create_email_notification**](NotificationsApi.md#create_email_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications/email | [EXPERIMENTAL] Add an email notification to a subscription.
[**create_sms_notification**](NotificationsApi.md#create_sms_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications/sms | [EXPERIMENTAL] Add an SMS notification to a subscription.
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /api/subscriptions/{scope}/{code}/notifications/{id} | [EXPERIMENTAL] Delete a notification for a given subscription.
[**get_notification**](NotificationsApi.md#get_notification) | **GET** /api/subscriptions/{scope}/{code}/notifications/{id} | [EXPERIMENTAL] Get a notification on a subscription.
[**list_notifications**](NotificationsApi.md#list_notifications) | **GET** /api/subscriptions/{scope}/{code}/notifications | [EXPERIMENTAL] List all notifications on a subscription.
[**update_api_request_notification**](NotificationsApi.md#update_api_request_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/apirequest/{id} | [EXPERIMENTAL] Update an api request notification for a given subscription.
[**update_email_notification**](NotificationsApi.md#update_email_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/email/{id} | [EXPERIMENTAL] Update an email notification for a given subscription.
[**update_sms_notification**](NotificationsApi.md#update_sms_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/sms/{id} | [EXPERIMENTAL] Update an SMS notification for a given subscription.


# **create_api_request_notification**
> Notification create_api_request_notification(scope, code, create_api_request_notification)

[EXPERIMENTAL] Add an Api Request notification to a subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a notification
code = 'code_example' # str | The code that identifies a notification
create_api_request_notification = {"description":"TestDescription","httpMethod":"Post","pathAndQuery":"notification/api/{{id}}/path?examplequery={{id}}","content":{"Key":"Value Example","MessageKey":"{{message}}"}} # CreateApiRequestNotification | The data to create a api request notification

    try:
        # [EXPERIMENTAL] Add an Api Request notification to a subscription.
        api_response = api_instance.create_api_request_notification(scope, code, create_api_request_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_api_request_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a notification | 
 **code** | **str**| The code that identifies a notification | 
 **create_api_request_notification** | [**CreateApiRequestNotification**](CreateApiRequestNotification.md)| The data to create a api request notification | 

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
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_email_notification**
> Notification create_email_notification(scope, code, create_email_notification)

[EXPERIMENTAL] Add an email notification to a subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a notification
code = 'code_example' # str | The code that identifies a notification
create_email_notification = {"description":"TestDescription","subject":"Event with id of {{id}}","body":"Event with message {{message}} and details {{details}}","emailAddressTo":["recipient@finbourne.com"],"emailAddressCc":["recipientcc@finbourne.com"],"emailAddressBcc":["recipientbcc@finbourne.com"]} # CreateEmailNotification | The data to create a email notification

    try:
        # [EXPERIMENTAL] Add an email notification to a subscription.
        api_response = api_instance.create_email_notification(scope, code, create_email_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_email_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a notification | 
 **code** | **str**| The code that identifies a notification | 
 **create_email_notification** | [**CreateEmailNotification**](CreateEmailNotification.md)| The data to create a email notification | 

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
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sms_notification**
> Notification create_sms_notification(scope, code, create_sms_notification)

[EXPERIMENTAL] Add an SMS notification to a subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a notification
code = 'code_example' # str | The code that identifies a notification
create_sms_notification = {"description":"TestDescription","body":"Event with message {{message}} and details {{details}}","recipients":["+447000000000"]} # CreateSmsNotification | The data to create an SMS notification

    try:
        # [EXPERIMENTAL] Add an SMS notification to a subscription.
        api_response = api_instance.create_sms_notification(scope, code, create_sms_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_sms_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a notification | 
 **code** | **str**| The code that identifies a notification | 
 **create_sms_notification** | [**CreateSmsNotification**](CreateSmsNotification.md)| The data to create an SMS notification | 

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
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> delete_notification(scope, code, id)

[EXPERIMENTAL] Delete a notification for a given subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification

    try:
        # [EXPERIMENTAL] Delete a notification for a given subscription.
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
**204** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification**
> Notification get_notification(scope, code, id)

[EXPERIMENTAL] Get a notification on a subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification

    try:
        # [EXPERIMENTAL] Get a notification on a subscription.
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

[EXPERIMENTAL] List all notifications on a subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription

    try:
        # [EXPERIMENTAL] List all notifications on a subscription.
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

# **update_api_request_notification**
> Notification update_api_request_notification(scope, code, id, update_api_request_notification)

[EXPERIMENTAL] Update an api request notification for a given subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a notification
code = 'code_example' # str | The code that identifies a notification
id = 'id_example' # str | The unique identifier of the notification
update_api_request_notification = {"description":"TestDescription","httpMethod":"Post","pathAndQuery":"notification/api/{{id}}/path?examplequery={{id}}","content":{"Key":"Value Example","MessageKey":"{{message}}"}} # UpdateApiRequestNotification | The data to update a notification

    try:
        # [EXPERIMENTAL] Update an api request notification for a given subscription.
        api_response = api_instance.update_api_request_notification(scope, code, id, update_api_request_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->update_api_request_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a notification | 
 **code** | **str**| The code that identifies a notification | 
 **id** | **str**| The unique identifier of the notification | 
 **update_api_request_notification** | [**UpdateApiRequestNotification**](UpdateApiRequestNotification.md)| The data to update a notification | 

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

# **update_email_notification**
> Notification update_email_notification(scope, code, id, update_email_notification)

[EXPERIMENTAL] Update an email notification for a given subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification
update_email_notification = {"description":"TestDescription","subject":"Event with id of {{id}}","body":"Event with message {{message}} and details {{details}}","emailAddressTo":["recipient@finbourne.com"],"emailAddressCc":["recipientcc@finbourne.com"],"emailAddressBcc":["recipientbcc@finbourne.com"]} # UpdateEmailNotification | The data to update a notification

    try:
        # [EXPERIMENTAL] Update an email notification for a given subscription.
        api_response = api_instance.update_email_notification(scope, code, id, update_email_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->update_email_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 
 **update_email_notification** | [**UpdateEmailNotification**](UpdateEmailNotification.md)| The data to update a notification | 

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

# **update_sms_notification**
> Notification update_sms_notification(scope, code, id, update_sms_notification)

[EXPERIMENTAL] Update an SMS notification for a given subscription.

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
    api_instance = notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification
update_sms_notification = {"description":"TestDescription","body":"Event with message {{message}} and details {{details}}","recipients":["+447000000000"]} # UpdateSmsNotification | The data to update a notification

    try:
        # [EXPERIMENTAL] Update an SMS notification for a given subscription.
        api_response = api_instance.update_sms_notification(scope, code, id, update_sms_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->update_sms_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 
 **update_sms_notification** | [**UpdateSmsNotification**](UpdateSmsNotification.md)| The data to update a notification | 

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

