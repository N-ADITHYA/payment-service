from fastapi import APIRouter
from services import handlers
from schemas.model import CreateOrder, PaymentModel, PaymentModelOut, CreateOrderOut, StatusOut
router = APIRouter()

@router.post("/create_order", response_model=CreateOrderOut)
def create(pay: CreateOrder):
    return handlers.create_order(pay.amount)

@router.post("/pay", response_model=PaymentModelOut)
def pay(req: PaymentModel):
    return handlers.pay(req.curr_id, req.payment)

@router.get("/status/{curr_id}", response_model=StatusOut)
def orders(curr_id: int):
    return handlers.get_status(curr_id)


