import warnings
from typing import Annotated, List

import uvicorn
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

warnings.filterwarnings("ignore", category=DeprecationWarning)

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: list[User] = []


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='SomeUser')],
        age: Annotated[int, Path(ge=1, le=100, description='Enter user age', example=25)]
) -> User:
    user = User(id=len(users) + 1 if users else 1, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, lt=1000, description='Enter user id', example=111)],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='SomeUser')],
        age: Annotated[int, Path(ge=1, le=100, description='Enter user age', example=25)]
) -> User:
    try:
        user = next(user for user in users if user.id == user_id)
        user.username = username
        user.age = age
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"User with user_id {user_id} was not found")


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=1, lt=1000, description='Enter user id', example=111)]
) -> User:
    try:
        user = next(user for user in users if user.id == user_id)
        return users.pop(users.index(user))
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
