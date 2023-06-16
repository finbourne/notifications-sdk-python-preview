# NotificationNotificationType

The type and contents of the notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**api_key_ref** | **str** | Reference to API key from Configuration Store | 
**api_secret_ref** | **str** | Reference to API secret from Configuration Store | 
**body** | **str** | The body of the SMS | 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | 
**http_method** | **str** | The HTTP method such as GET, POST, etc. to use on the request | 
**path_and_query** | **str** | The url to send the request to. | 
**content** | **object** | The content of the request | [optional] 
**subject** | **str** | The subject of the email | 
**plain_text_body** | **str** | The plain text body of the email | 
**html_body** | **str** | The HTML body of the email (if any) | [optional] 
**email_address_to** | **list[str]** | &#39;To&#39; recipients of the email | 
**email_address_cc** | **list[str]** | &#39;Cc&#39; recipients of the email | [optional] 
**email_address_bcc** | **list[str]** | &#39;Bcc&#39; recipients of the email | [optional] 
**recipients** | **list[str]** | The phone numbers to which the SMS will be sent to (E.164 format) | 
**url** | **str** | The URL to send the request to | 
**authentication_type** | **str** | The type of authentication to use on the request | 
**authentication_configuration_item_paths** | **dict[str, str]** | The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires &#39;Username&#39; and &#39;Password&#39;  - BearerToken - Requires &#39;BearerToken&#39; and optionally &#39;BearerScheme&#39;                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \&quot;authenticationType\&quot;: \&quot;BasicAuth\&quot;,      \&quot;authenticationConfigurationItemPaths\&quot;: {          \&quot;Username\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\&quot;,          \&quot;Password\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\&quot;      } | [optional] 
**content_type** | **str** | The type of the content e.g. Json | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


