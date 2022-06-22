from pydantic import BaseModel

class UserDTO (BaseModel):
    age: int

class User ():
    age: int

    def __init__(self, user_props: UserDTO):
        self.age = user_props.age