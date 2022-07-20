from fastapi import APIRouter, HTTPException
from src.domain.user.user_entity import User, UserDTO


router = APIRouter(
    prefix="/users",
    tags=["users"],
    # TODO dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Não encontrado"}},
)

@router.post("/", description="Api to save user", status_code=201)
async def save_user(user_props: UserDTO):
    user = User(user_props)
    return {"user": user}

@router.get("/", description="Api to list users")
async def users():
    return [User(user_props=UserDTO(age=0))]
