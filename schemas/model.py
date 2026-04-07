from pydantic import BaseModel

class CreateOrder(BaseModel):
    amount: float

class PaymentModel(BaseModel):
    curr_id: int
    payment: float

class StatusModel(BaseModel):
    curr_id: int


class CreateOrderOut(BaseModel):
    order_id: int
    status: str

class PaymentModelOut(BaseModel):
    order_id: int
    status: str
    remaining: float | None = None

class StatusOut(BaseModel):
    status: str
    amount: float