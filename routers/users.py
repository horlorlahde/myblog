from fastapi import APIRouter, Depends, status
from database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session
from pmodels import UserRequest, ShowUser, ShowUserBlog
from functions.userfunc import get_all_users, get_user_by_email, create_a_user, update_a_user, delete_a_user


router = APIRouter(
    tags=["Users"],
    prefix="/users",
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowUserBlog])
async def get_all(db: db_dependency):
    return get_all_users(db)


@router.get('/{user_email}', status_code=status.HTTP_200_OK,  response_model=List[ShowUserBlog])
async def get_all(db: db_dependency, user_email: str):
    return get_user_by_email(db, user_email)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    return create_a_user(db, user_request)


@router.put('/update/{user_email}', status_code=status.HTTP_204_NO_CONTENT)
async def update_user(db: db_dependency, user_email: str, user_request: UserRequest):
    return update_a_user(db, user_email, user_request)
   
@router.delete('/delete/{user_email}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_dependency, user_email: str):
    return delete_a_user(db, user_email)