"""
created by Nagaj at 06/07/2021
"""
from fastapi import APIRouter
from app.api.v1.endpoints import root
from app.api.v1.endpoints import user
from app.api.v1.endpoints import book

api_root = APIRouter()
api_router = APIRouter()

api_root.include_router(root.router, tags=["Root"])
api_router.include_router(user.router, tags=["Users API"])
api_router.include_router(book.router, tags=["Book API"])
