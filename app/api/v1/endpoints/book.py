"""
created by Nagaj at 06/07/2021
"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/books/")
def create_book():
    return {"data": {}}


@router.get("/books/")
def get_books():
    return {"books": []}


@router.get("/book/{book_id}")
def get_book(book_id: int):
    return {"id": book_id}
