from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
# only get 10 published blogs
    if published:
        return {'data':f'{limit} published blogs from the database'}
    else:
       return {'data':f'{limit} blogs from the database'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blog'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    publise: Optional[bool]


@app.post('/post')
def create_blog(request:Blog):
    return {'data':f'Created blog with titile as {request.title}'}