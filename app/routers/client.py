from fastapi import APIRouter
from app.models import Client

router = APIRouter()

@router.post("/client")
def get_client(client: Client):
    collection = {
        0: "Jacob",
        1: "Felipe"
    }
    return {"message": f"Your client id is {client.id}, with name {collection[client.id]}"}