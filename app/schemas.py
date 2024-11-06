from typing import List
from pydantic import BaseModel


class UserSchema(BaseModel):
    user_id: int
    name: str
    sex: str
    home_town: str


class GroupSchema(BaseModel):
    group_id: int
    name: str


class DetailedGroupSchema(GroupSchema):
    subscribers: List[UserSchema]


class DetailedUserSchema(UserSchema):
    follows: List[UserSchema]
    subscribes: List[GroupSchema]


class CreateUserSchema(UserSchema):
    follows: list[int]
    subscribes: list[int]


class CreateGroupSchema(GroupSchema):
    subscribers: list[int]
