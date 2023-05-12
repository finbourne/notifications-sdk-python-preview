# lusid_notifications.NotificationsApi

All URIs are relative to *https://www.lusid.com/notifications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_sqs_notification**](NotificationsApi.md#create_aws_sqs_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications/awssqs | [EXPERIMENTAL] CreateAwsSqsNotification: Add an AWS SQS notification to a subscription.
[**create_email_notification**](NotificationsApi.md#create_email_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications/email | [EXPERIMENTAL] CreateEmailNotification: Add an email notification to a subscription.
[**create_sms_notification**](NotificationsApi.md#create_sms_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications/sms | [EXPERIMENTAL] CreateSmsNotification: Add an SMS notification to a subscription.
[**create_webhook_notification**](NotificationsApi.md#create_webhook_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications/webhook | [EXPERIMENTAL] CreateWebhookNotification: Add a Webhook notification to a subscription.
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /api/subscriptions/{scope}/{code}/notifications/{id} | [EXPERIMENTAL] DeleteNotification: Delete a notification for a given subscription.
[**get_notification**](NotificationsApi.md#get_notification) | **GET** /api/subscriptions/{scope}/{code}/notifications/{id} | [EXPERIMENTAL] GetNotification: Get a notification on a subscription.
[**list_notifications**](NotificationsApi.md#list_notifications) | **GET** /api/subscriptions/{scope}/{code}/notifications | [EXPERIMENTAL] ListNotifications: List all notifications on a subscription.
[**update_aws_sqs_notification**](NotificationsApi.md#update_aws_sqs_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/awssqs/{id} | [EXPERIMENTAL] UpdateAwsSqsNotification: Update an AWS SQS notification for a given subscription.
[**update_email_notification**](NotificationsApi.md#update_email_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/email/{id} | [EXPERIMENTAL] UpdateEmailNotification: Update an email notification for a given subscription.
[**update_sms_notification**](NotificationsApi.md#update_sms_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/sms/{id} | [EXPERIMENTAL] UpdateSmsNotification: Update an SMS notification for a given subscription.
[**update_webhook_notification**](NotificationsApi.md#update_webhook_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/webhook/{id} | [EXPERIMENTAL] UpdateWebhookNotification: Update a Webhook notification for a given subscription.


# **create_aws_sqs_notification**
> Notification create_aws_sqs_notification(scope, code, create_aws_sqs_notification)

[EXPERIMENTAL] CreateAwsSqsNotification: Add an AWS SQS notification to a subscription.

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a notification
code = 'code_example' # str | The code that identifies a notification
create_aws_sqs_notification = {"apiKeyRef":"config://shared/official/system-a-config/apiKey","apiSecretRef":"config://shared/official/system-a-config/apiSecret","body":"Event with message {{message}}","description":"Example description","queueUrlRef":"config://shared/official/system-a-config/queueUrl"} # CreateAwsSqsNotification | The data to create an message sent to AWS Simple Queue Service

    try:
        # [EXPERIMENTAL] CreateAwsSqsNotification: Add an AWS SQS notification to a subscription.
        api_response = api_instance.create_aws_sqs_notification(scope, code, create_aws_sqs_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_aws_sqs_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a notification | 
 **code** | **str**| The code that identifies a notification | 
 **create_aws_sqs_notification** | [**CreateAwsSqsNotification**](CreateAwsSqsNotification.md)| The data to create an message sent to AWS Simple Queue Service | 

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

# **create_email_notification**
> Notification create_email_notification(scope, code, create_email_notification)

[EXPERIMENTAL] CreateEmailNotification: Add an email notification to a subscription.

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
create_email_notification = {"description":"TestDescription","subject":"Event with id of {{id}}","plainTextBody":"Event with message {{message}} and subject {{subject}}","htmlBody":"<p>Event with message {{message}} and subject {{subject}}</p>","emailAddressTo":["recipient@finbourne.com"],"emailAddressCc":["recipientcc@finbourne.com"],"emailAddressBcc":["recipientbcc@finbourne.com"]} # CreateEmailNotification | The data to create a email notification

    try:
        # [EXPERIMENTAL] CreateEmailNotification: Add an email notification to a subscription.
        api_response = api_instance.create_email_notification(scope, code, create_email_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_email_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
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
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sms_notification**
> Notification create_sms_notification(scope, code, create_sms_notification)

[EXPERIMENTAL] CreateSmsNotification: Add an SMS notification to a subscription.

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
create_sms_notification = {"description":"TestDescription","body":"Event with message {{message}} and subject {{subject}}","recipients":["+447000000000"]} # CreateSmsNotification | The data to create an SMS notification

    try:
        # [EXPERIMENTAL] CreateSmsNotification: Add an SMS notification to a subscription.
        api_response = api_instance.create_sms_notification(scope, code, create_sms_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_sms_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
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
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook_notification**
> Notification create_webhook_notification(scope, code, create_webhook_notification)

[EXPERIMENTAL] CreateWebhookNotification: Add a Webhook notification to a subscription.

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
create_webhook_notification = {"description":"TestDescription","httpMethod":"Post","url":"https://example.com/api/{{id}}/path?examplequery={{id}}","authenticationType":"BearerToken","authenticationConfigurationItemPaths":{"BearerToken":"config://personal/myUserId/WebhookConfigurations/ExampleService/BearerToken"},"contentType":"Json","content":{"Key":"Value Example","MessageKey":"{{message}}"}} # CreateWebhookNotification | The data to create a webhook notification

    try:
        # [EXPERIMENTAL] CreateWebhookNotification: Add a Webhook notification to a subscription.
        api_response = api_instance.create_webhook_notification(scope, code, create_webhook_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_webhook_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **create_webhook_notification** | [**CreateWebhookNotification**](CreateWebhookNotification.md)| The data to create a webhook notification | 

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
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
    api_instance = lusid_notifications.NotificationsApi(api_client)
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
    api_instance = lusid_notifications.NotificationsApi(api_client)
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

# **update_aws_sqs_notification**
> Notification update_aws_sqs_notification(scope, code, id, update_aws_sqs_notification)

[EXPERIMENTAL] UpdateAwsSqsNotification: Update an AWS SQS notification for a given subscription.

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a notification
code = 'code_example' # str | The code that identifies a notification
id = 'id_example' # str | The unique identifier of the notification
update_aws_sqs_notification = {"apiKeyRef":"config://shared/official/system-a-config/apiKey","apiSecretRef":"config://shared/official/system-a-config/apiSecret","body":"Event with message {{message}}","description":"Example description","queueUrlRef":"config://shared/official/system-a-config/queueUrl"} # UpdateAwsSqsNotification | The data to update a notification

    try:
        # [EXPERIMENTAL] UpdateAwsSqsNotification: Update an AWS SQS notification for a given subscription.
        api_response = api_instance.update_aws_sqs_notification(scope, code, id, update_aws_sqs_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->update_aws_sqs_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a notification | 
 **code** | **str**| The code that identifies a notification | 
 **id** | **str**| The unique identifier of the notification | 
 **update_aws_sqs_notification** | [**UpdateAwsSqsNotification**](UpdateAwsSqsNotification.md)| The data to update a notification | 

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

[EXPERIMENTAL] UpdateEmailNotification: Update an email notification for a given subscription.

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification
update_email_notification = {"description":"TestDescription","subject":"Event with id of {{id}}","plainTextBody":"Event with message {{message}} and subject {{subject}}","htmlBody":"<p>Event with message {{message}} and subject {{subject}}</p>","emailAddressTo":["recipient@finbourne.com"],"emailAddressCc":["recipientcc@finbourne.com"],"emailAddressBcc":["recipientbcc@finbourne.com"]} # UpdateEmailNotification | The data to update a notification

    try:
        # [EXPERIMENTAL] UpdateEmailNotification: Update an email notification for a given subscription.
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

[EXPERIMENTAL] UpdateSmsNotification: Update an SMS notification for a given subscription.

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification
update_sms_notification = {"description":"TestDescription","body":"Event with message {{message}} and subject {{subject}}","recipients":["+447000000000"]} # UpdateSmsNotification | The data to update a notification

    try:
        # [EXPERIMENTAL] UpdateSmsNotification: Update an SMS notification for a given subscription.
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

# **update_webhook_notification**
> Notification update_webhook_notification(scope, code, id, update_webhook_notification)

[EXPERIMENTAL] UpdateWebhookNotification: Update a Webhook notification for a given subscription.

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
    api_instance = lusid_notifications.NotificationsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a subscription
code = 'code_example' # str | The code that identifies a subscription
id = 'id_example' # str | The unique identifier of the notification
update_webhook_notification = {"description":"TestDescription","httpMethod":"Post","url":"https://example.com/api/{{id}}/path?examplequery={{id}}","authenticationType":"BearerToken","authenticationConfigurationItemPaths":{"BearerToken":"config://personal/myUserId/WebhookConfigurations/ExampleService/BearerToken"},"contentType":"Json","content":{"Key":"Value Example","MessageKey":"{{message}}"}} # UpdateWebhookNotification | The data to update a notification

    try:
        # [EXPERIMENTAL] UpdateWebhookNotification: Update a Webhook notification for a given subscription.
        api_response = api_instance.update_webhook_notification(scope, code, id, update_webhook_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->update_webhook_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 
 **update_webhook_notification** | [**UpdateWebhookNotification**](UpdateWebhookNotification.md)| The data to update a notification | 

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

