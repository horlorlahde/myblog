from models import User
from fastapi import HTTPException, status
from functions.hashingfunc import Hash

def get_all_users(db):
    user_model = db.query(User).filter().all()
    return user_model

def get_user_by_email(db, user_email):
    user_model = db.query(User).filter(User.email == user_email).first()
    if user_model is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_model

def create_a_user(db, user_request):
    user_model = User(
        fullname=user_request.fullname,
        email=user_request.email,
        password=Hash.bcrypt(user_request.password)
    )

    db.add(user_model)
    db.commit()
    if user_model:
        return {"data": f"an accout has been created successfully with {user_model.email}"}


def update_a_user(db, user_email, user_request):
    db.query(User).filter(User.email == user_email).update(user_request.model_dump())
    db.commit()
    

def delete_a_user(db, user_email):
    user_model = db.query(User).filter(User.email == user_email).first()

    if user_model is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist")
    
    db.query(User).filter(User.email == user_email).delete()
    db.commit()


