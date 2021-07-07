"""
created by Nagaj at 06/07/2021
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health():
    return {"status": "ok"}
