# Delivery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the delivery. | 
**event_id** | **str** | The identifier of the associated event. | 
**subscription_id** | [**ResourceId**](ResourceId.md) |  | 
**notification_id** | **str** | The identifier of the associated notification. | 
**delivery_channel** | **str** | The delivery channel of the message. | 
**message_details** | **str** | The Details of the delivery message as JSON string. | 
**attempts** | [**list[Attempt]**](Attempt.md) | A list of all the delivery attempts made for this message. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


