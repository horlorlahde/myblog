from pydantic import BaseModel
from typing import List, Optional

class UserRequest(BaseModel):
    fullname : str
    email : str
    password: str

class ShowUser(BaseModel):
    class Config:
        orm_mode = True
    fullname : str
    email : str

class BlogRequest(BaseModel):
    title : str
    body: str
    

class ShowBlog(BlogRequest):
    class Config:
        orm_mode = True
    title : str
    body: str
    creator: ShowUser

class ShowUserBlog(ShowUser):
    blog: List[BlogRequest]

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None