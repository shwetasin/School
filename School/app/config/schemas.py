from typing import Optional
from pydantic import BaseModel
import datetime
from app.config import model


class School(BaseModel):
    id:int
    designation:str
    name:str
    phone_number:int
    
    class Config:
        orm_mode=True

class Classes(BaseModel):
    id:int
    techers_id:int
    name_of_student:str



    class Config:
        orm_mode=True

class getPayloadSchool(BaseModel):
    id:str

    class Config:
        orm_mode=True

class getPayloadClass(BaseModel):
    id:int

    class Config:
        orm_mode=True