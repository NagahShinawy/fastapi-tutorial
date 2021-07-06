"""
created by Nagaj at 06/07/2021
"""
import logging
from http import HTTPStatus
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/users", status_code=HTTPStatus.OK)
def users():
    return {
        "data": [
            {"id": 1, "username": "John", "email": "john@test.com"},
            {"id": 2, "username": "james", "email": "james@test.com"},
        ]
    }


@app.post("/users", status_code=HTTPStatus.CREATED)
def users():
    return {
        "data": [
            {"id": 3, "username": "Leon", "email": "leon@test.com"},
        ],
        "msg": "user <leon> was created"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
