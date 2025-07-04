# coding: utf-8

"""
    Femsa API

    Femsa sdk

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@femsa.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from digitalfemsa.models.charge_response_channel import ChargeResponseChannel
from digitalfemsa.models.charge_response_refunds import ChargeResponseRefunds
from digitalfemsa.models.payment_method_cash import PaymentMethodCash
from typing import Optional, Set
from typing_extensions import Self

class ChargeResponse(BaseModel):
    """
    ChargeResponse
    """ # noqa: E501
    amount: Optional[StrictInt] = None
    channel: Optional[ChargeResponseChannel] = None
    created_at: Optional[StrictInt] = None
    currency: Optional[StrictStr] = None
    customer_id: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    device_fingerprint: Optional[StrictStr] = None
    failure_code: Optional[StrictStr] = None
    failure_message: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    livemode: Optional[StrictBool] = None
    object: Optional[StrictStr] = None
    order_id: Optional[StrictStr] = None
    paid_at: Optional[StrictInt] = None
    payment_method: Optional[PaymentMethodCash] = None
    reference_id: Optional[StrictStr] = Field(default=None, description="Reference ID of the charge")
    refunds: Optional[ChargeResponseRefunds] = None
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["amount", "channel", "created_at", "currency", "customer_id", "description", "device_fingerprint", "failure_code", "failure_message", "id", "livemode", "object", "order_id", "paid_at", "payment_method", "reference_id", "refunds", "status"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ChargeResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of channel
        if self.channel:
            _dict['channel'] = self.channel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['payment_method'] = self.payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refunds
        if self.refunds:
            _dict['refunds'] = self.refunds.to_dict()
        # set to None if paid_at (nullable) is None
        # and model_fields_set contains the field
        if self.paid_at is None and "paid_at" in self.model_fields_set:
            _dict['paid_at'] = None

        # set to None if reference_id (nullable) is None
        # and model_fields_set contains the field
        if self.reference_id is None and "reference_id" in self.model_fields_set:
            _dict['reference_id'] = None

        # set to None if refunds (nullable) is None
        # and model_fields_set contains the field
        if self.refunds is None and "refunds" in self.model_fields_set:
            _dict['refunds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChargeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "channel": ChargeResponseChannel.from_dict(obj["channel"]) if obj.get("channel") is not None else None,
            "created_at": obj.get("created_at"),
            "currency": obj.get("currency"),
            "customer_id": obj.get("customer_id"),
            "description": obj.get("description"),
            "device_fingerprint": obj.get("device_fingerprint"),
            "failure_code": obj.get("failure_code"),
            "failure_message": obj.get("failure_message"),
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "object": obj.get("object"),
            "order_id": obj.get("order_id"),
            "paid_at": obj.get("paid_at"),
            "payment_method": PaymentMethodCash.from_dict(obj["payment_method"]) if obj.get("payment_method") is not None else None,
            "reference_id": obj.get("reference_id"),
            "refunds": ChargeResponseRefunds.from_dict(obj["refunds"]) if obj.get("refunds") is not None else None,
            "status": obj.get("status")
        })
        return _obj


