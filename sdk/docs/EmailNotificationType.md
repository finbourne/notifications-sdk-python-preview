# EmailNotificationType

The information required to create or update an Email notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**subject** | **str** | The subject of the email | 
**plain_text_body** | **str** | The plain text body of the email | 
**html_body** | **str** | The HTML body of the email (if any) | [optional] 
**email_address_to** | **list[str]** | &#39;To&#39; recipients of the email | 
**email_address_cc** | **list[str]** | &#39;Cc&#39; recipients of the email | [optional] 
**email_address_bcc** | **list[str]** | &#39;Bcc&#39; recipients of the email | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


