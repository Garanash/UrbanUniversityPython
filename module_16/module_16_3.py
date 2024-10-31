import warnings
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path

warnings.filterwarnings("ignore", category=DeprecationWarning)

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='SomeUser')],
        age: Annotated[str, Path(min_length=1, max_length=3, description='Enter user age', example='25')]
) -> str:
    new_key = str(int(max(users.keys())) + 1 if users else 1)
    # new_key = str(int(list(users.keys())[-1]) + 1 if users else 1)
    users[new_key] = f'Имя: {username}, возраст: {age}'
    return f'User {new_key} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[str, Path(min_length=1, max_length=3, description='Enter user id', example='111')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='SomeUser')],
        age: Annotated[str, Path(min_length=1, max_length=3, description='Enter user age', example='25')]
) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[str, Path(min_length=1, max_length=3, description='Enter user id', example='111')]
) -> str:
    del users[user_id]
    return f'User {user_id} is deleted'


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
