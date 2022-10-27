from fastapi import APIRouter

from .v1 import *

v1 = APIRouter(prefix='/v1')

v1.include_router(items)
v1.include_router(users)
