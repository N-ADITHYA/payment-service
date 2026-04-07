from pydantic import BaseModel
from decimal import Decimal

class CreateOrder(BaseModel):
    amount: Decimal

class PaymentModel(BaseModel):
    curr_id: int
    payment: Decimal

class StatusModel(BaseModel):
    curr_id: int


class CreateOrderOut(BaseModel):
    order_id: int
    status: str

class PaymentModelOut(BaseModel):
    order_id: int
    status: str
    remaining: Decimal | None = None

class StatusOut(BaseModel):
    status: str
    amount: Decimal