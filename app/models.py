from pydantic import BaseModel
from typing import Optional

# Basic user schema
class User(BaseModel):
    username: str
    email: str
    password: str
    role: Optional[str] = "user"  # Default role is "user"

# User schema for DB (with hashed password)
class UserInDB(User):
    hashed_password: str

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str
