

from sqlalchemy import  Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    username = Column(String, index=True, unique= True, nullable= False)
    full_name = Column(String)
    password = Column(String, index=True, nullable= False)
    

    books = relationship("Book", back_populates="user")


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    title = Column(String, index=True, nullable= False)
    author = Column(String, index=True, nullable= False)
    description = Column(String, index=True, nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates= "books")







