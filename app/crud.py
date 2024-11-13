from app.models import User, UserInDB
from app.database import db
from app.auth import get_password_hash

async def create_user(user: User):
    user_in_db = UserInDB(
        **user.dict(), hashed_password=get_password_hash(user.password)
    )
    await db.users.insert_one(user_in_db.dict())
    return user_in_db

async def get_user_by_username(username: str):
    return await db.users.find_one({"username": username})

async def get_user_by_role(role: str):
    return await db.users.find_one({"role": role})

async def update_user(username: str, updated_user: User):
    await db.users.update_one({"username": username}, {"$set": updated_user.dict()})
