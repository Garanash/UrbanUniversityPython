
from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn

app = FastAPI()

@app.get('/')
async def root_route() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def path_route() -> str:
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def parameter_route(user_id : int = Path(ge=1, le=100, description='Enter User ID', example='1')) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user/{username}/{age}')
async def parameter_route2(
        username : Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
        age : int = Path(ge=5, le=20, description='Enter age')
    ) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
