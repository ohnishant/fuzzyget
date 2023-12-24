from typing import Union
from fastapi import FastAPI, status

from .logger import get_logger

from .finder import find

LOGGER = get_logger()

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/search/{user}/{phrase}")
async def search(user: str, phrase: str):
    search_results = " | ".join(await find(user=user, phrase=phrase))
    " | ".join(search_results)
    return {"matches": search_results}


@app.get("/")
@app.get("/health", status_code=status.HTTP_200_OK)
async def check_health():
    return {"status": "OK"}
