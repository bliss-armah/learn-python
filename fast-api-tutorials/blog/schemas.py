from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    id:int
    title:str
    body:str


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]

class ShowBlog(Blog):
    id:int
    title:str
    body:str
    author: ShowUser