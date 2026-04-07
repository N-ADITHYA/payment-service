from fastapi import FastAPI
from routes.order_routes import router

app = FastAPI()
app.include_router(router)




# ----------------------------------------------------------
#
# dB = {}
# # amP = {}
# @app.post("/create_order")
# def create_order(amount: float):
#     stat = {}
#     global order_id
#     order_id += 1
#     curr_id = order_id
#     stat["status"] = ("Created")
#     stat["amount"] = amount
#     dB[curr_id] = stat
#
#     print(dB)
#     return curr_id
#
# # order_id += 1
# @app.post("/pay")
# def paym(curr_id: int, payment: float):
#     if curr_id in dB:
#         if dB[curr_id]["status"] != "Completed":
#             if payment > 0:
#                 if dB[curr_id]["amount"] == payment:
#                     dB[curr_id]["status"] = "Completed"
#                     dB[curr_id]["amount"] = 0
#                     print(dB)
#                     return "Payment Done"
#                 elif payment > 0 and payment < dB[curr_id]["amount"]:
#                     remaining = dB[curr_id]["amount"] - payment
#                     dB[curr_id]["amount"] = remaining
#                     dB[curr_id]["status"] = "Pending"
#                     return f"amount recieved is {payment}, remaining to be paid is {remaining} by the user {curr_id}"
#                 else:
#                     return "You have entered an invalid amount"
#             else:
#                 return "Bro pay the right amount"
#         else:
#             return "Payment is Done"
#     else:
#          return "User does not exist"
#
#
# @app.get("/status")
# def getStatus():
#     return dB