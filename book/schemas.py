from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str 
    author: str
    description: str

class Book(BookBase):
    id : int
    user_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    full_name : str
    password: str

class User(UserBase):
    id: int


#Enforcing data validation and raps attributes around book object
#Also helps to filter a model
   
       
    model_config = ConfigDict(from_attributes = True)



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
       




   
