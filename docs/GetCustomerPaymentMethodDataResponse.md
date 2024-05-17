# GetCustomerPaymentMethodDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**barcode_url** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from digitalfemsa.models.get_customer_payment_method_data_response import GetCustomerPaymentMethodDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerPaymentMethodDataResponse from a JSON string
get_customer_payment_method_data_response_instance = GetCustomerPaymentMethodDataResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomerPaymentMethodDataResponse.to_json())

# convert the object into a dict
get_customer_payment_method_data_response_dict = get_customer_payment_method_data_response_instance.to_dict()
# create an instance of GetCustomerPaymentMethodDataResponse from a dict
get_customer_payment_method_data_response_from_dict = GetCustomerPaymentMethodDataResponse.from_dict(get_customer_payment_method_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


