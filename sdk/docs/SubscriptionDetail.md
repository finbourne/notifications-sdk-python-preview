# SubscriptionDetail

Subscription that contains its list of notifications

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications** | [**list[Notification]**](Notification.md) | List of notifications belonging to a subscription | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the subscription | 
**description** | **str** | The summary of the services provided by the subscription | [optional] 
**status** | **str** | The current status of the subscription | 
**matching_pattern** | [**MatchingPattern**](MatchingPattern.md) |  | 
**created_at** | **datetime** | The time at which the subscription was made | 
**created_by** | **str** | The user who made the subscription | 
**last_modified_at** | **datetime** | The time at which the subscription was last modified | 
**last_modified_by** | **str** | The user who last modified the subscription | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


