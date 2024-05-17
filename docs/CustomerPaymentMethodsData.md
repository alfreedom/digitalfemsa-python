# CustomerPaymentMethodsData


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
from digitalfemsa.models.customer_payment_methods_data import CustomerPaymentMethodsData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPaymentMethodsData from a JSON string
customer_payment_methods_data_instance = CustomerPaymentMethodsData.from_json(json)
# print the JSON string representation of the object
print(CustomerPaymentMethodsData.to_json())

# convert the object into a dict
customer_payment_methods_data_dict = customer_payment_methods_data_instance.to_dict()
# create an instance of CustomerPaymentMethodsData from a dict
customer_payment_methods_data_from_dict = CustomerPaymentMethodsData.from_dict(customer_payment_methods_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


