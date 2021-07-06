"""
created by Nagaj at 06/07/2021
"""
from fastapi import APIRouter
from app.api.v1.endpoints import user
from app.api.v1.endpoints import book


api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(book.router)