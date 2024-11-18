from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated, List
from database import get_db
from models import User
from pmodels import Login, Token
from functions.hashingfunc import Hash
from routers.token import create_access_token
from fastapi.security import  OAuth2PasswordRequestForm


router = APIRouter(
    tags=["Login Authentication"],
    prefix="/login"
)
db_dependency = Annotated[Session, Depends(get_db)]

@router.post('/', response_model=Token)
async def login(db: db_dependency, login_request: OAuth2PasswordRequestForm = Depends()):
    user_model = db.query(User).filter(User.email == login_request.username).first()
    if not user_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if  not Hash.verify(login_request.password, user_model.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password")
    
    access_token = create_access_token(data={"sub": user_model.email})
    return {"access_token": access_token, "token_type": "bearer"}