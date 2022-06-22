from fastapi import FastAPI

from src.domain.user.user_entity import User, UserDTO

app = FastAPI()


@app.post("/")
async def users(user_props: UserDTO):
    user = User(user_props)
    return {"user": user}
