from typing import Union

from fastapi import APIRouter

items = APIRouter(tags=["未知"])


@items.get('/search')
async def search(keyword: Union[str, None] = None, page: int = 1, limit: int = 20):
    return {"msg": "success", "data": {"keyword": keyword}}
