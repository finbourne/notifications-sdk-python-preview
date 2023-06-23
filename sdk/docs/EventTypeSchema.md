# EventTypeSchema

An EventType object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the event type | [optional] 
**display_name** | **str** | Identifier name of the event | [optional] 
**description** | **str** | The summary of the event | [optional] 
**application** | **str** | The application associated with the event | [optional] 
**header_schema** | [**list[EventFieldDefinition]**](EventFieldDefinition.md) | The header schema for the event type | [optional] [readonly] 
**body_schema** | [**list[EventFieldDefinition]**](EventFieldDefinition.md) | The body schema for the event type | [optional] [readonly] 
**href** | **str** | A URI for retrieving this schema | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


