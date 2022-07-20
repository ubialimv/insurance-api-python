from fastapi import FastAPI
from src.application.routers import users


app = FastAPI()
app.include_router(users.router)

@app.get("/")
async def home():
    return {"status": "ok"}
