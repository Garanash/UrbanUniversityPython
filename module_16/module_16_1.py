import fastapi

app = fastapi.FastAPI()


@app.get('/')
async def main() -> dict:
    return {"message": "main page"}


@app.get('/admin')
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def count_user(user_id) -> dict:
    return {"message": f"user number {user_id}"}


@app.get("/user")
async def userinfo(user_name: str = 'None', user_age: int = 0) -> dict:
    return {"message": f"user name: {user_name} number {user_age}"}
