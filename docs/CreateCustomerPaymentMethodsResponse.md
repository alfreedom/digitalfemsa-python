# CreateCustomerPaymentMethodsResponse


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
from digitalfemsa.models.create_customer_payment_methods_response import CreateCustomerPaymentMethodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerPaymentMethodsResponse from a JSON string
create_customer_payment_methods_response_instance = CreateCustomerPaymentMethodsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerPaymentMethodsResponse.to_json())

# convert the object into a dict
create_customer_payment_methods_response_dict = create_customer_payment_methods_response_instance.to_dict()
# create an instance of CreateCustomerPaymentMethodsResponse from a dict
create_customer_payment_methods_response_from_dict = CreateCustomerPaymentMethodsResponse.from_dict(create_customer_payment_methods_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


