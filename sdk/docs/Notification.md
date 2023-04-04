# Notification

A notification object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the notification | 
**description** | **str** | The summary of the services provided by the notification | [optional] 
**display_name** | **str** | The name of the notification | [optional] 
**delivery_channel** | **str** | The medium through which the notification is delivered | 
**recipients** | **dict(str, object)** | Recipient of the notification | 
**content** | **dict(str, object)** | The contents of the notification | 
**status** | [**NotificationStatus**](NotificationStatus.md) |  | [optional] 
**created_at** | **datetime** | The time at which the subscription was made | 
**created_by** | **str** | The user who made the subscription | 
**last_modified_at** | **datetime** | The time at which the subscription was last modified | 
**last_modified_by** | **str** | The user who last modified the subscription | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


