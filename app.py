from fastapi import FastAPI
from urllib.parse import quote
import requests

app = FastAPI()

@app.get("/card/{name}")
def user_input_name(name):
    card_name = "https://api.scryfall.com/cards/named?exact=" + quote(name)
    response = requests.get(card_name)
    data = response.json()

    return {
    "name": data["name"],
    "mana_cost": data["mana_cost"],
    "type_line": data["type_line"],
    "image_url": data["image_uris"]["large"]
    }

from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory=".", html=True), name="static")
# @app.get("/")
# def read_root():
#     return {"message": "Hello, MTG!"}

