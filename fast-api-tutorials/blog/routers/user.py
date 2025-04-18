from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from .. import models,schemas,database
from ..repository import user



router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/',response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(database.get_db)):
    return user.show(id,db)