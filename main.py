from typing import Union
from fastapi import FastAPI, Depends
from src.application.routers import users


app = FastAPI()
app.include_router(users.router)

@app.get("/")
async def home():
    return {"status": "ok"}

class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/search")
async def search(commons: CommonQueryParams = Depends(CommonQueryParams)):
    return {"commons": commons}