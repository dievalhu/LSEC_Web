from typing import Optional
from pydantic   import BaseModel

class User(BaseModel):
    id: Optional[int]
    name: str
    email:str    
    password: str

class Palabra(BaseModel):
    id_palabra: Optional[int]
    palabra: str
    descripcion: str    
    video: str

class Caracter(BaseModel):
    id_caracter: Optional[int]
    caracter: str    
    video: str

class DatabaseConfig(BaseModel):
    USER: str
    PWD: str
    DB_NAME: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    email: str
    role: str