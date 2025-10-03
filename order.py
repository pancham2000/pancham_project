from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from login import Login, User

class Ord(BaseModel):
    brand : str
    model : str
    price : int

class OrderRequest(BaseModel):
    user: User
    order: Ord

class Order(Login):
    #if login success then only i need to able to order the product 
    @staticmethod
    def order_car(request: OrderRequest):
        auth_response = Login.authenticate(request.user)
        if auth_response.get("message") == "Login successful!":
            return {
                "message": f"Order placed successfully for {request.user.username}",
                "order": "order details",
                "brand": request.order.brand,
                "model": request.order.model,
                "price": request.order.price
            }
        raise HTTPException(status_code=401, detail="Order failed due to authentication error!")