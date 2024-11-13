# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello, World!",
        "message2":"This application is based on jwt"

    }
