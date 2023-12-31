# core.ils.client
Neoception® Intralogistics Suite is a collection of modules for automation in the context of manufacturing.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://www.neoception.com/intralogistics-suite/](https://www.neoception.com/intralogistics-suite/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import core.ils.client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import core.ils.client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = core.ils.client.AboutApi(core.ils.client.ApiClient(configuration))

try:
    api_response = api_instance.about()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.ils.neoception.dev/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AboutApi* | [**about**](docs/AboutApi.md#about) | **GET** /about | 
*CarrierApi* | [**dissociate_card_from_carrier**](docs/CarrierApi.md#dissociate_card_from_carrier) | **DELETE** /v1beta1/kanban/carriers/{carrierId}:dissociate-card | Remove the association between the specified Carrier and a Kanban Card.
*DeviceApi* | [**delete_device_by_id**](docs/DeviceApi.md#delete_device_by_id) | **DELETE** /v1/core/devices/{deviceId} | Delete a Device by id.
*DeviceApi* | [**get_detailed_device_by_id**](docs/DeviceApi.md#get_detailed_device_by_id) | **GET** /v1/core/devices/{deviceId}:detailed | Get a Device by id, detailed.
*DeviceApi* | [**get_device_by_id**](docs/DeviceApi.md#get_device_by_id) | **GET** /v1/core/devices/{deviceId} | Get a Device by id.
*DeviceApi* | [**get_device_settings_by_device_id**](docs/DeviceApi.md#get_device_settings_by_device_id) | **GET** /v1/core/devices/{deviceId}/settings | Get all Settings of a Device by id.
*DeviceApi* | [**get_device_tags_by_device_id**](docs/DeviceApi.md#get_device_tags_by_device_id) | **GET** /v1/core/devices/{deviceId}/tags | Get all Tags of a Device by id.
*DeviceApi* | [**get_devices**](docs/DeviceApi.md#get_devices) | **GET** /v1beta1/core/devices | Get all Devices, paginated.
*DeviceApi* | [**get_devices1**](docs/DeviceApi.md#get_devices1) | **GET** /v1/core/devices | Get all Devices, paginated.
*DeviceApi* | [**remove_device_tag**](docs/DeviceApi.md#remove_device_tag) | **DELETE** /v1/core/devices/{deviceId}/tags/{tag} | Remove a Tag from Device, if assigned already.
*DeviceApi* | [**update_device_name**](docs/DeviceApi.md#update_device_name) | **PATCH** /v1/core/devices/{deviceId}:rename | Rename a Device.
*DeviceApi* | [**update_device_settings**](docs/DeviceApi.md#update_device_settings) | **PATCH** /v1/core/devices/{deviceId}/settings | Update Settings of a Device.
*DeviceApi* | [**update_device_tag**](docs/DeviceApi.md#update_device_tag) | **PATCH** /v1/core/devices/{deviceId}/tags/{tag} | Add a Tag to a Device, if not assigned already.
*DeviceApi* | [**update_device_tags**](docs/DeviceApi.md#update_device_tags) | **PUT** /v1/core/devices/{deviceId}/tags | Replace all Tags of a Device.
*DeviceGroupApi* | [**delete_device_group_by_id**](docs/DeviceGroupApi.md#delete_device_group_by_id) | **DELETE** /v1/core/device-groups/{deviceGroupId} | Delete a Device Group by id.
*DeviceGroupApi* | [**get_detailed_device_group_by_id**](docs/DeviceGroupApi.md#get_detailed_device_group_by_id) | **GET** /v1/core/device-groups/{deviceGroupId}:detailed | Get a Device Group by id, detailed.
*DeviceGroupApi* | [**get_device_group_by_id**](docs/DeviceGroupApi.md#get_device_group_by_id) | **GET** /v1/core/device-groups/{deviceGroupId} | Get a Device Group by id.
*DeviceGroupApi* | [**get_device_group_settings_by_device_id**](docs/DeviceGroupApi.md#get_device_group_settings_by_device_id) | **GET** /v1/core/device-groups/{deviceGroupId}/settings | Get all Settings of a Device Group by id.
*DeviceGroupApi* | [**get_device_groups**](docs/DeviceGroupApi.md#get_device_groups) | **GET** /v1/core/device-groups | Get all Device Groups, paginated.
*DeviceGroupApi* | [**get_device_tags_by_device_id1**](docs/DeviceGroupApi.md#get_device_tags_by_device_id1) | **GET** /v1/core/device-groups/{deviceGroupId}/tags | Get all Tags of a Device Group by id.
*DeviceGroupApi* | [**remove_device_group_tag**](docs/DeviceGroupApi.md#remove_device_group_tag) | **DELETE** /v1/core/device-groups/{deviceGroupId}/tags/{tag} | Remove a Tag from Device Group, if assigned already.
*DeviceGroupApi* | [**update_device_group_name**](docs/DeviceGroupApi.md#update_device_group_name) | **PATCH** /v1/core/device-groups/{deviceGroupId}:rename | Rename a Device Group.
*DeviceGroupApi* | [**update_device_group_settings**](docs/DeviceGroupApi.md#update_device_group_settings) | **PATCH** /v1/core/device-groups/{deviceGroupId}/settings | Update Settings of a Device Group.
*DeviceGroupApi* | [**update_device_group_tag**](docs/DeviceGroupApi.md#update_device_group_tag) | **PATCH** /v1/core/device-groups/{deviceGroupId}/tags/{tag} | Add a Tag to a Device Group, if not assigned already.
*DeviceGroupApi* | [**update_device_group_tags**](docs/DeviceGroupApi.md#update_device_group_tags) | **PUT** /v1/core/device-groups/{deviceGroupId}/tags | Replace all Tags of a Device Group.
*IdentifierApi* | [**create_enrichment_schema**](docs/IdentifierApi.md#create_enrichment_schema) | **POST** /v1/core/identifiers/enrichment-schemas | Create a Schema.
*IdentifierApi* | [**delete_enrichment_by_identifier_id**](docs/IdentifierApi.md#delete_enrichment_by_identifier_id) | **DELETE** /v1/core/identifiers/{identifierId}/enrichments | Delete all Enrichments of an Identifier.
*IdentifierApi* | [**delete_enrichment_by_key_name_and_value**](docs/IdentifierApi.md#delete_enrichment_by_key_name_and_value) | **DELETE** /v1/core/identifiers/enrichments/{key}:{value}:by-key-and-value | Delete all enrichments from all identifiers where specific key and value are present.
*IdentifierApi* | [**find_enrichments_with_non_unique_values_by_key_name**](docs/IdentifierApi.md#find_enrichments_with_non_unique_values_by_key_name) | **GET** /v1/core/identifiers/enrichments/{key}:non-unique-values-by-key | Find all enrichments by identifier, where values occurring more than once, for a specific key.
*IdentifierApi* | [**generate_identifier**](docs/IdentifierApi.md#generate_identifier) | **PUT** /v1beta1/core/identifiers | Generate an identifier based on a code and salt (optional).
*IdentifierApi* | [**generate_identifier1**](docs/IdentifierApi.md#generate_identifier1) | **POST** /v1/core/identifiers | Generate an identifier based on a code and salt (optional).
*IdentifierApi* | [**get_enrichment_schema**](docs/IdentifierApi.md#get_enrichment_schema) | **GET** /v1/core/identifiers/enrichment-schemas/{name} | Get the Schema for a specific name.
*IdentifierApi* | [**get_enrichment_schemas**](docs/IdentifierApi.md#get_enrichment_schemas) | **GET** /v1/core/identifiers/enrichment-schemas | Get all Schemas.
*IdentifierApi* | [**get_identifier_by_id**](docs/IdentifierApi.md#get_identifier_by_id) | **GET** /v1/core/identifiers/{identifierId} | Get an Identifier by id.
*IdentifierApi* | [**get_identifiers**](docs/IdentifierApi.md#get_identifiers) | **GET** /v1/core/identifiers | Get all identifiers, paginated.
*IdentifierApi* | [**patch_enrichment_by_identifier_id**](docs/IdentifierApi.md#patch_enrichment_by_identifier_id) | **PATCH** /v1/core/identifiers/{identifierId}/enrichments | Add or Update specific Enrichments of an Identifier.
*IdentifierApi* | [**update_enrichment_by_identifier_id**](docs/IdentifierApi.md#update_enrichment_by_identifier_id) | **PUT** /v1/core/identifiers/{identifierId}/enrichments | Override all Enrichments of an Identifier.
*IdentifierApi* | [**update_enrichment_schema**](docs/IdentifierApi.md#update_enrichment_schema) | **PUT** /v1/core/identifiers/enrichment-schemas/{name} | Update the Schema for a specific name.
*KanbanControlCycleApi* | [**assign_kanban_card_to_carrier**](docs/KanbanControlCycleApi.md#assign_kanban_card_to_carrier) | **PUT** /v1beta1/kanban/control-cycles/{controlCycleId}/cards:associate-carrier/{carrierId} | Assign a free Kanban Card, from a specific Kanban Control Cycle, to a Carrier.
*KanbanControlCycleApi* | [**associate_lane_to_kanban_control_cycle**](docs/KanbanControlCycleApi.md#associate_lane_to_kanban_control_cycle) | **PUT** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes:associate-lane/{laneId} | Associate a Lane to a Kanban Control Cycle.
*KanbanControlCycleApi* | [**associate_lane_to_kanban_control_cycle1**](docs/KanbanControlCycleApi.md#associate_lane_to_kanban_control_cycle1) | **PUT** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes:associate-lane/{address}:by-address | Associate a Lane to a Kanban Control Cycle.
*KanbanControlCycleApi* | [**create_kanban_control_cycle**](docs/KanbanControlCycleApi.md#create_kanban_control_cycle) | **POST** /v1beta1/kanban/control-cycles | Create a new Kanban Control Cycle.
*KanbanControlCycleApi* | [**dissociate_lane_to_kanban_control_cycle**](docs/KanbanControlCycleApi.md#dissociate_lane_to_kanban_control_cycle) | **DELETE** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes:dissociate-lane/{laneId} | Dissociate a Lane from a Kanban Control Cycle.
*KanbanControlCycleApi* | [**dissociate_lane_to_kanban_control_cycle1**](docs/KanbanControlCycleApi.md#dissociate_lane_to_kanban_control_cycle1) | **DELETE** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes:dissociate-lane/{address}:by-address | Dissociate a Lane from a Kanban Control Cycle.
*KanbanControlCycleApi* | [**get_kanban_control_cycle_by_external_id**](docs/KanbanControlCycleApi.md#get_kanban_control_cycle_by_external_id) | **GET** /v1beta1/kanban/control-cycles/{externalId}:by-external-id | Get Kanban Control Cycle by External Id.
*KanbanControlCycleApi* | [**get_kanban_control_cycle_by_id**](docs/KanbanControlCycleApi.md#get_kanban_control_cycle_by_id) | **GET** /v1beta1/kanban/control-cycles/{controlCycleId} | Get Kanban Control Cycle by Id.
*KanbanControlCycleApi* | [**get_kanban_control_cycle_cards**](docs/KanbanControlCycleApi.md#get_kanban_control_cycle_cards) | **GET** /v1beta1/kanban/control-cycles/{controlCycleId}/cards | Get all Kanban Cards of a Kanban Control Cycle.
*KanbanControlCycleApi* | [**get_kanban_control_cycle_lanes**](docs/KanbanControlCycleApi.md#get_kanban_control_cycle_lanes) | **GET** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes | Get all Lanes assigned to a Kanban Control Cycle.
*KanbanControlCycleApi* | [**get_kanban_control_cycles**](docs/KanbanControlCycleApi.md#get_kanban_control_cycles) | **GET** /v1beta1/kanban/control-cycles | Get all Kanban Control Cycles, paginated.
*KanbanControlCycleApi* | [**remove_card_from_kanban_control_cycle**](docs/KanbanControlCycleApi.md#remove_card_from_kanban_control_cycle) | **DELETE** /v1beta1/kanban/control-cycles/{controlCycleId}/cards/{cardId} | Remove a card from a Kanban Control Cycle.
*KanbanControlCycleApi* | [**remove_kanban_control_cycle**](docs/KanbanControlCycleApi.md#remove_kanban_control_cycle) | **DELETE** /v1beta1/kanban/control-cycles/{controlCycleId} | Remove a Kanban Control Cycle.
*KanbanControlCycleApi* | [**update_kanban_control_cycle**](docs/KanbanControlCycleApi.md#update_kanban_control_cycle) | **PUT** /v1beta1/kanban/control-cycles/{controlCycleId} | Update a Kanban Control Cycle.
*LaneApi* | [**get_lane**](docs/LaneApi.md#get_lane) | **GET** /v1beta1/kanban/lanes/{laneId} | Get a Lane by id.
*LaneApi* | [**get_lane_by_address**](docs/LaneApi.md#get_lane_by_address) | **GET** /v1beta1/kanban/lanes/{address}:by-address | Get a Lane by address.
*LaneApi* | [**get_lane_stock_trigger**](docs/LaneApi.md#get_lane_stock_trigger) | **GET** /v1beta1/kanban/lanes/{laneId}/triggers:stock | Get a Lane&#x27;s Stock Trigger.
*LaneApi* | [**get_lanes**](docs/LaneApi.md#get_lanes) | **GET** /v1beta1/kanban/lanes | Get all Lanes, paginated.
*LaneApi* | [**get_lanes_carriers**](docs/LaneApi.md#get_lanes_carriers) | **GET** /v1beta1/kanban/lanes/{laneId}/carriers | Get all Carriers currently allocated to a Lane, paginated.
*LaneApi* | [**get_lanes_carriers1**](docs/LaneApi.md#get_lanes_carriers1) | **GET** /v1beta1/kanban/lanes/carriers | Get all Carriers currently allocated to all Lanes, paginated.
*LaneApi* | [**remove_lane_stock_trigger**](docs/LaneApi.md#remove_lane_stock_trigger) | **DELETE** /v1beta1/kanban/lanes/{laneId}/triggers:stock | Remove a Lane&#x27;s Stock Trigger.
*LaneApi* | [**set_lane_stock_trigger**](docs/LaneApi.md#set_lane_stock_trigger) | **PUT** /v1beta1/kanban/lanes/{laneId}/triggers:stock/{threshold} | Set a Lane&#x27;s Stock Trigger.
*OperationsApi* | [**request_blink_operation**](docs/OperationsApi.md#request_blink_operation) | **PUT** /v1/core/operations/set-light | Broadcast a Blink operation to all eligible Devices and/or Device Groups.
*OperationsApi* | [**request_configure_put_to_light_for_lanes**](docs/OperationsApi.md#request_configure_put_to_light_for_lanes) | **PUT** /v1beta1/kanban/operations/put-to-light:configure | Configure Put To Light for specified Lanes.
*OperationsApi* | [**request_put_to_light_for_carrier**](docs/OperationsApi.md#request_put_to_light_for_carrier) | **PUT** /v1beta1/kanban/operations/put-to-light | Broadcast a Put To Light request for the specified Carrier.
*OperationsApi* | [**request_rfid_scan_operation**](docs/OperationsApi.md#request_rfid_scan_operation) | **PUT** /v1/core/operations/rfid-scan | Broadcast a RFID Scan operation to all eligible Devices and/or Device Groups.
*OperationsApi* | [**request_set_image_operation**](docs/OperationsApi.md#request_set_image_operation) | **PUT** /v1beta1/kanban/operations/set-image | Broadcast a Set Image operation to all eligible Device
*OperationsApi* | [**request_set_image_operation1**](docs/OperationsApi.md#request_set_image_operation1) | **PUT** /v1/core/operations/set-image | Broadcast a Set Image operation to all eligible Device and/or Device Groups.
*OperationsApi* | [**request_set_light**](docs/OperationsApi.md#request_set_light) | **PUT** /v1beta1/kanban/operations/set-light | Broadcast a Set Light request for the specified Lanes or Devices.
*OperationsApi* | [**request_test_me_device_group_operation**](docs/OperationsApi.md#request_test_me_device_group_operation) | **GET** /v1/core/operations/test-me-device-group | Finds all eligible Device Groups for the given criteria. Nothing gets broadcast to targets.
*OperationsApi* | [**request_test_me_device_operation**](docs/OperationsApi.md#request_test_me_device_operation) | **GET** /v1/core/operations/test-me-device | Finds all eligible Devices for the given criteria. Nothing gets broadcast to targets.

## Documentation For Models

 - [Carrier](docs/Carrier.md)
 - [CarrierPaginatedList](docs/CarrierPaginatedList.md)
 - [ConfigurePutToLightOperationBody](docs/ConfigurePutToLightOperationBody.md)
 - [DefaultResponse](docs/DefaultResponse.md)
 - [Device](docs/Device.md)
 - [DeviceDetailed](docs/DeviceDetailed.md)
 - [DeviceGroup](docs/DeviceGroup.md)
 - [DeviceGroupDetailed](docs/DeviceGroupDetailed.md)
 - [DeviceGroupPaginatedList](docs/DeviceGroupPaginatedList.md)
 - [DeviceGroupTagsList](docs/DeviceGroupTagsList.md)
 - [DeviceGroupUpdateSettingsBody](docs/DeviceGroupUpdateSettingsBody.md)
 - [DevicePaginatedList](docs/DevicePaginatedList.md)
 - [DeviceState](docs/DeviceState.md)
 - [DeviceTagsList](docs/DeviceTagsList.md)
 - [DeviceUpdateSettingsBody](docs/DeviceUpdateSettingsBody.md)
 - [EnrichmentSchema](docs/EnrichmentSchema.md)
 - [EnrichmentSchemaCreateBody](docs/EnrichmentSchemaCreateBody.md)
 - [EnrichmentSchemaKey](docs/EnrichmentSchemaKey.md)
 - [EnrichmentSchemaKeyRules](docs/EnrichmentSchemaKeyRules.md)
 - [EnrichmentSchemaList](docs/EnrichmentSchemaList.md)
 - [EnrichmentSchemaUpdateBody](docs/EnrichmentSchemaUpdateBody.md)
 - [Identifier](docs/Identifier.md)
 - [IdentifierCreate](docs/IdentifierCreate.md)
 - [IdentifierEnrichmentsDuplicatedOccurrence](docs/IdentifierEnrichmentsDuplicatedOccurrence.md)
 - [IdentifierEnrichmentsUpdateBody](docs/IdentifierEnrichmentsUpdateBody.md)
 - [IdentifierPaginatedList](docs/IdentifierPaginatedList.md)
 - [IdentifiersByEnrichmentValue](docs/IdentifiersByEnrichmentValue.md)
 - [KanbanControlCycle](docs/KanbanControlCycle.md)
 - [KanbanControlCycleCard](docs/KanbanControlCycleCard.md)
 - [KanbanControlCycleCardList](docs/KanbanControlCycleCardList.md)
 - [KanbanControlCycleCreateBody](docs/KanbanControlCycleCreateBody.md)
 - [KanbanControlCyclePaginatedList](docs/KanbanControlCyclePaginatedList.md)
 - [KanbanControlCycleUpdateBody](docs/KanbanControlCycleUpdateBody.md)
 - [Lane](docs/Lane.md)
 - [LaneCarrier](docs/LaneCarrier.md)
 - [LaneCarrierPaginatedList](docs/LaneCarrierPaginatedList.md)
 - [LaneList](docs/LaneList.md)
 - [LanePaginatedList](docs/LanePaginatedList.md)
 - [LaneTrigger](docs/LaneTrigger.md)
 - [PageMetadata](docs/PageMetadata.md)
 - [PutToLightOperationBody](docs/PutToLightOperationBody.md)
 - [SetImageOperationBody](docs/SetImageOperationBody.md)
 - [SetLightOperationBody](docs/SetLightOperationBody.md)
 - [State](docs/State.md)

## Documentation For Authorization


## token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## user

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://neoceptionidp.eu.auth0.com/authorize?audience=https://api.ils.neoception.dev
- **Scopes**: 


## Author

contact@neoception.com
