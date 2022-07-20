from fastapi import APIRouter
from src.domain.user.user_entity import User, UserDTO


# async def get_query_token(tokenzinho: str):
#     print('passou')
#     if tokenzinho != "jessica":
#         raise HTTPException(status_code=400, detail="No Jessica token provided")

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_query_token)],
    responses={404: {"description": "Não encontrado"}},
)

@router.post("", description="Api to save user", status_code=201)
async def save_user(user_props: UserDTO):
    user = User(user_props)
    return {"user": user}

@router.get("", description="Api to list users")
async def users():
    return [User(user_props=UserDTO(age=0))]
