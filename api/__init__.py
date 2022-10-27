from fastapi import FastAPI

from api.routers import v1


from api.version import API_VERSION


def create_api() -> FastAPI:
    api = FastAPI(version=API_VERSION)
    api.include_router(v1, prefix='/api')
    return api
