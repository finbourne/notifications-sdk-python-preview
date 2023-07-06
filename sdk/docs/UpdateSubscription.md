# UpdateSubscription

The information required to update a subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the subscription | 
**description** | **str** | The summary of the services provided by the subscription | 
**status** | **str** | The current status of the subscription. Possible values are: Active, Inactive | 
**matching_pattern** | [**MatchingPattern**](MatchingPattern.md) |  | 
**use_as_auth** | **str** | Id of user associated with subscription. All events associated with   the subscription will use this user to check entitlements against   the resource to send a notification. Can be null, in which case   we&#39;ll default to that of the user making this request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


