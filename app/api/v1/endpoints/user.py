"""
created by Nagaj at 06/07/2021
"""
from app.config.logs import logger
from fastapi import APIRouter


router = APIRouter()


@router.post("/users/")
def create_user():
    return {"data": {}}


@router.get("/users/")
def get_users():
    return {"users": []}


@router.get("/user/{user_id}")
def get_user(user_id: int):
    logger.info(f"GETTING USER WITH PARAMS [user_id:{user_id}]")
    return {"user_id": user_id}
