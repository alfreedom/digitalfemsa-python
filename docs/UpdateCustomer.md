# UpdateCustomer

update customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antifraud_info** | [**UpdateCustomerAntifraudInfo**](UpdateCustomerAntifraudInfo.md) |  | [optional] 
**default_payment_source_id** | **str** | It is a parameter that allows to identify in the response, the Femsa ID of a payment method (payment_id) | [optional] 
**email** | **str** | An email address is a series of customizable characters followed by a universal Internet symbol, the at symbol (@), the name of a host server, and a web domain ending (.mx, .com, .org, . net, etc). | [optional] 
**name** | **str** | Client&#39;s name | [optional] 
**phone** | **str** | Is the customer&#39;s phone number | [optional] 
**default_shipping_contact_id** | **str** | It is a parameter that allows to identify in the response, the Femsa ID of the shipping address (shipping_contact) | [optional] 
**corporate** | **bool** | It is a value that allows identifying if the email is corporate or not. | [optional] [default to False]
**custom_reference** | **str** | It is an undefined value. | [optional] 
**fiscal_entities** | [**List[CustomerFiscalEntitiesRequest]**](CustomerFiscalEntitiesRequest.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**payment_sources** | [**List[CustomerPaymentMethodsRequest]**](CustomerPaymentMethodsRequest.md) | Contains details of the payment methods that the customer has active or has used in Femsa | [optional] 
**shipping_contacts** | [**List[CustomerShippingContacts]**](CustomerShippingContacts.md) | Contains the detail of the shipping addresses that the client has active or has used in Femsa | [optional] 

## Example

```python
from digitalfemsa.models.update_customer import UpdateCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomer from a JSON string
update_customer_instance = UpdateCustomer.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomer.to_json())

# convert the object into a dict
update_customer_dict = update_customer_instance.to_dict()
# create an instance of UpdateCustomer from a dict
update_customer_from_dict = UpdateCustomer.from_dict(update_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


