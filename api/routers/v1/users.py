from core.auth import AuthHandler
from fastapi import APIRouter, Depends, HTTPException
from scheams.users import AuthDetails

users = APIRouter(tags=["用户相关"])

auth_handler = AuthHandler()

user_list = []
login_users = {}


@users.post('/register', status_code=201)
async def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in user_list):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    user_list.append({
        'username': auth_details.username,
        'password': hashed_password
    })
    return {}


@users.post('/login', summary="登录")
async def login(auth_details: AuthDetails):
    user = None
    for x in user_list:
        if x['username'] == auth_details.username:
            user = x
            break

    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(
            status_code=401, detail='Invalid username or password')
    token = auth_handler.encode_token(user['username'])
    login_users.update({user['username']: token})
    return {"token": token}


@users.put('/logout')
async def logout():
    pass
