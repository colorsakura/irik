from api import create_api

api = create_api()

if __name__ == '__main__':

    from uvicorn import run
    run('main:api', reload=True)
