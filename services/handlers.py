from database import fakeDb
from fastapi import HTTPException


dB = fakeDb.db
order_id = 0

def create_order(amount: float):

    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    global order_id
    order_id += 1
    curr_id = order_id
    dB[curr_id] = {
        "status": "Created",
        "amount": amount
    }

    print(dB)
    return {
        "order_id": curr_id,
        "status": "Created"
    }


def pay(curr_id: int, payment: float):
    if curr_id not in dB:
        raise HTTPException(status_code=404, detail="Order not found")
    order = dB[curr_id]

    if payment <= 0:
        raise HTTPException(status_code=400, detail="Payment must be positive")

    if order["status"] == "Completed":
        raise HTTPException(status_code=400, detail="Payment has been done already")

    if payment > order["amount"]:
        raise HTTPException(status_code=400, detail="Amount exceeds order amount")

    if payment < order["amount"]:
        remaining = order["amount"] - payment
        order["status"] = "Pending"
        order["amount"] = remaining

        return {
            "order_id": curr_id,
            "status": order["status"],
            "remaining": order["amount"],
        }

    elif payment == order["amount"]:
        order["status"] = "Completed"
        order["amount"] = 0

        return {
            "order_id": curr_id,
            "status": "Completed",
            "remaining": order["amount"]

        }





def get_status(curr_id: int):
    if curr_id not in dB:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "status": dB[curr_id]["status"],
        "amount": dB[curr_id]["amount"]
    }
