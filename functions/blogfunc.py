from models import Blog
from fastapi import HTTPException, status

def get_all_blogs(db):
    blog_model = db.query(Blog).filter().all()
    if blog_model is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Blog is found in database") 
    return blog_model

def get_blog_by_id(db, blog_id):
    blog_model = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog_model is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="blog not found")
    return blog_model

def create_a_blog(db, blog_request):
    blog_model =  Blog(
        title=blog_request.title,
        body=blog_request.body,
        user_id=1
    )

    db.add(blog_model)
    db.commit()
    if blog_model:
        return {"data": "Blog has been created"}


def update_a_blog(db, blog_id, blog_request):
    db.query(Blog).filter(Blog.email == blog_id).update(blog_request.model_dump())
    db.commit()
    

def delete_a_blog(db, blog_id):
    blog_model = db.query(Blog).filter(Blog.email == blog_id).first()

    if blog_model is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="blog does not exist")
    
    db.query(Blog).filter(Blog.email == blog_id).delete()
    db.commit()