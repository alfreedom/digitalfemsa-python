# Customer

a customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antifraud_info** | [**CustomerAntifraudInfo**](CustomerAntifraudInfo.md) |  | [optional] 
**corporate** | **bool** | It is a value that allows identifying if the email is corporate or not. | [optional] [default to False]
**custom_reference** | **str** | It is an undefined value. | [optional] 
**email** | **str** | An email address is a series of customizable characters followed by a universal Internet symbol, the at symbol (@), the name of a host server, and a web domain ending (.mx, .com, .org, . net, etc). | 
**default_payment_source_id** | **str** | It is a parameter that allows to identify in the response, the Femsa ID of a payment method (payment_id) | [optional] 
**default_shipping_contact_id** | **str** | It is a parameter that allows to identify in the response, the Femsa ID of the shipping address (shipping_contact) | [optional] 
**fiscal_entities** | [**List[CustomerFiscalEntitiesRequest]**](CustomerFiscalEntitiesRequest.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**name** | **str** | Client&#39;s name | 
**payment_sources** | [**List[PaymentMethodCashRequest]**](PaymentMethodCashRequest.md) | Contains details of the payment methods that the customer has active or has used in Femsa | [optional] 
**phone** | **str** | Is the customer&#39;s phone number | 
**shipping_contacts** | [**List[CustomerShippingContacts]**](CustomerShippingContacts.md) | Contains the detail of the shipping addresses that the client has active or has used in Femsa | [optional] 

## Example

```python
from digitalfemsa.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


