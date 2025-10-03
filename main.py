from fastapi import FastAPI
from login import User, Login
from order import Order
import uvicorn

app = FastAPI()

app.post("/login")(Login.authenticate)
app.post("/order_car")(Order.order_car)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)