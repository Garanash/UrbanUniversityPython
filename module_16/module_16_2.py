from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/')
async def main() -> dict:
    return {"message": "main page"}


@app.get('/user/{user_id}')
async def id_info(user_id: Annotated[int, Path(ge=1,
                                               le=100,
                                               discription='Enter User ID',
                                               example=75)]) -> dict:
    return {"message": 'your data is valid'}


@app.get('/user/{user_name}/{user_age}')
async def user_info(user_name: Annotated[str, Path(min_length=5,
                                                   max_length=20,
                                                   discription='enter username',
                                                   example="Andrey")],
                    user_age: Annotated[int, Path(ge=18,
                                                  le=120,
                                                  discription='enter age',
                                                  example=75)]) -> dict:
    return {"message": "your data is valid"}
