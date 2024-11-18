from fastapi import APIRouter,HTTPException, Depends, status
from database import get_db 
from typing import Annotated, List
from sqlalchemy.orm import Session
from pmodels import BlogRequest, ShowBlog
from models import User
from functions.blogfunc import get_all_blogs, get_blog_by_id, create_a_blog, update_a_blog, delete_a_blog
from functions.Oauth2 import get_current_user

router = APIRouter(
    tags=["Blogs"],
    prefix="/blogs",
)

db_dependency = Annotated[Session, Depends(get_db)]
db_token = Annotated[User, Depends(get_current_user)]

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowBlog])
async def get_all(db: db_dependency , db_token: db_token):
    return get_all_blogs(db)


@router.get('/{blog_id}', status_code=status.HTTP_200_OK,  response_model=ShowBlog)
async def get_all(db: db_dependency, blog_id: int, db_token: db_token):
    return get_blog_by_id(db, blog_id)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_blog(db: db_dependency, blog_request: BlogRequest, db_token: db_token):
    return create_a_blog(db, blog_request)


@router.put('/update/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_blog(db: db_dependency, blog_id: int, blog_request:BlogRequest, db_token: db_token):
    return update_a_blog(db, blog_id, blog_request)
   
@router.delete('/delete/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(db: db_dependency, blog_id: int, db_token: db_token):
    return delete_a_blog(db, blog_id)