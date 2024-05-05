from fastapi import FastAPI
from .routers import client

app = FastAPI()

app.include_router(client.router)