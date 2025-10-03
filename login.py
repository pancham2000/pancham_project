from pydantic import BaseModel
from fastapi import HTTPException

class User(BaseModel):
    username: str
    password: str

class Login:
    def authenticate(user: User):
        if user.username == "Pancham" and user.password == "pancham1234":
            return {"message": "Login successful!"}
        raise HTTPException(status_code=401, detail="Login failed!")
