from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas,database

router = APIRouter()


@router.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
def create_blog(request:schemas.Blog,db:Session=Depends(database.get_db)):
   new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
   db.add(new_blog)
   db.commit()
   db.refresh(new_blog)
   return new_blog

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete_blog(id:int,db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update_blog(id:int,request:schemas.Blog,db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Blog with id {id} not found')
    blog.update(request.model_dump())
    db.commit()
    return 'updated'

@router.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
def all_blogs(db:Session=Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return  blogs

@router.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog,tags=['blogs'])
def get_blog(id:int,db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Blog with id {id} not found')
    return blog
