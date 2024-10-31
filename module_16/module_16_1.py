import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root_route() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def path_route() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def parameter_route(user_id) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def query_route(username='NoName', age='NoAge') -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
